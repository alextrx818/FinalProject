import logging
from typing import List, Dict, Any, Optional
from rapidfuzz import fuzz

logger = logging.getLogger(__name__)

class TennisMerger:
    # Constants for name matching
    PUNCTUATIONS = [",", "-", "'"]  # Periods handled separately
    FUZZ_THRESHOLD = 80  # Similarity score threshold (0-100)

    def normalize_name(self, name: str) -> str:
        """
        Basic normalization for player names:
        - Convert to lowercase
        - Handle initials (j.r. -> jr)
        - Replace punctuation with spaces
        - Collapse multiple spaces
        - Special handling for multiple initials
        """
        name = name.lower()
        # Replace certain punctuation (hyphens, commas, apostrophes) with spaces
        # but keep periods for special handling of initials
        for ch in [",", "-", "'"]:
            name = name.replace(ch, " ")

        # Split on whitespace
        tokens = name.split()
        
        expanded_tokens = []
        for token in tokens:
            # If this chunk has multiple periods (e.g., "j.r."), let's split them out
            if token.count(".") > 1:
                # Example: "j.r." -> split on "." -> ["j", "r", ""]
                subparts = token.split(".")
                # Filter out empty strings and re-add the "." so "j" -> "j."
                for sp in subparts:
                    if sp:  # if not empty
                        expanded_tokens.append(sp + ".")
            else:
                expanded_tokens.append(token)

        # Now we have a list where multiple initials are separated, e.g. ["j.", "r."] instead of "j.r."
        # Next we merge consecutive single-letter initials:
        merged_parts = []
        i = 0
        while i < len(expanded_tokens):
            part = expanded_tokens[i]
            
            # Check if this part is a single-letter+period, e.g. "j."
            if len(part) == 2 and part[1] == "." and part[0].isalpha():
                # Look ahead to see if next is also single-letter+period
                if (i + 1 < len(expanded_tokens)
                    and len(expanded_tokens[i+1]) == 2
                    and expanded_tokens[i+1][1] == "."
                    and expanded_tokens[i+1][0].isalpha()):
                    
                    # Merge them, e.g. "j." + "r." -> "jr"
                    combined = part[0] + expanded_tokens[i+1][0]
                    merged_parts.append(combined)
                    i += 2  # Skip the next token (we merged it)
                else:
                    # Just a single initial on its own, strip the period
                    merged_parts.append(part[0])
                    i += 1
            else:
                # Replace any leftover periods in longer tokens with space
                part = part.replace(".", " ")
                merged_parts.append(part)
                i += 1

        # Join and split again to clean up extra spaces
        result = " ".join(merged_parts)
        result = " ".join(result.split())
        return result

    def fuzzy_match_names(self, name1: str, name2: str, threshold: Optional[int] = None) -> bool:
        """
        Uses RapidFuzz to measure string similarity.
        Uses partial_ratio to better handle abbreviated names (e.g., "N. Djokovic" vs "Novak Djokovic")
        """
        if threshold is None:
            threshold = self.FUZZ_THRESHOLD
            
        norm1 = self.normalize_name(name1)
        norm2 = self.normalize_name(name2)
        
        # Use partial_ratio for better matching of abbreviated names
        ratio = fuzz.partial_ratio(norm1, norm2)
        return ratio >= threshold

    def names_are_equivalent(
        self,
        rapid_home: str,
        rapid_away: str,
        bets_home: str,
        bets_away: str,
        threshold: Optional[int] = None
    ) -> bool:
        """
        Checks if two pairs of names (rapid vs. bets) represent the same match
        by either direct or flipped fuzzy matching.
        """
        if threshold is None:
            threshold = self.FUZZ_THRESHOLD

        norm_rapid_home = self.normalize_name(rapid_home)
        norm_rapid_away = self.normalize_name(rapid_away)
        norm_bets_home = self.normalize_name(bets_home)
        norm_bets_away = self.normalize_name(bets_away)

        # Try direct match (home->home, away->away)
        direct_match = (
            self.fuzzy_match_names(norm_rapid_home, norm_bets_home, threshold) and
            self.fuzzy_match_names(norm_rapid_away, norm_bets_away, threshold)
        )
        
        # Try flipped match (home->away, away->home)
        flipped_match = (
            self.fuzzy_match_names(norm_rapid_home, norm_bets_away, threshold) and
            self.fuzzy_match_names(norm_rapid_away, norm_bets_home, threshold)
        )
        
        return direct_match or flipped_match

    def merge_events_and_odds(self, events: List[Dict], odds: Dict[str, Dict]) -> List[Dict]:
        """
        Merge tennis events with their corresponding odds data.
        For RapidAPI data, odds are in raw_odds_data field.
        """
        merged_data = []
        
        for event in events:
            match_id = event.get("match_id")
            if not match_id:
                continue
                
            # For RapidAPI data
            if "raw_odds_data" in event:
                match_odds = event["raw_odds_data"]
            # For BetsAPI data
            elif match_id in odds:
                match_odds = odds[match_id]
            else:
                match_odds = {}
            
            merged_match = {
                **event,
                "odds": match_odds
            }
            merged_data.append(merged_match)
            
        logger.info(f"Merged {len(merged_data)} matches with their odds")
        return merged_data

    def merge(self, bets_data: List[Dict[str, Any]], rapid_data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Merges data from BetsAPI (prematch) and RapidAPI (in-play),
        attempting to match by fuzzy-comparing player names.
        """
        merged_records: List[Dict[str, Any]] = []
        matched_indices = set()  # Track indices instead of dicts

        # 1) Process each Rapid record
        for rapid_idx, rd in enumerate(rapid_data):
            try:
                event_data = rd.get("raw_event_data", {})
                rapid_home = event_data.get("team1", "")
                rapid_away = event_data.get("team2", "")

                found_match = False
                # Look for matching BetsAPI record
                for bets_idx, bd in enumerate(bets_data):
                    if bets_idx in matched_indices:
                        continue  # Skip already matched records
                        
                    try:
                        bets_players = bd.get("players", {})
                        bets_home = bets_players.get("home", "")
                        bets_away = bets_players.get("away", "")

                        if self.names_are_equivalent(
                            rapid_home, rapid_away,
                            bets_home, bets_away
                        ):
                            found_match = True
                            matched_indices.add(bets_idx)

                            merged_records.append({
                                "home_player": bets_home,  # Use BetsAPI names as canonical
                                "away_player": bets_away,
                                "betsapi_data": bd,
                                "rapid_data": rd
                            })
                            break  # Found our match, move to next Rapid record

                    except Exception as e:
                        logger.error(f"Error comparing BetsAPI record to Rapid record: {str(e)}")

                if not found_match:
                    # Store Rapid record without BetsAPI match
                    merged_records.append({
                        "home_player": rapid_home,
                        "away_player": rapid_away,
                        "betsapi_data": None,
                        "rapid_data": rd
                    })

            except Exception as e:
                logger.error(f"Error processing Rapid record #{rapid_idx}: {str(e)}")

        # 2) Add any unmatched BetsAPI records
        for bets_idx, bd in enumerate(bets_data):
            if bets_idx not in matched_indices:
                try:
                    bets_players = bd.get("players", {})
                    home_name = bets_players.get("home", "")
                    away_name = bets_players.get("away", "")
                    
                    merged_records.append({
                        "home_player": home_name,
                        "away_player": away_name,
                        "betsapi_data": bd,
                        "rapid_data": None
                    })
                except Exception as e:
                    logger.error(f"Error processing unmatched BetsAPI record: {str(e)}")

        logger.info(f"Merging complete. Total records: {len(merged_records)}")
        return merged_records
