import os
import requests
from typing import Dict, List, Optional
import time

class Bet365Client:
    BASE_URL = "https://bet365-api-inplay.p.rapidapi.com/bet365"
    
    def __init__(self, api_key: str):
        self.headers = {
            "x-rapidapi-key": api_key,
            "x-rapidapi-host": "bet365-api-inplay.p.rapidapi.com"
        }
        
    def get_tennis_events(self) -> List[Dict]:
        """Fetch all in-play tennis events"""
        url = f"{self.BASE_URL}/get_sport_events/tennis"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching tennis events: {e}")
            return []

    def get_event_markets(self, event_id: str) -> Optional[Dict]:
        """Fetch markets for a specific event"""
        url = f"{self.BASE_URL}/get_event_with_markets/{event_id}"
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching markets for event {event_id}: {e}")
            return None

    def get_all_tennis_data(self) -> List[Dict]:
        """Fetch all tennis events and their corresponding markets"""
        events_data = self.get_tennis_events()
        full_data = []
        
        for event in events_data:
            event_id = event.get('id')
            if event_id:
                # Add a small delay to avoid hitting rate limits
                time.sleep(1)
                market_data = self.get_event_markets(event_id)
                if market_data:
                    full_data.append({
                        'event': event,
                        'markets': market_data
                    })
        
        return full_data
