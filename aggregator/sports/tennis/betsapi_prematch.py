import requests
import logging
from typing import Dict, List, Optional
from concurrent.futures import ThreadPoolExecutor, as_completed

# Import your config from aggregator
from aggregator.config import API_CREDENTIALS, API_URLS, REQUEST_CONFIG

logger = logging.getLogger(__name__)

class BetsapiPrematch:
    """
    1) Use config data from aggregator.config for tokens/URLs.
    2) Fetch in-play tennis events (sport_id=13), extracting only event IDs.
    3) For each event ID, concurrently fetch prematch data:
       GET /v3/bet365/prematch?token=<API_KEY>&FI=<event_id>
    4) Return { "event_id": <id>, "prematch_data": {...} }
    """

    def __init__(self):
        # Retrieve your token from aggregator.config
        self.token = API_CREDENTIALS["bet365"]["api_key"]
        # If you have a base URL or other config in API_URLS, you can use that here:
        self.base_inplay_url = "https://api.b365api.com/v3/events/inplay"
        self.base_prematch_url = "https://api.b365api.com/v3/bet365/prematch"

        # Optionally, retrieve any request settings from REQUEST_CONFIG
        self.timeout = REQUEST_CONFIG.get("timeout", 30)
        self.max_workers = REQUEST_CONFIG.get("max_workers", 10)

    def fetch_inplay_tennis_ids(self) -> List[str]:
        """
        Fetch all in-play tennis events:
          GET /v3/events/inplay?sport_id=13&token=<token>
        Return a list of event IDs as strings.
        """
        url = f"{self.base_inplay_url}?sport_id=13&token={self.token}"
        logger.info(f"Fetching in-play tennis events from {url}")
        resp = requests.get(url, timeout=self.timeout)
        resp.raise_for_status()

        data = resp.json()
        events = data.get("results", [])
        inplay_ids = []

        for event in events:
            # The ID might be under 'id' or 'FI'
            fi = event.get("id") or event.get("FI")
            if fi:
                inplay_ids.append(str(fi))

        logger.info(f"Found {len(inplay_ids)} in-play tennis match IDs.")
        return inplay_ids

    def fetch_prematch_data(self, event_id: str) -> Dict:
        """
        For a given event_id, fetch the full prematch data:
          GET /v3/bet365/prematch?token=<token>&FI=<event_id>
        Return the full JSON response.
        """
        url = f"{self.base_prematch_url}?token={self.token}&FI={event_id}"
        logger.debug(f"Fetching prematch data for event_id={event_id} from {url}")
        resp = requests.get(url, timeout=self.timeout)
        resp.raise_for_status()

        return resp.json()

    def get_tennis_data(self) -> List[Dict]:
        """
        Main logic:
          - Fetch all in-play tennis IDs.
          - Concurrently fetch prematch data for each ID.
          - Return a list of { "event_id": <id>, "prematch_data": <full JSON> }.
        """
        inplay_ids = self.fetch_inplay_tennis_ids()
        results = []

        logger.info("Starting concurrent fetch of prematch data...")
        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            future_to_id = {
                executor.submit(self.fetch_prematch_data, eid): eid
                for eid in inplay_ids
            }

            for future in as_completed(future_to_id):
                eid = future_to_id[future]
                try:
                    data = future.result()
                except Exception as exc:
                    logger.error(f"Error fetching prematch data for {eid}: {exc}")
                    results.append({
                        "event_id": eid,
                        "error": str(exc),
                        "prematch_data": {}
                    })
                else:
                    results.append({
                        "event_id": eid,
                        "prematch_data": data
                    })

        logger.info(f"Fetched prematch data for {len(results)} events.")
        return results


if __name__ == "__main__":
    """
    Example usage:
      1) Ensure aggregator.config has your bet365 token in API_CREDENTIALS["bet365"]["api_key"].
      2) Ensure you set up logging if desired (e.g. logging.basicConfig(level=logging.INFO)).
      3) Run this script to fetch in-play event IDs and their prematch data.
    """
    logging.basicConfig(level=logging.INFO)
    fetcher = BetsapiPrematch()
    try:
        data = fetcher.get_tennis_data()
        print(f"Fetched prematch data for {len(data)} in-play events.")
        # Show or process data
        for item in data:
            print(f"Event ID: {item['event_id']}")
            if "error" in item:
                print(f"  ERROR: {item['error']}")
            else:
                # The entire JSON can be huge, so print a summary or partial
                pm = item["prematch_data"]
                print(f"  Keys: {list(pm.keys())} | success={pm.get('success')}")
    except Exception as e:
        print(f"Failed to fetch data: {e}")
