#!/usr/bin/env python3

import json
import logging
from datetime import datetime
import pytz

from aggregator.sports.tennis.tennis_merger import TennisMerger
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_current_est_time():
    """Get current time in EST timezone."""
    est = pytz.timezone('US/Eastern')
    return datetime.now(est).strftime('%Y-%m-%d %H:%M:%S EST')

async def dump_data():
    """
    Fetch, merge, and dump tennis data to both console and file.
    """
    # Initialize our components
    bets_client = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    merger = TennisMerger()

    # Get data from both sources
    bets_data = await bets_client.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()

    # Merge the data
    merged_data = merger.merge(bets_data, rapid_data)

    # Create output with timestamp
    output = {
        "timestamp": get_current_est_time(),
        "data": merged_data
    }

    # 1. Print raw single-line JSON
    logger.info("--- RAW SINGLE-LINE JSON ---")
    logger.info(json.dumps(output))

    # 2. Print pretty JSON
    logger.info("\n--- PRETTY JSON ---")
    logger.info(json.dumps(output, indent=2))

    # 3. Write to file (pretty)
    with open('mergedDump.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2)
    
    logger.info(f"\nWrote merged data to mergedDump.json at {get_current_est_time()}")
    logger.info(f"Merged data size: {len(merged_data)}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(dump_data())
