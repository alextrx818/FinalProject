import requests
import logging
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed
from aggregator.config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class RapidInplayOddsFetcher:
    def __init__(self):
        self.api_key = API_CREDENTIALS["bet365"]["api_key"]
        self.api_host = API_CREDENTIALS["bet365"]["api_host"]
        self.headers = {
            "x-rapidapi-key": self.api_key,
            "x-rapidapi-host": self.api_host
        }

    def fetch_inplay_tennis_events(self) -> List[Dict]:
        """
        Fetch all live tennis events (including marketFI IDs, etc.)
        from the in-play endpoint.
        """
        url = f"https://{self.api_host}/bet365/get_sport_events/tennis"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def fetch_event_odds(self, event_id: str) -> Dict:
        """
        Fetch odds for a specific event using its ID.
        """
        url = f"https://{self.api_host}/bet365/get_event_with_markets/{event_id}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def get_tennis_data(self) -> List[Dict]:
        """
        Main logic to:
          1) Fetch live in-play tennis events.
          2) Extract their IDs.
          3) Concurrently fetch odds for each event.
          4) Merge the odds data back into the base event data.
          5) Return the combined data (ready for parsing/storage).
        """
        # 1) Fetch in-play tennis events
        events = self.fetch_inplay_tennis_events()

        # 2) Build a list of event IDs + keep basic event details
        combined_data = []
        event_ids = []

        for event in events:
            event_id = event.get("marketFI")
            # Store the base event info
            combined_data.append({
                "event_id": event_id,
                "eventName": event.get("eventName"),
                "liga": event.get("liga"),
                "team1": event.get("team1"),
                "team2": event.get("team2"),
                "game": event.get("game"),
                "marketsCount": event.get("marketsCount"),
            })

            if event_id:
                event_ids.append(event_id)

        # 3) Concurrently fetch odds for each event ID
        with ThreadPoolExecutor(max_workers=10) as executor:
            future_to_id = {
                executor.submit(self.fetch_event_odds, eid): eid
                for eid in event_ids
            }

            # 4) Merge odds data back into combined_data
            for future in as_completed(future_to_id):
                eid = future_to_id[future]
                try:
                    odds_data = future.result()
                except Exception as exc:
                    logger.error(f"Error fetching odds for {eid}: {exc}")
                    odds_data = {}

                # Attach the odds_data to the correct event in combined_data
                for c_data in combined_data:
                    if c_data["event_id"] == eid:
                        c_data["odds_data"] = odds_data
                        break

        # 5) Return the combined data
        return combined_data
