"""
Common parsing logic for basketball data.
"""

from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class BasketballParser:
    def parse_events(self, raw_events: List[Dict]) -> List[Dict]:
        """Parse raw basketball events data into standardized format"""
        parsed_events = []
        
        for event in raw_events:
            try:
                parsed_event = {
                    "match_id": event.get("id"),
                    "event_name": event.get("name"),
                    "status": event.get("status"),
                    "score": {
                        "home": event.get("home_score"),
                        "away": event.get("away_score"),
                        "period": event.get("period")
                    },
                    "teams": {
                        "home": event.get("home_team"),
                        "away": event.get("away_team")
                    },
                    "league": event.get("league"),
                    "start_time": event.get("time")
                }
                parsed_events.append(parsed_event)
            except Exception as e:
                logger.error(f"Error parsing basketball event {event.get('id')}: {str(e)}")
                continue
                
        return parsed_events

    def parse_odds(self, raw_odds: Dict) -> Dict:
        """Parse raw basketball odds data into standardized format"""
        parsed_odds = {}
        
        try:
            for market in raw_odds.get("markets", []):
                market_name = market.get("name")
                if not market_name:
                    continue
                    
                parsed_odds[market_name] = {
                    outcome.get("name"): outcome.get("odds")
                    for outcome in market.get("outcomes", [])
                    if outcome.get("name") and outcome.get("odds")
                }
        except Exception as e:
            logger.error(f"Error parsing basketball odds: {str(e)}")
            
        return parsed_odds
