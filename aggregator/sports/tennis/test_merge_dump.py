import asyncio
import json
import logging
from datetime import datetime
import pytz

from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

logging.basicConfig(level=logging.INFO)

async def main():
    """
    1) Fetch data from BetsAPI (prematch) + RapidAPI (live).
    2) Merge them via TennisMerger.
    3) Write the final merged JSON to 'mergedDump.json'.
    """
    # 1. Create the same fetchers your main bot uses:
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()

    # 2. Fetch data from each API:
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    logging.info(f"Fetched {len(bets_data)} from BetsAPI and {len(rapid_data)} from RapidAPI.")

    # 3. Merge using your aggregator (TennisMerger):
    merger = TennisMerger()
    merged_data = merger.merge(bets_data, rapid_data)
    logging.info(f"Merged data size: {len(merged_data)}")

    # Get current EST time
    eastern = pytz.timezone('US/Eastern')
    utc_now = datetime.now(pytz.UTC)
    est_now = utc_now.astimezone(eastern)
    timestamp = est_now.strftime("%Y-%m-%d %H:%M:%S %Z")

    # 4. Write the final JSON to 'mergedDump.json' with timestamp
    output_data = {
        "timestamp": timestamp,
        "data": merged_data
    }
    
    with open('mergedDump.json', 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2)

    logging.info(f"Wrote merged data to mergedDump.json at {timestamp}")

if __name__ == "__main__":
    asyncio.run(main())
