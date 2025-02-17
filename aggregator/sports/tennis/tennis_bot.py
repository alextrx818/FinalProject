import os
import asyncio
import logging
import signal
import time
from typing import Optional

# Local imports (using relative imports)
from .betsapi_prematch import BetsapiPrematch
from .rapid_tennis_fetcher import RapidInplayOddsFetcher
from . import tennis_merger
from . import tennis_parser
from . import tennis_database

###############################################################################
# Configuration via Environment Variables or defaults
###############################################################################
# For concurrency in each fetcher
DEFAULT_CONCURRENCY = int(os.getenv("TENNIS_BOT_CONCURRENCY", "5"))
DEFAULT_MAX_RETRIES = int(os.getenv("TENNIS_BOT_MAX_RETRIES", "3"))
# For how often we fetch data (in seconds)
DEFAULT_FETCH_INTERVAL = float(os.getenv("TENNIS_BOT_FETCH_INTERVAL", "60"))

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

# Avoid adding handlers multiple times if the module is re-imported
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

###############################################################################
# Graceful Shutdown Setup
###############################################################################
def shutdown_handler(loop: asyncio.AbstractEventLoop) -> None:
    """
    Signal handler to gracefully shut down the bot.
    Cancels all running tasks so they can clean up.
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
      1) BetsAPI Prematch
      2) Rapid Tennis Fetcher (for in-play odds)
    Then merges, parses, and stores the data.
    Repeats every fetch_interval seconds.
    """

    def __init__(
        self,
        fetch_interval: Optional[float] = None,
        concurrency_limit: Optional[int] = None,
        max_retries: Optional[int] = None
    ) -> None:
        """
        :param fetch_interval: Interval in seconds between fetch cycles.
        :param concurrency_limit: Max number of concurrent requests per fetcher.
        :param max_retries: Max retries for transient errors in fetchers.
        """
        # If not provided, fall back to environment variables or defaults
        self.fetch_interval = fetch_interval or DEFAULT_FETCH_INTERVAL

        # Initialize your two fetchers with concurrency + retry logic
        self.betsapi_fetcher = BetsapiPrematch(
            concurrency_limit=concurrency_limit or DEFAULT_CONCURRENCY,
            max_retries=max_retries or DEFAULT_MAX_RETRIES
        )
        self.rapid_fetcher = RapidInplayOddsFetcher()  # No extra params needed

    async def run(self) -> None:
        """
        Main loop: run forever, fetching from both APIs every self.fetch_interval seconds,
        unless a shutdown signal is received.
        """
        logger.info("TennisBot started. Press Ctrl+C to stop.")

        while True:
            start_time = time.time()
            logger.info("Starting fetch cycle...")

            try:
                # 1) Fetch data from BetsAPI
                logger.info("[BetsAPI] Beginning fetch...")
                bets_data = await self.betsapi_fetcher.get_tennis_data()
                logger.info(f"[BetsAPI] Fetch returned {len(bets_data)} records.")

                # 2) Fetch data from Rapid Tennis
                logger.info("[RapidAPI] Beginning fetch...")
                rapid_data = await self.rapid_fetcher.get_tennis_data()
                logger.info(f"[RapidAPI] Fetch returned {len(rapid_data)} records.")

                # 3) Merge the two sets of data
                logger.info("Merging data...")
                merged_data = []  # TODO: Implement tennis_merger
                logger.info(f"Merged data size: {len(merged_data)}")

                # 4) Parse the merged data
                logger.info("Parsing merged data...")
                parsed_data = []  # TODO: Implement tennis_parser
                logger.info(f"Parsed data size: {len(parsed_data)}")

                # 5) Save to the tennis database
                logger.info("Saving parsed data to database...")
                # TODO: Implement tennis_database
                logger.info("Data successfully saved to the database.")

            except asyncio.CancelledError:
                # This happens if we received a shutdown signal
                logger.warning("Fetch loop cancelled. Exiting gracefully.")
                break  # Exit the while loop

            except Exception as e:
                # Improved error context
                logger.error("Error in TennisBot run loop", exc_info=True)

            # Sleep until next fetch, minus time already spent
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
    """
    loop = asyncio.get_event_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(sig, lambda: shutdown_handler(loop))

    # Create a TennisBot with optional overrides from environment variables
    bot = TennisBot(
        fetch_interval=DEFAULT_FETCH_INTERVAL,
        concurrency_limit=DEFAULT_CONCURRENCY,
        max_retries=DEFAULT_MAX_RETRIES
    )

    await bot.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # Catch direct interrupts if they happen before the signal handler
        logger.info("KeyboardInterrupt or SystemExit received. Shutting down.")
