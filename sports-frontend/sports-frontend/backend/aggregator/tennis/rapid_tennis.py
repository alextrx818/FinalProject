import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TennisFetcher:
    def __init__(self):
        # First API - Bet365 Inplay
        self.inplay_url = "https://bet365-api-inplay.p.rapidapi.com/bet365/get_sport_events/tennis"
        # Second API - BetsAPI Odds
        self.odds_url = "https://betsapi.com/api/bet365/tennis"
        
        self.headers = {
            "x-rapidapi-key": "750ad01770msh9716fc05e7ecc56p15565fjsn93e405806783",
            "x-rapidapi-host": "bet365-api-inplay.p.rapidapi.com"
        }

    def fetch_inplay_matches(self):
        """Fetch raw inplay tennis matches from first API"""
        try:
            response = requests.get(self.inplay_url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching inplay matches: {str(e)}")
            return None

    def fetch_odds_data(self):
        """Fetch raw tennis odds from second API"""
        try:
            response = requests.get(self.odds_url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching odds data: {str(e)}")
            return None

if __name__ == "__main__":
    fetcher = TennisFetcher()
    inplay_data = fetcher.fetch_inplay_matches()
    odds_data = fetcher.fetch_odds_data()
    
    if inplay_data and odds_data:
        print("Successfully fetched both raw data sources")
