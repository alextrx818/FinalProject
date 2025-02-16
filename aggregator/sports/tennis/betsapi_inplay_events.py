"""
Fetch tennis in-play events from BetsAPI.
"""

import requests
import logging
from typing import Dict, List, Optional
from config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class BetsAPIInplayEventsFetcher:
    def __init__(self):
        self.base_url = API_URLS["betsapi"]
        self.api_key = API_CREDENTIALS["betsapi"]["api_key"]
        self.config = REQUEST_CONFIG

    def fetch_events(self) -> Optional[List[Dict]]:
        """Fetch all live tennis events from BetsAPI"""
        try:
            url = f"{self.base_url}/events/inplay"
            params = {
                "token": self.api_key,
                "sport_id": 13  # Tennis sport ID in BetsAPI
            }
            
            response = requests.get(
                url, 
                params=params,
                timeout=self.config["timeout"]
            )
            response.raise_for_status()
            
            data = response.json()
            if data.get("success") == 1:
                events = data.get("results", [])
                logger.info(f"Successfully fetched {len(events)} live tennis events from BetsAPI")
                return events
            else:
                logger.error(f"BetsAPI error: {data.get('error')}")
                return None
                
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching tennis events from BetsAPI: {str(e)}")
            return None
