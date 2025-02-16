"""
Fetch basketball in-play events.
"""

import requests
import logging
from typing import Dict, List, Optional
from config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class BasketballInplayEventsFetcher:
    def __init__(self):
        self.base_url = API_URLS["bet365"]
        self.headers = {
            "x-rapidapi-key": API_CREDENTIALS["bet365"]["api_key"],
            "x-rapidapi-host": API_CREDENTIALS["bet365"]["api_host"]
        }
        self.config = REQUEST_CONFIG

    def fetch_events(self) -> Optional[List[Dict]]:
        """Fetch all live basketball events"""
        try:
            url = f"{self.base_url}/get_sport_events/basketball"
            response = requests.get(
                url, 
                headers=self.headers,
                timeout=self.config["timeout"]
            )
            response.raise_for_status()
            
            events = response.json()
            logger.info(f"Successfully fetched {len(events)} live basketball events")
            return events
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching basketball events: {str(e)}")
            return None
