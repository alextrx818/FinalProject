"""
Common parsing logic for tennis data from various APIs.
"""

from typing import Dict, List, Optional
import logging

logger = logging.getLogger(__name__)

class TennisParser:
    def parse_events(self, raw_events: List[Dict]) -> List[Dict]:
        """Parse raw tennis events data into standardized format"""
        parsed_events = []
        
        for event in raw_events:
            try:
                parsed_event = {
                    "match_id": event.get("marketFI"),
                    "event_name": event.get("eventName"),
                    "status": "Live" if event.get("isLive") else "Upcoming",
                    "score": event.get("score"),
                    "players": {
                        "home": event.get("homeTeam"),
                        "away": event.get("awayTeam")
                    },
                    "tournament": event.get("tournament"),
                    "start_time": event.get("startTime")
                }
                parsed_events.append(parsed_event)
            except Exception as e:
                logger.error(f"Error parsing event {event.get('marketFI')}: {str(e)}")
                continue
                
        return parsed_events

    def parse_odds(self, raw_odds: Dict) -> Dict:
        """Parse raw tennis odds data into standardized format"""
        parsed_odds = {}
        
        try:
            for market in raw_odds.get("markets", []):
                market_name = market.get("marketName")
                if not market_name:
                    continue
                    
                parsed_odds[market_name] = {
                    outcome.get("outcomeName"): outcome.get("price")
                    for outcome in market.get("outcomes", [])
                    if outcome.get("outcomeName") and outcome.get("price")
                }
        except Exception as e:
            logger.error(f"Error parsing odds: {str(e)}")
            
        return parsed_odds
