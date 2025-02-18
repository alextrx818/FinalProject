import asyncio
import json

# Imports for your fetchers and merger
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

async def main():
    # 1. Fetch real data from BetsAPI and RapidAPI
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()

    print(f"Fetched {len(bets_data)} records from BetsAPI.")
    print(f"Fetched {len(rapid_data)} records from RapidAPI.")

    # 2. Merge data (no fields filtered by default)
    merger = TennisMerger()
    merged_data = merger.merge(bets_data, rapid_data)
    print(f"Merged data contains {len(merged_data)} records.")

    # 3. Dump the merged data to a file (e.g. 'merged_data.json')
    with open("merged_data.json", "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=2)

    print("Merged data has been written to 'merged_data.json' with no filtering.")

if __name__ == "__main__":
    asyncio.run(main())
