"""
Combines soccer data from multiple APIs if needed.
"""

from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class SoccerMerger:
    def merge_events_and_odds(self, events: List[Dict], odds: Dict[str, Dict]) -> List[Dict]:
        """Merge soccer events with their corresponding odds data"""
        merged_data = []
        
        for event in events:
            match_id = event.get("match_id")
            if not match_id:
                continue
                
            match_odds = odds.get(match_id, {})
            
            merged_match = {
                **event,
                "odds": match_odds
            }
            merged_data.append(merged_match)
            
        logger.info(f"Merged {len(merged_data)} soccer matches with their odds")
        return merged_data
