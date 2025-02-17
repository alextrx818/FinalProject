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
from .sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher as TennisRapidFetcher

# Soccer imports - temporarily commented out
# from .sports.soccer.soccer_parser import SoccerParser
# from .sports.soccer.soccer_merger import SoccerMerger
# from .sports.soccer.inplay_events import SoccerInplayEventsFetcher
# from .sports.soccer.inplay_odds_markets import SoccerInplayOddsFetcher
# from .sports.soccer.prematch import SoccerPrematchFetcher

# Basketball imports - temporarily commented out
# from .sports.basketball.basketball_parser import BasketballParser
# from .sports.basketball.basketball_merger import BasketballMerger
# from .sports.basketball.inplay_events import BasketballInplayEventsFetcher
# from .sports.basketball.inplay_odds_markets import BasketballInplayOddsFetcher
# from .sports.basketball.prematch import BasketballPrematchFetcher

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SportsAggregator:
    def __init__(self):
        self.db = DatabaseManager()
        
        # Tennis components
        self.tennis_parser = TennisParser()
        self.tennis_merger = TennisMerger()
        self.tennis_rapid_fetcher = TennisRapidFetcher()
        
        # Soccer components - temporarily commented out
        # self.soccer_parser = SoccerParser()
        # self.soccer_merger = SoccerMerger()
        # self.soccer_events = SoccerInplayEventsFetcher()
        # self.soccer_odds = SoccerInplayOddsFetcher()
        # self.soccer_prematch = SoccerPrematchFetcher()
        
        # Basketball components - temporarily commented out
        # self.basketball_parser = BasketballParser()
        # self.basketball_merger = BasketballMerger()
        # self.basketball_events = BasketballInplayEventsFetcher()
        # self.basketball_odds = BasketballInplayOddsFetcher()
        # self.basketball_prematch = BasketballPrematchFetcher()

    def aggregate_tennis_data(self):
        """Fetch, parse, and store tennis data"""
        try:
            # 1. Fetch events and odds from Rapid API
            rapid_data = self.tennis_rapid_fetcher.fetch_data()
            
            # 2. Parse the raw data
            parsed_rapid_data = self.tennis_parser.parse_data(rapid_data) if rapid_data else []
            
            # 3. Merge data
            rapid_merged = self.tennis_merger.merge_data(parsed_rapid_data)
            
            # 4. Store in database
            self.db.store_tennis_data(rapid_merged)
            
            logger.info(f"Successfully aggregated tennis data: {len(rapid_merged)} Rapid API events")
        except Exception as e:
            logger.error(f"Error aggregating tennis data: {str(e)}")

    def run(self):
        """Main loop to continuously aggregate sports data"""
        while True:
            self.aggregate_tennis_data()
            # self.aggregate_soccer_data()  # temporarily commented out
            # self.aggregate_basketball_data()  # temporarily commented out
            time.sleep(60)  # Wait 1 minute before next update

if __name__ == "__main__":
    aggregator = SportsAggregator()
    aggregator.run()
