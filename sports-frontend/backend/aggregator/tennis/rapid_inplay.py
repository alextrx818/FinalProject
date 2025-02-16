import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TennisFetcher:
    def __init__(self):
        self.base_url = "https://bet365-api-inplay.p.rapidapi.com/bet365"
        self.headers = {
            "x-rapidapi-key": "750ad01770msh9716fc05e7ecc56p15565fjsn93e405806783",
            "x-rapidapi-host": "bet365-api-inplay.p.rapidapi.com"
        }

    def fetch_inplay_raw(self):
        """Step 1: Just fetch raw inplay data, no filtering"""
        try:
            url = f"{self.base_url}/get_sport_events/tennis"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching inplay data: {str(e)}")
            return None

    def fetch_odds_raw(self, event_id):
        """Step 2: Just fetch raw odds data, no filtering"""
        try:
            url = f"{self.base_url}/get_event_markets/{event_id}"
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching odds for event {event_id}: {str(e)}")
            return None

if __name__ == "__main__":
    # Test raw data fetching
    fetcher = TennisFetcher()
    
    # Get raw inplay data
    inplay_data = fetcher.fetch_inplay_raw()
    
    if inplay_data and inplay_data.get('results'):
        # Get first event's odds as test
        first_event = inplay_data['results'][0]
        event_id = first_event['id']
        odds_data = fetcher.fetch_odds_raw(event_id)
