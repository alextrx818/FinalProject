"""
Fetch tennis in-play odds from BetsAPI.
"""

import requests
import logging
from typing import Dict, List, Optional
from config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class BetsAPIInplayOddsFetcher:
    def __init__(self):
        self.base_url = API_URLS["betsapi"]
        self.api_key = API_CREDENTIALS["betsapi"]["api_key"]
        self.config = REQUEST_CONFIG

    def fetch_odds(self, event_id: str) -> Optional[Dict]:
        """Fetch odds for a specific tennis match"""
        try:
            url = f"{self.base_url}/event/odds"
            params = {
                "token": self.api_key,
                "event_id": event_id
            }
            
            response = requests.get(
                url, 
                params=params,
                timeout=self.config["timeout"]
            )
            response.raise_for_status()
            
            data = response.json()
            if data.get("success") == 1:
                odds = data.get("results", {})
                logger.info(f"Successfully fetched odds for match {event_id} from BetsAPI")
                return odds
            else:
                logger.error(f"BetsAPI error: {data.get('error')}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching odds for match {event_id} from BetsAPI: {str(e)}")
            return None

    def fetch_odds_for_matches(self, event_ids: List[str]) -> Dict[str, Dict]:
        """Fetch odds for multiple tennis matches"""
        all_odds = {}
        for event_id in event_ids:
            odds = self.fetch_odds(event_id)
            if odds:
                all_odds[event_id] = odds
        
        logger.info(f"Successfully fetched odds for {len(all_odds)}/{len(event_ids)} matches from BetsAPI")
        return all_odds
