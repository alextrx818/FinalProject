"""
Handle basketball prematch data.
"""

import requests
import logging
from typing import Dict, List, Optional
from config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class BasketballPrematchFetcher:
    def __init__(self):
        self.base_url = API_URLS["bet365"]
        self.headers = {
            "x-rapidapi-key": API_CREDENTIALS["bet365"]["api_key"],
            "x-rapidapi-host": API_CREDENTIALS["bet365"]["api_host"]
        }
        self.config = REQUEST_CONFIG

    def fetch_prematch_events(self, league_id: Optional[str] = None) -> Optional[List[Dict]]:
        """Fetch upcoming basketball matches"""
        try:
            url = f"{self.base_url}/get_prematch_events/basketball"
            params = {}
            if league_id:
                params["league_id"] = league_id
                
            response = requests.get(
                url, 
                headers=self.headers,
                params=params,
                timeout=self.config["timeout"]
            )
            response.raise_for_status()
            
            events = response.json()
            logger.info(f"Successfully fetched {len(events)} upcoming basketball matches")
            return events
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching upcoming basketball matches: {str(e)}")
            return None

    def fetch_prematch_odds(self, event_id: str) -> Optional[Dict]:
        """Fetch prematch odds for a specific basketball match"""
        try:
            url = f"{self.base_url}/get_prematch_odds/{event_id}"
            response = requests.get(
                url, 
                headers=self.headers,
                timeout=self.config["timeout"]
            )
            response.raise_for_status()
            
            odds = response.json()
            logger.info(f"Successfully fetched prematch odds for basketball match {event_id}")
            return odds
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching prematch odds for basketball match {event_id}: {str(e)}")
            return None
