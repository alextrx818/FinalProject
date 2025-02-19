import os
import asyncio
import json
import logging
from datetime import datetime
import pytz

# 1) Import the same fetchers your production code uses
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher

# 2) Import the merger
from aggregator.sports.tennis.tennis_merger import TennisMerger

###############################################################################
# Optional environment-based constants
###############################################################################
DEFAULT_CONCURRENCY = int(os.getenv("TENNIS_BOT_CONCURRENCY", "5"))
DEFAULT_MAX_RETRIES = int(os.getenv("TENNIS_BOT_MAX_RETRIES", "3"))

###############################################################################
# Logging Setup
###############################################################################
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    """
    1) Fetch BetsAPI (Prematch) + RapidAPI (Live) data
    2) Merge results via TennisMerger
    3) Write final JSON to mergedDump.json
    """

    logger.info("=== Starting Test Orchestrator ===")

    # 3) Create your fetchers with the same settings you use in your main bot
    betsapi_fetcher = BetsapiPrematch(
        concurrency_limit=DEFAULT_CONCURRENCY,
        max_retries=DEFAULT_MAX_RETRIES
    )
    rapid_fetcher = RapidInplayOddsFetcher()

    # 4) Fetch data from each source
    logger.info("Fetching BetsAPI (Prematch) data...")
    bets_data = await betsapi_fetcher.get_tennis_data()
    logger.info(f"Got {len(bets_data)} records from BetsAPI.")

    logger.info("Fetching RapidAPI (Live) data...")
    rapid_data = await rapid_fetcher.get_tennis_data()
    logger.info(f"Got {len(rapid_data)} records from RapidAPI.")

    # 5) Merge the two sources
    merger = TennisMerger()
    merged_data = merger.merge(bets_data, rapid_data)
    logger.info(f"Merged data size: {len(merged_data)}")

    # Create output with EST timestamp
    eastern = pytz.timezone('US/Eastern')
    utc_now = datetime.now(pytz.UTC)
    est_now = utc_now.astimezone(eastern)
    timestamp = est_now.strftime("%Y-%m-%d %H:%M:%S %Z")
    output_data = {
        "timestamp": timestamp,
        "data": merged_data
    }

    # 6) Write the merged JSON to a file
    with open("mergedDump.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

    logger.info("Wrote merged data to mergedDump.json. Done.")

if __name__ == "__main__":
    asyncio.run(main())
