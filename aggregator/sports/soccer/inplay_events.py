"""
Fetch soccer in-play events.
"""

import requests
import logging
from typing import Dict, List, Optional
from aggregator.config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class SoccerInplayEventsFetcher:
    def __init__(self):
        self.base_url = API_URLS["bet365"]
        self.headers = {
            "x-rapidapi-key": API_CREDENTIALS["bet365"]["api_key"],
            "x-rapidapi-host": API_CREDENTIALS["bet365"]["api_host"]
        }
        self.config = REQUEST_CONFIG

    def fetch_events(self) -> Optional[List[Dict]]:
        """Fetch all live soccer events"""
        try:
            url = f"{self.base_url}/get_sport_events/soccer"
            response = requests.get(
                url, 
                headers=self.headers,
                timeout=self.config["timeout"]
            )
            response.raise_for_status()
            
            events = response.json()
            logger.info(f"Successfully fetched {len(events)} live soccer events")
            return events
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching soccer events: {str(e)}")
            return None
