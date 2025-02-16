"""
Fetch tennis in-play odds from Rapid API.
"""

import requests
import logging
from typing import Dict, List, Optional
from config import API_KEYS

logger = logging.getLogger(__name__)

class RapidInplayOddsFetcher:
    def __init__(self):
        self.base_url = "https://bet365-api-inplay.p.rapidapi.com/bet365"
        self.headers = {
            "x-rapidapi-key": API_KEYS["bet365"],
            "x-rapidapi-host": "bet365-api-inplay.p.rapidapi.com"
        }

    def fetch_odds(self, market_fi: str) -> Optional[Dict]:
        """Fetch odds for a specific tennis match"""
        try:
            url = f"{self.base_url}/get_event_markets/{market_fi}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            odds = response.json()
            logger.info(f"Successfully fetched odds for match {market_fi}")
            return odds
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching odds for match {market_fi}: {str(e)}")
            return None

    def fetch_odds_for_matches(self, market_fis: List[str]) -> Dict[str, Dict]:
        """Fetch odds for multiple tennis matches"""
        all_odds = {}
        for market_fi in market_fis:
            odds = self.fetch_odds(market_fi)
            if odds:
                all_odds[market_fi] = odds
        return all_odds
