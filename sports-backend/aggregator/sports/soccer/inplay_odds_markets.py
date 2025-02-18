"""
Fetch soccer in-play odds/markets.
"""

import requests
import logging
from typing import Dict, List, Optional
from config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class SoccerInplayOddsFetcher:
    def __init__(self):
        self.base_url = API_URLS["bet365"]
        self.headers = {
            "x-rapidapi-key": API_CREDENTIALS["bet365"]["api_key"],
            "x-rapidapi-host": API_CREDENTIALS["bet365"]["api_host"]
        }
        self.config = REQUEST_CONFIG

    def fetch_odds(self, event_id: str) -> Optional[Dict]:
        """Fetch odds for a specific soccer match"""
        try:
            url = f"{self.base_url}/get_event_markets/{event_id}"
            response = requests.get(
                url, 
                headers=self.headers,
                timeout=self.config["timeout"]
            )
            response.raise_for_status()
            
            odds = response.json()
            logger.info(f"Successfully fetched odds for soccer match {event_id}")
            return odds
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching odds for soccer match {event_id}: {str(e)}")
            return None

    def fetch_odds_for_matches(self, event_ids: List[str]) -> Dict[str, Dict]:
        """Fetch odds for multiple soccer matches"""
        all_odds = {}
        for event_id in event_ids:
            odds = self.fetch_odds(event_id)
            if odds:
                all_odds[event_id] = odds
        
        logger.info(f"Successfully fetched odds for {len(all_odds)}/{len(event_ids)} soccer matches")
        return all_odds
