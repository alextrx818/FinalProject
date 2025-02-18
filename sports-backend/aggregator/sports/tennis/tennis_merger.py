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

    def reset_fallback_count_if_new_day(self):
        """
        If you want to reset the counter daily,
        check if today's date is different from self.last_reset_date.
        """
        current_date = datetime.now().date()
        if current_date != self.last_reset_date:
            self.fuzzy_fallback_count = 0
            self.last_reset_date = current_date

    def get_possible_ids(self, data_dict: Dict[str, Any], fields: List[str]) -> set:
        """
        Searches each field in 'fields' for any numeric substring (Bet365 ID).
        Returns a set of all IDs found.
        Example fields to check: ["eventId", "bet365_id", "FI"].
        """
        possible_ids = set()
        for field in fields:
            val = data_dict.get(field)
            if val is None:
                continue

            # Convert to string to handle int or str
            val_str = str(val)
            # Find all sequences of digits in that string
            matches = re.findall(r'(\d+)', val_str)
            for match in matches:
                possible_ids.add(match)
        return possible_ids

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
        for ch in self.PUNCTUATIONS:
            name = name.replace(ch, " ")

        tokens = name.split()
        expanded_tokens = []
        for token in tokens:
            # If this chunk has multiple periods (e.g., "j.r."), split them
            if token.count(".") > 1:
                subparts = token.split(".")
                for sp in subparts:
                    if sp:
                        expanded_tokens.append(sp + ".")
            else:
                expanded_tokens.append(token)

        merged_parts = []
        i = 0
        while i < len(expanded_tokens):
            part = expanded_tokens[i]
            # Check if this part is single-letter+period (e.g. "j.")
            if len(part) == 2 and part[1] == "." and part[0].isalpha():
                # Look ahead: next part also single-letter+period?
                if (
                    i + 1 < len(expanded_tokens)
                    and len(expanded_tokens[i+1]) == 2
                    and expanded_tokens[i+1][1] == "."
                    and expanded_tokens[i+1][0].isalpha()
                ):
                    combined = part[0] + expanded_tokens[i+1][0]
                    merged_parts.append(combined)
                    i += 2
                else:
                    merged_parts.append(part[0])  # single initial (strip period)
                    i += 1
            else:
                # Replace leftover periods in longer tokens with space
                part = part.replace(".", " ")
                merged_parts.append(part)
                i += 1

        result = " ".join(merged_parts)
        result = " ".join(result.split())
        return result

    def fuzzy_match_names(self, name1: str, name2: str, threshold: Optional[int] = None) -> bool:
        """
        Uses RapidFuzz to measure string similarity.
        Uses partial_ratio to handle abbreviated names (e.g. "N. Djokovic" vs "Novak Djokovic")
        """
        if threshold is None:
            threshold = self.FUZZ_THRESHOLD

        # Normalize both names
        norm1 = self.normalize_name(name1)
        norm2 = self.normalize_name(name2)
        
        # Get the similarity score
        score = fuzz.partial_ratio(norm1, norm2)
        logger.info(f"Fuzzy match score for '{name1}' vs '{name2}': {score}")
        
        return score >= threshold

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

        # Direct match (home->home, away->away)
        direct_match = (
            self.fuzzy_match_names(rapid_home, bets_home, threshold)
            and self.fuzzy_match_names(rapid_away, bets_away, threshold)
        )
        
        # Flipped match (home->away, away->home)
        flipped_match = (
            self.fuzzy_match_names(rapid_home, bets_away, threshold)
            and self.fuzzy_match_names(rapid_away, bets_home, threshold)
        )
        
        return direct_match or flipped_match

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
        matched_indices = set()

        # Stats counters
        total_rapid_matches = len(rapid_data)
        total_bets_matches = len(bets_data)
        id_matches = 0
        name_matches = 0
        unmatched_rapid = 0

        # For convenience, pre-extract possible IDs from each Bets record
        # so we don't do it repeatedly in the loop.
        bets_possible_ids = []
        for bd in bets_data:
            bets_ids = self.get_possible_ids(bd, ["eventId", "bet365_id", "FI"])
            bets_possible_ids.append(bets_ids)

        # 1) Process each Rapid record
        for rd in rapid_data:
            event_data = rd.get("raw_event_data", {})
            rapid_home = event_data.get("team1", "")
            rapid_away = event_data.get("team2", "")

            # We'll look in raw_event_data for "eventId", "bet365_id", or "FI"
            # You could also consider top-level fields if needed.
            rapid_ids = self.get_possible_ids(event_data, ["eventId", "bet365_id", "FI"])

            logger.info(f"Processing match: {rapid_home} vs {rapid_away}")
            logger.info(f"  Possible IDs from Rapid: {rapid_ids}")

            found_match = False

            for idx, bd in enumerate(bets_data):
                if idx in matched_indices:
                    continue

                bets_players = bd.get("players", {})
                bets_home = bets_players.get("home", "")
                bets_away = bets_players.get("away", "")

                # Check for ID overlap
                if rapid_ids and bets_possible_ids[idx]:
                    overlap = rapid_ids.intersection(bets_possible_ids[idx])
                    if overlap:
                        # We found a direct ID match
                        logger.info(f"ID MATCH! Found overlapping IDs: {overlap}")
                        logger.info(f"  Rapid: {rapid_home} vs {rapid_away}")
                        logger.info(f"  Bets: {bets_home} vs {bets_away}")
                        found_match = True
                        matched_indices.add(idx)
                        id_matches += 1
                        merged_records.append({
                            "home_player": bets_home,
                            "away_player": bets_away,
                            "betsapi_data": bd,
                            "rapid_data": rd
                        })
                        break

                # Only try fuzzy if no ID match
                if not found_match and self.names_are_equivalent(rapid_home, rapid_away, bets_home, bets_away):
                    logger.info("Fallback fuzzy match success.")
                    found_match = True
                    matched_indices.add(idx)
                    merged_records.append({
                        "home_player": bets_home,
                        "away_player": bets_away,
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
        for idx, bd in enumerate(bets_data):
            if idx not in matched_indices:
                bets_players = bd.get("players", {})
                home_name = bets_players.get("home", "")
                away_name = bets_players.get("away", "")
                if len([i for i in range(len(bets_data)) if i not in matched_indices]) <= 3:  # Only show first 3
                    logger.info("\n=== UNMATCHED BETS RECORD ===")
                    logger.info("Players: %s vs %s" % (home_name, away_name))
                    logger.info("Possible IDs found: %s" % bets_possible_ids[idx])
                    logger.info("All fields from record:")
                    for key, value in bd.items():
                        logger.info(f"  {key}: {value}")
                merged_records.append({
                    "home_player": home_name,
                    "away_player": away_name,
                    "betsapi_data": bd,
                    "rapid_data": None
                })

        unmatched_rapid_count = len(rapid_data) - (id_matches + name_matches)
        unmatched_bets_count = len(bets_data) - len(matched_indices)

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
