import requests
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BetsTennisFetcher:
    def __init__(self):
        self.base_url = "https://api.betsapi.com/v1"
        self.token = "YOUR_BETSAPI_TOKEN"  # You'll need to provide this

    def fetch_inplay_matches(self):
        """Fetch raw tennis inplay matches from BetsAPI"""
        try:
            url = f"{self.base_url}/events/inplay"
            params = {
                'sport_id': '13',  # Tennis sport ID for BetsAPI
                'token': self.token
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching BetsAPI inplay matches: {str(e)}")
            return None

    def fetch_odds_data(self, event_id):
        """Fetch raw tennis odds from BetsAPI for a specific event"""
        try:
            url = f"{self.base_url}/event/odds"
            params = {
                'event_id': event_id,
                'token': self.token
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching BetsAPI odds: {str(e)}")
            return None

if __name__ == "__main__":
    fetcher = BetsTennisFetcher()
    inplay_data = fetcher.fetch_inplay_matches()
    
    if inplay_data and inplay_data.get('results'):
        # Get odds for first event as test
        first_event = inplay_data['results'][0]
        event_id = first_event['id']
        odds_data = fetcher.fetch_odds_data(event_id)
        print("Successfully fetched BetsAPI data")
