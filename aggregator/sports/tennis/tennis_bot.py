import os
import asyncio
import logging
import signal
import time
import json
from typing import Optional, Dict
from datetime import datetime, timedelta
import pytz

# Using absolute imports
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher as RapidTennisFetcher
from aggregator.sports.tennis import tennis_merger
from aggregator.sports.tennis import tennis_parser
from aggregator.sports.tennis import tennis_database

###############################################################################
# Configuration via Environment Variables or defaults
###############################################################################
DEFAULT_CONCURRENCY = int(os.getenv("TENNIS_BOT_CONCURRENCY", "5"))  # For BetsAPI only
DEFAULT_MAX_RETRIES = int(os.getenv("TENNIS_BOT_MAX_RETRIES", "3"))  # For BetsAPI only
DEFAULT_FETCH_INTERVAL = float(os.getenv("TENNIS_BOT_FETCH_INTERVAL", "60"))
COUNTER_FILE = "tennis_bot_counters.json"  # File to store persistent counters

###############################################################################
# Logging Configuration
###############################################################################
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler("tennis_bot.log", mode='a')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# Avoid adding handlers multiple times
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

###############################################################################
# Graceful Shutdown Setup
###############################################################################
def shutdown_handler(loop: asyncio.AbstractEventLoop) -> None:
    """
    Signal handler to gracefully shut down the bot.

    This function is triggered by signal handlers (SIGINT, SIGTERM),
    logs a shutdown message, and cancels all running tasks on the
    provided event loop. This allows for an orderly exit of the
    application.
    
    :param loop: The asyncio event loop whose tasks we need to cancel.
    """
    logger.info("Received shutdown signal. Cancelling tasks...")
    for task in asyncio.all_tasks(loop=loop):
        task.cancel()

###############################################################################
# TennisBot Class
###############################################################################
class TennisBot:
    """
    Orchestrates fetching data from:
      1) BetsAPI Prematch (with concurrency/retry logic)
      2) RapidInplayOddsFetcher (no concurrency/retry params)
    Then merges first, parses second, and optionally saves to DB.
    Repeats every fetch_interval seconds.
    """

    def __init__(
        self,
        fetch_interval: Optional[float] = None,
        concurrency_limit: Optional[int] = None,
        max_retries: Optional[int] = None
    ) -> None:
        """
        Initialize the TennisBot with optional configuration overrides.

        :param fetch_interval: Interval in seconds between fetch cycles.
                               Defaults to TENNIS_BOT_FETCH_INTERVAL or 60.
        :param concurrency_limit: Max concurrent requests for BetsAPI.
                                  Defaults to TENNIS_BOT_CONCURRENCY or 5.
        :param max_retries: Max retries for BetsAPI requests.
                            Defaults to TENNIS_BOT_MAX_RETRIES or 3.
        """
        self.fetch_interval = fetch_interval or DEFAULT_FETCH_INTERVAL

        # BetsAPI fetcher with concurrency + retry logic
        self.betsapi_fetcher = BetsapiPrematch(
            concurrency_limit=concurrency_limit or DEFAULT_CONCURRENCY,
            max_retries=max_retries or DEFAULT_MAX_RETRIES
        )

        # RapidInplayOddsFetcher does NOT accept concurrency/retry parameters
        self.rapid_fetcher = RapidTennisFetcher()

        # Initialize with EST timezone
        est = pytz.timezone('America/New_York')
        current_date = datetime.now(est)
        
        # Load persisted counters or initialize new ones
        self.load_counters()
        
        # Initialize time tracking
        self.last_reset_date = current_date.date()
        self.last_reset_month = current_date.month
        self.last_reset_hour = current_date.hour

    def load_counters(self) -> None:
        """Load counters from file or initialize new ones if file doesn't exist"""
        try:
            with open(COUNTER_FILE, 'r') as f:
                data = json.load(f)
                self.current_cycle_calls = data.get('current_cycle_calls', {'betsapi': 0, 'rapidapi': 0})
                self.hourly_total_calls = data.get('hourly_total_calls', {'betsapi': 0, 'rapidapi': 0})
                self.daily_total_calls = data.get('daily_total_calls', {'betsapi': 0, 'rapidapi': 0})
                self.monthly_total_calls = data.get('monthly_total_calls', {'betsapi': 0, 'rapidapi': 0})
                logger.info("Loaded persisted counters from file")
        except FileNotFoundError:
            logger.info("No persisted counters found, initializing new ones")
            self.current_cycle_calls = {'betsapi': 0, 'rapidapi': 0}
            self.hourly_total_calls = {'betsapi': 0, 'rapidapi': 0}
            self.daily_total_calls = {'betsapi': 0, 'rapidapi': 0}
            self.monthly_total_calls = {'betsapi': 0, 'rapidapi': 0}

    def save_counters(self) -> None:
        """Save current counter values to file"""
        data = {
            'current_cycle_calls': self.current_cycle_calls,
            'hourly_total_calls': self.hourly_total_calls,
            'daily_total_calls': self.daily_total_calls,
            'monthly_total_calls': self.monthly_total_calls
        }
        with open(COUNTER_FILE, 'w') as f:
            json.dump(data, f)

    def reset_hourly_counters(self) -> None:
        """Reset hourly API call counters if it's a new hour"""
        est = pytz.timezone('America/New_York')
        current_hour = datetime.now(est).hour
        if current_hour != self.last_reset_hour:
            logger.info(f"\nResetting hourly counters (Hour changed from {self.last_reset_hour} to {current_hour})")
            self.hourly_total_calls = {'betsapi': 0, 'rapidapi': 0}
            self.last_reset_hour = current_hour

    def reset_monthly_counters(self) -> None:
        """Reset monthly API call counters if it's a new month"""
        est = pytz.timezone('America/New_York')
        current_date = datetime.now(est)
        if current_date.month != self.last_reset_month:
            logger.info(f"\nResetting monthly counters (Month changed from {self.last_reset_month} to {current_date.month})")
            self.monthly_total_calls = {'betsapi': 0, 'rapidapi': 0}
            self.last_reset_month = current_date.month

    def reset_daily_counters(self) -> None:
        """Reset daily API call counters if it's a new day in EST"""
        est = pytz.timezone('America/New_York')
        current_date = datetime.now(est).date()
        if current_date > self.last_reset_date:
            self.daily_total_calls = {'betsapi': 0, 'rapidapi': 0}
            self.last_reset_date = current_date

    def reset_cycle_counters(self) -> None:
        """Reset API call counters for new fetch cycle"""
        self.current_cycle_calls = {'betsapi': 0, 'rapidapi': 0}

    async def run(self) -> None:
        """
        Main loop: run forever, fetching from both APIs every self.fetch_interval seconds,
        unless a shutdown signal is received.

        1) Fetch data from BetsAPI (prematch).
        2) Fetch data from RapidAPI (live).
        3) Merge data using tennis_merger (IDs, fuzzy name match, etc.).
        4) (Optional) parse merged data and save to DB (commented out for now).
        5) Sleep any remaining time so we start the next cycle at roughly fetch_interval.
        
        This continues until an asyncio.CancelledError is raised
        (e.g., by our shutdown_handler upon receiving SIGINT/SIGTERM).
        """
        logger.info("TennisBot started. Press Ctrl+C to stop.")

        while True:
            start_time = time.time()
            logger.info("Starting fetch cycle...")

            try:
                # Reset all counters at start
                self.reset_cycle_counters()
                self.reset_hourly_counters()
                self.reset_daily_counters()
                self.reset_monthly_counters()

                # 1) Fetch data from BetsAPI
                logger.info("[BetsAPI] Beginning fetch...")
                bets_data = await self.betsapi_fetcher.get_tennis_data()
                self.current_cycle_calls['betsapi'] = len(bets_data)    # Track current cycle
                self.hourly_total_calls['betsapi'] += len(bets_data)    # Track hourly total
                self.daily_total_calls['betsapi'] += len(bets_data)     # Track daily total
                self.monthly_total_calls['betsapi'] += len(bets_data)   # Track monthly total
                logger.info(f"[BetsAPI] Fetch returned {len(bets_data)} records.")

                # 2) Fetch data from Rapid Tennis
                logger.info("[RapidAPI] Beginning fetch...")
                rapid_data = await self.rapid_fetcher.get_tennis_data()
                self.current_cycle_calls['rapidapi'] = len(rapid_data)    # Track current cycle
                self.hourly_total_calls['rapidapi'] += len(rapid_data)    # Track hourly total
                self.daily_total_calls['rapidapi'] += len(rapid_data)     # Track daily total
                self.monthly_total_calls['rapidapi'] += len(rapid_data)   # Track monthly total
                logger.info(f"[RapidAPI] Fetch returned {len(rapid_data)} records.")

                # Save counters after updating
                self.save_counters()

                # 3) Merge data (Merger comes first)
                logger.info("Merging data...")
                merger = tennis_merger.TennisMerger()
                merged_data = merger.merge(bets_data, rapid_data)
                stats = merger.get_match_stats(merged_data)
                logger.info("\nAPI AND MATCH STATISTICS:")
                logger.info("  API Calls:")
                logger.info("    Current Cycle:")
                logger.info(f"      BetsAPI calls: {self.current_cycle_calls['betsapi']}")
                logger.info(f"      RapidAPI calls: {self.current_cycle_calls['rapidapi']}")
                logger.info("    Hourly Totals (EST):")
                logger.info(f"      BetsAPI calls: {self.hourly_total_calls['betsapi']}")
                logger.info(f"      RapidAPI calls: {self.hourly_total_calls['rapidapi']}")
                logger.info("    Daily Totals (EST):")
                logger.info(f"      BetsAPI calls: {self.daily_total_calls['betsapi']}")
                logger.info(f"      RapidAPI calls: {self.daily_total_calls['rapidapi']}")
                logger.info("    Monthly Totals (EST):")
                logger.info(f"      BetsAPI calls: {self.monthly_total_calls['betsapi']}")
                logger.info(f"      RapidAPI calls: {self.monthly_total_calls['rapidapi']}")
                logger.info("  Match Results:")
                logger.info(f"    Total RapidAPI records: {len(rapid_data)}")
                logger.info(f"    Total BetsAPI records: {len(bets_data)}")
                logger.info(f"    ID matches found: {stats['successful_matches']}")
                logger.info(f"    Fuzzy name matches found: {stats['fuzzy_matches']}")
                logger.info(f"    Unmatched RapidAPI records: {stats['unmatched_rapid']}")
                logger.info(f"    Unmatched BetsAPI records: {stats['unmatched_bets']}")

                # Show unmatched events details (for debugging)
                if stats['unmatched_rapid'] > 0:
                    logger.info("\nUnmatched RapidAPI events:")
                    for event in stats['unmatched_rapid_events']:
                        home = event['raw_event_data'].get('home_player', 'Unknown')
                        away = event['raw_event_data'].get('away_player', 'Unknown')
                        logger.info(f"  {home} vs {away}")

                if stats['unmatched_bets'] > 0:
                    logger.info("\nUnmatched BetsAPI events:")
                    for event in stats['unmatched_bets_events']:
                        names = merger.get_player_names_from_record(event)
                        # Get all possible IDs
                        top_bet365_id = event.get('bet365_id', 'Not found')
                        inplay_id = event.get('inplay_event', {}).get('id', 'Not found')
                        fi_id = event.get('FI', 'Not found')
                        top_id = event.get('id', 'Not found')
                        
                        logger.info(f"  {names[0]} vs {names[1]}")
                        logger.info(f"    - bet365_id: {top_bet365_id}")
                        logger.info(f"    - inplay_event.id: {inplay_id}")
                        logger.info(f"    - FI: {fi_id}")
                        logger.info(f"    - id: {top_id}")

                # 4) Parse data (Parser after merging)
                """
                logger.info("Parsing merged data...")
                parsed_data = tennis_parser.parse(merged_data)
                logger.info(f"Parsed data size: {len(parsed_data)}")
                """

                # 5) Save to the database (if desired)
                """
                logger.info("Saving parsed data to database...")
                tennis_database.save(parsed_data)
                logger.info("Data successfully saved to the database.")
                """

            except asyncio.CancelledError:
                logger.warning("Fetch loop cancelled. Exiting gracefully.")
                # Save counters one last time before exiting
                self.save_counters()
                break

            except Exception as e:
                logger.error("Error in TennisBot run loop", exc_info=True)
                # Still try to save counters even if there was an error
                self.save_counters()

            # Sleep until next fetch
            elapsed = time.time() - start_time
            wait_time = max(0, self.fetch_interval - elapsed)
            logger.info(f"Fetch cycle complete. Sleeping for {wait_time:.2f} seconds.")
            await asyncio.sleep(wait_time)

        logger.info("TennisBot run loop has exited.")

###############################################################################
# Main Entry Point
###############################################################################
async def main() -> None:
    """
    Sets up graceful shutdown handlers, then runs the TennisBot indefinitely.

    1) Instantiates the event loop.
    2) Adds signal handlers for SIGINT, SIGTERM that call shutdown_handler.
    3) Creates the TennisBot instance with default or environment-based config.
    4) Awaits the run() method in an infinite loop, unless cancelled.

    This function is called in the __main__ block below with asyncio.run().
    """
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: shutdown_handler(loop))

    # Create a TennisBot with optional overrides (if desired)
    bot = TennisBot()
    await bot.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.info("KeyboardInterrupt or SystemExit received. Shutting down.")
