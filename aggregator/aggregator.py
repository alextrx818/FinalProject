"""
Main orchestrator script that coordinates fetching, parsing, and storing data from various sports APIs.
"""

import logging
from typing import Dict, List
import time
from .database.db_utils import DatabaseManager

# Tennis imports
from .sports.tennis.tennis_parser import TennisParser
from .sports.tennis.tennis_merger import TennisMerger
from .sports.tennis.rapid_inplay_events import RapidInplayEventsFetcher as TennisRapidEventsFetcher
from .sports.tennis.rapid_inplay_odds import RapidInplayOddsFetcher as TennisRapidOddsFetcher
from .sports.tennis.betsapi_inplay_events import BetsAPIInplayEventsFetcher as TennisBetsAPIEventsFetcher
from .sports.tennis.betsapi_inplay_odds import BetsAPIInplayOddsFetcher as TennisBetsAPIOddsFetcher

# Soccer imports
from .sports.soccer.soccer_parser import SoccerParser
from .sports.soccer.soccer_merger import SoccerMerger
from .sports.soccer.inplay_events import SoccerInplayEventsFetcher
from .sports.soccer.inplay_odds_markets import SoccerInplayOddsFetcher
from .sports.soccer.prematch import SoccerPrematchFetcher

# Basketball imports
from .sports.basketball.basketball_parser import BasketballParser
from .sports.basketball.basketball_merger import BasketballMerger
from .sports.basketball.inplay_events import BasketballInplayEventsFetcher
from .sports.basketball.inplay_odds_markets import BasketballInplayOddsFetcher
from .sports.basketball.prematch import BasketballPrematchFetcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SportsAggregator:
    def __init__(self):
        self.db = DatabaseManager()
        
        # Tennis components
        self.tennis_parser = TennisParser()
        self.tennis_merger = TennisMerger()
        self.tennis_rapid_events = TennisRapidEventsFetcher()
        self.tennis_rapid_odds = TennisRapidOddsFetcher()
        self.tennis_betsapi_events = TennisBetsAPIEventsFetcher()
        self.tennis_betsapi_odds = TennisBetsAPIOddsFetcher()
        
        # Soccer components
        self.soccer_parser = SoccerParser()
        self.soccer_merger = SoccerMerger()
        self.soccer_events = SoccerInplayEventsFetcher()
        self.soccer_odds = SoccerInplayOddsFetcher()
        self.soccer_prematch = SoccerPrematchFetcher()
        
        # Basketball components
        self.basketball_parser = BasketballParser()
        self.basketball_merger = BasketballMerger()
        self.basketball_events = BasketballInplayEventsFetcher()
        self.basketball_odds = BasketballInplayOddsFetcher()
        self.basketball_prematch = BasketballPrematchFetcher()

    def aggregate_tennis_data(self):
        """Fetch, parse, and store tennis data"""
        try:
            # 1. Fetch events and odds from Rapid API
            rapid_events = self.tennis_rapid_events.fetch_events()
            rapid_odds = self.tennis_rapid_odds.fetch_odds()
            
            # 2. Fetch events and odds from BetsAPI
            betsapi_events = self.tennis_betsapi_events.fetch_events()
            if betsapi_events:
                event_ids = [event.get("id") for event in betsapi_events]
                betsapi_odds = self.tennis_betsapi_odds.fetch_odds_for_matches(event_ids)
            else:
                betsapi_odds = {}

            # 3. Parse the raw data
            parsed_rapid_events = self.tennis_parser.parse_events(rapid_events) if rapid_events else []
            parsed_rapid_odds = self.tennis_parser.parse_odds(rapid_odds) if rapid_odds else {}
            parsed_betsapi_events = self.tennis_parser.parse_events(betsapi_events) if betsapi_events else []
            parsed_betsapi_odds = self.tennis_parser.parse_odds(betsapi_odds) if betsapi_odds else {}

            # 4. Merge data
            rapid_merged = self.tennis_merger.merge_events_and_odds(parsed_rapid_events, parsed_rapid_odds)
            betsapi_merged = self.tennis_merger.merge_events_and_odds(parsed_betsapi_events, parsed_betsapi_odds)
            
            # 5. Store in database
            self.db.store_tennis_data(rapid_merged + betsapi_merged)
            
            logger.info(f"Successfully aggregated tennis data: {len(rapid_merged)} Rapid API events, {len(betsapi_merged)} BetsAPI events")
        except Exception as e:
            logger.error(f"Error aggregating tennis data: {str(e)}")

    def aggregate_soccer_data(self):
        """Fetch, parse, and store soccer data"""
        try:
            # 1. Fetch events and odds
            events = self.soccer_events.fetch_events()
            if events:
                event_ids = [event.get("id") for event in events]
                odds = self.soccer_odds.fetch_odds_for_matches(event_ids)
            else:
                odds = {}

            # 2. Parse the raw data
            parsed_events = self.soccer_parser.parse_events(events) if events else []
            parsed_odds = self.soccer_parser.parse_odds(odds) if odds else {}

            # 3. Merge data
            merged_data = self.soccer_merger.merge_events_and_odds(parsed_events, parsed_odds)

            # 4. Store in database
            self.db.store_soccer_data(merged_data)
            
            logger.info(f"Successfully aggregated soccer data: {len(merged_data)} events")
        except Exception as e:
            logger.error(f"Error aggregating soccer data: {str(e)}")

    def aggregate_basketball_data(self):
        """Fetch, parse, and store basketball data"""
        try:
            # 1. Fetch events and odds
            events = self.basketball_events.fetch_events()
            if events:
                event_ids = [event.get("id") for event in events]
                odds = self.basketball_odds.fetch_odds_for_matches(event_ids)
            else:
                odds = {}

            # 2. Parse the raw data
            parsed_events = self.basketball_parser.parse_events(events) if events else []
            parsed_odds = self.basketball_parser.parse_odds(odds) if odds else {}

            # 3. Merge data
            merged_data = self.basketball_merger.merge_events_and_odds(parsed_events, parsed_odds)

            # 4. Store in database
            self.db.store_basketball_data(merged_data)
            
            logger.info(f"Successfully aggregated basketball data: {len(merged_data)} events")
        except Exception as e:
            logger.error(f"Error aggregating basketball data: {str(e)}")

    def run(self):
        """Main loop to continuously aggregate sports data"""
        while True:
            self.aggregate_tennis_data()
            self.aggregate_soccer_data()
            self.aggregate_basketball_data()
            time.sleep(60)  # Update every minute

if __name__ == "__main__":
    aggregator = SportsAggregator()
    aggregator.run()
