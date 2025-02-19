import json
import os
import asyncio
import logging
from datetime import datetime
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

# Directory to store raw merger dumps
RAW_DUMP_DIR = "raw_merger_dumps"

# Configure Logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    logger.info("=== Starting Live Tennis Merger Test ===")

    # 1) Instantiate your BetsAPI and RapidAPI fetchers
    bets_fetcher = BetsapiPrematch(concurrency_limit=5, max_retries=3)
    rapid_fetcher = RapidInplayOddsFetcher()

    # 2) Fetch data
    logger.info("Fetching data from BetsAPI...")
    bets_raw = await bets_fetcher.get_tennis_data()
    logger.info(f"BetsAPI returned {len(bets_raw)} records.\n")

    logger.info("Fetching data from RapidAPI...")
    rapid_raw = await rapid_fetcher.get_tennis_data()
    logger.info(f"RapidAPI returned {len(rapid_raw)} records.\n")

    # 3) Transform BetsAPI data
    bets_data_for_merger = []
    for item in bets_raw:
        inplay_event = item.get("inplay_event", {})
        bet365_id = item.get("bet365_id", "")
        prematch_data = item.get("raw_prematch_data", {})

        home_player = inplay_event.get("home", {}).get("name", "")
        away_player = inplay_event.get("away", {}).get("name", "")

        bets_data_for_merger.append({
            "players": {
                "home": home_player,
                "away": away_player
            },
            "bet365_id": bet365_id,
            "inplay_event": inplay_event,
            "raw_prematch_data": prematch_data
        })

    # 4) Use Rapid data as is
    rapid_data_for_merger = rapid_raw

    # 5) Merge
    merger = TennisMerger()
    merged_data = merger.merge(bets_data_for_merger, rapid_data_for_merger)

    # 6) Save raw merged data
    os.makedirs(RAW_DUMP_DIR, exist_ok=True)
    filename = f"{RAW_DUMP_DIR}/merged_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(merged_data, f, indent=4)

    logger.info(f"\n=== Raw merged data saved to {filename} ===")

    # 7) Print statistics
    logger.info(f"\n=== Merged {len(merged_data)} Records ===")
    logger.info("Review the logs above for detailed match info (ID vs fuzzy).")

    for i, record in enumerate(merged_data, start=1):
        logger.info(f"\n--- Merged Record #{i} ---")
        logger.info(f"Home Player: {record.get('home_player')}")
        logger.info(f"Away Player: {record.get('away_player')}")
        logger.info(f"BetsAPI Data: {'present' if record.get('betsapi_data') else 'None'}")
        logger.info(f"Rapid Data: {'present' if record.get('rapid_data') else 'None'}")

    # Print summary statistics
    successful_matches = sum(1 for record in merged_data if record.get("betsapi_data") and record.get("rapid_data"))
    unmatched_bets = sum(1 for record in merged_data if record.get("betsapi_data") and not record.get("rapid_data"))
    unmatched_rapid = sum(1 for record in merged_data if record.get("rapid_data") and not record.get("betsapi_data"))

    logger.info(f"\nFuzzy fallback count: {merger.fuzzy_fallback_count}")
    logger.info(f"Successfully matched events: {successful_matches}")
    logger.info(f"Unmatched events:")
    logger.info(f"  - BetsAPI only: {unmatched_bets}")
    logger.info(f"  - RapidAPI only: {unmatched_rapid}")

    if merger.fuzzy_fallback_count > 10:
        logger.warning("A large number of merges had to fall back on fuzzy matching.")

    logger.info("=== Done testing with live data. ===\n")

if __name__ == "__main__":
    asyncio.run(main())
