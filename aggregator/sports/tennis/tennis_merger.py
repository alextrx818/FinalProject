import re
import logging
from typing import List, Dict, Any, Optional
from rapidfuzz import fuzz
from datetime import datetime

logger = logging.getLogger(__name__)

class TennisMerger:
    # Constants for name matching
    PUNCTUATIONS = [",", "-", "'"]  # Periods handled separately
    FUZZ_THRESHOLD = 80  # Similarity score threshold (0-100)

    def __init__(self):
        # Track how many times we resort to fuzzy matching
        self.fuzzy_fallback_count = 0
        # Optionally, store today's date so we can reset daily if desired
        self.last_reset_date = datetime.now().date()

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

        # Try direct match (home->home, away->away)
        direct_match = (
            self.fuzzy_match_names(rapid_home, bets_home, threshold) and
            self.fuzzy_match_names(rapid_away, bets_away, threshold)
        )
        
        # Try flipped match (home->away, away->home)
        flipped_match = (
            self.fuzzy_match_names(rapid_home, bets_away, threshold) and
            self.fuzzy_match_names(rapid_away, bets_home, threshold)
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

    def get_player_names_from_record(self, bets_record: Dict[str, Any]) -> tuple:
        """
        Extract player names from a BetsAPI record, checking both players dict and inplay_event.
        Returns a tuple of (home_player, away_player).
        """
        # First try players dict
        players = bets_record.get("players", {})
        home_name = players.get("home", "")
        away_name = players.get("away", "")

        # If either name is empty, try inplay_event
        if not home_name or not away_name:
            inplay = bets_record.get("inplay_event", {})
            home = inplay.get("home", {})
            away = inplay.get("away", {})
            home_name = home_name or home.get("name", "")
            away_name = away_name or away.get("name", "")

        # Update names consistently throughout the record
        if home_name and away_name:
            self.update_names_in_record(bets_record, home_name, away_name)

        return home_name, away_name

    def update_names_in_record(self, record: Dict[str, Any], home_name: str, away_name: str) -> None:
        """
        Update player names consistently throughout a record's nested data structures.
        """
        # Update BetsAPI inplay_event
        if "inplay_event" in record:
            inplay = record["inplay_event"]
            if "home" in inplay:
                inplay["home"]["name"] = home_name
            if "away" in inplay:
                inplay["away"]["name"] = away_name

        # Update RapidAPI raw_event_data
        if "raw_event_data" in record:
            event_data = record["raw_event_data"]
            event_data["team1"] = home_name
            event_data["team2"] = away_name
            # Also update eventName for consistency
            event_data["eventName"] = f"{home_name} - {away_name}"

        # Update players dict if it exists
        if "players" in record:
            record["players"]["home"] = home_name
            record["players"]["away"] = away_name

    def merge(
        self,
        bets_data: List[Dict[str, Any]],
        rapid_data: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Merges data from BetsAPI (prematch) and RapidAPI (in-play).
        1) Attempt ID match by scanning these fields for numeric substrings:
           - "eventId"
           - "bet365_id"
           - "FI"
        2) If no overlap in IDs, fallback to fuzzy name matching.
        3) Track how many times fuzzy is used, log if >10.
        """
        self.reset_fallback_count_if_new_day()

        merged_records: List[Dict[str, Any]] = []
        matched_rapid_indices = set()  # Track which rapid records are matched
        matched_bets_indices = set()   # Track which bets records are matched

        # Stats counters
        total_rapid_matches = len(rapid_data)
        total_bets_matches = len(bets_data)
        id_matches = 0
        name_matches = 0
        unmatched_rapid = 0

        # For convenience, pre-extract possible IDs from each Bets record
        bets_possible_ids = []
        for bd in bets_data:
            bets_ids = self.get_possible_ids(bd, ["eventId", "bet365_id", "FI"])
            bets_possible_ids.append(bets_ids)

        # 1) Process each Rapid record
        for rapid_idx, rd in enumerate(rapid_data):
            if rapid_idx in matched_rapid_indices:
                continue

            event_data = rd.get("raw_event_data", {})
            rapid_home = event_data.get("team1", "")  # Changed from home_player to team1
            rapid_away = event_data.get("team2", "")  # Changed from away_player to team2

            # Look for IDs in raw_event_data
            rapid_ids = self.get_possible_ids(event_data, ["eventId", "bet365_id", "FI"])

            logger.info(f"Processing match: {rapid_home} vs {rapid_away}")
            logger.info(f"  Possible IDs from Rapid: {rapid_ids}")

            found_match = False

            for bets_idx, bd in enumerate(bets_data):
                if bets_idx in matched_bets_indices:
                    continue

                # Get player names using the new helper function
                home_name, away_name = self.get_player_names_from_record(bd)

                # Check for ID overlap
                if rapid_ids and bets_possible_ids[bets_idx]:
                    overlap = rapid_ids.intersection(bets_possible_ids[bets_idx])
                    if overlap:
                        # We found a direct ID match
                        logger.info(f"ID MATCH! Found overlapping IDs: {overlap}")
                        logger.info(f"  Rapid: {rapid_home} vs {rapid_away}")
                        logger.info(f"  Bets: {home_name} vs {away_name}")
                        found_match = True
                        matched_rapid_indices.add(rapid_idx)
                        matched_bets_indices.add(bets_idx)
                        id_matches += 1
                        
                        # Get player names and ensure they're consistent everywhere
                        home_name, away_name = self.get_player_names_from_record(bd)
                        self.update_names_in_record(rd, home_name, away_name)
                        
                        merged_records.append({
                            "home_player": home_name,
                            "away_player": away_name,
                            "betsapi_data": bd,
                            "rapid_data": rd
                        })
                        break

                # Only try fuzzy if no ID match
                if not found_match and self.names_are_equivalent(rapid_home, rapid_away, home_name, away_name):
                    logger.info("Fallback fuzzy match success.")
                    found_match = True
                    matched_rapid_indices.add(rapid_idx)
                    matched_bets_indices.add(bets_idx)
                    merged_records.append({
                        "home_player": home_name,  # Use names from helper function
                        "away_player": away_name,
                        "betsapi_data": bd,
                        "rapid_data": rd
                    })
                    self.fuzzy_fallback_count += 1
                    name_matches += 1
                    break

            if not found_match:
                # No match found, store Rapid record alone
                unmatched_rapid += 1
                if unmatched_rapid <= 3:  # Only show first 3
                    logger.info("\n=== UNMATCHED RAPID RECORD #%d ===" % unmatched_rapid)
                    logger.info("Players: %s vs %s" % (rapid_home, rapid_away))
                    logger.info("Possible IDs found: %s" % rapid_ids)
                    logger.info("All fields from raw_event_data:")
                    for key, value in event_data.items():
                        logger.info(f"  {key}: {value}")
                merged_records.append({
                    "home_player": rapid_home,
                    "away_player": rapid_away,
                    "betsapi_data": None,
                    "rapid_data": rd
                })

        # 2) Add any unmatched BetsAPI records
        for bets_idx, bd in enumerate(bets_data):
            if bets_idx not in matched_bets_indices:
                # Get player names using the new helper function
                home_name, away_name = self.get_player_names_from_record(bd)
                if len([i for i in range(len(bets_data)) if i not in matched_bets_indices]) <= 3:  # Only show first 3
                    logger.info("\n=== UNMATCHED BETS RECORD ===")
                    logger.info("Players: %s vs %s" % (home_name, away_name))
                    logger.info("Possible IDs found: %s" % bets_possible_ids[bets_idx])
                    logger.info("All fields from record:")
                    for key, value in bd.items():
                        logger.info(f"  {key}: {value}")
                merged_records.append({
                    "home_player": home_name,  # Use names from helper function
                    "away_player": away_name,
                    "betsapi_data": bd,
                    "rapid_data": None
                })

        unmatched_rapid_count = len(rapid_data) - (id_matches + name_matches)
        unmatched_bets_count = len(bets_data) - len(matched_bets_indices)

        # Log stats
        logger.info("\nMATCH STATISTICS:")
        logger.info(f"  Total RapidAPI records: {total_rapid_matches}")
        logger.info(f"  Total BetsAPI records: {total_bets_matches}")
        logger.info(f"  ID matches found: {id_matches}")
        logger.info(f"  Fuzzy name matches found: {name_matches}")
        logger.info(f"  Unmatched RapidAPI records: {unmatched_rapid_count}")
        logger.info(f"  Unmatched BetsAPI records: {unmatched_bets_count}")

        # If fuzzy fallback used more than 10 times, log a warning
        if self.fuzzy_fallback_count > 10:
            logger.warning(
                f"Fuzzy fallback used {self.fuzzy_fallback_count} times today!"
            )

        return merged_records

    def get_match_stats(self, merged_data: List[Dict[str, Any]]) -> Dict[str, int]:
        """
        Calculate matching statistics from merged data.
        Returns:
            Dict with stats:
            - successful_matches: number of events matched between both APIs
            - unmatched_bets: number of events only in BetsAPI
            - unmatched_rapid: number of events only in RapidAPI
            - fuzzy_matches: number of matches that used fuzzy matching
        """
        successful_matches = sum(1 for record in merged_data if record.get("betsapi_data") and record.get("rapid_data"))
        unmatched_bets = sum(1 for record in merged_data if record.get("betsapi_data") and not record.get("rapid_data"))
        unmatched_rapid = sum(1 for record in merged_data if record.get("rapid_data") and not record.get("betsapi_data"))
        
        return {
            "successful_matches": successful_matches,
            "unmatched_bets": unmatched_bets,
            "unmatched_rapid": unmatched_rapid,
            "fuzzy_matches": self.fuzzy_fallback_count
        }

    def get_possible_ids(self, data: Dict[str, Any], fields: List[str]) -> set:
        """
        Extracts possible IDs from the given data by scanning the specified fields.
        """
        ids = set()
        for field in fields:
            value = data.get(field)
            if value:
                # Use regular expression to find numeric substrings
                ids.update(re.findall(r'\d+', str(value)))
        return ids

    def reset_fallback_count_if_new_day(self):
        """
        Resets the fuzzy fallback count if today's date is different from the last reset date.
        """
        today = datetime.now().date()
        if today != self.last_reset_date:
            self.fuzzy_fallback_count = 0
            self.last_reset_date = today
