"""
Fetch tennis in-play events from Rapid API.
"""

import requests
import logging
from typing import Dict, List, Optional
from config import API_KEYS

logger = logging.getLogger(__name__)

class RapidInplayEventsFetcher:
    def __init__(self):
        self.base_url = "https://bet365-api-inplay.p.rapidapi.com/bet365"
        self.headers = {
            "x-rapidapi-key": API_KEYS["bet365"],
            "x-rapidapi-host": "bet365-api-inplay.p.rapidapi.com"
        }

    def fetch_events(self) -> Optional[List[Dict]]:
        """Fetch all live tennis events"""
        try:
            url = f"{self.base_url}/get_sport_events/tennis"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            events = response.json()
            logger.info(f"Successfully fetched {len(events)} live tennis events")
            return events
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching tennis events: {str(e)}")
            return None
