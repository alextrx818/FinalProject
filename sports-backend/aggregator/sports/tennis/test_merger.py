import asyncio
import logging

# Import your existing classes
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

# -------------------------------------------------------------------------
# Configure Logging
# -------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# -------------------------------------------------------------------------
# Main Async Test Function
# -------------------------------------------------------------------------
async def main():
    """
    1) Fetch live in-play + prematch data from BetsAPI.
    2) Fetch live in-play + odds data from RapidAPI.
    3) Transform BetsAPI results into a format TennisMerger expects.
    4) Merge the two sets with TennisMerger.
    5) Print the results for inspection (logging).
    """

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

    # 3) Transform BetsAPI data into the structure TennisMerger expects
    #    The TennisMerger wants a list of dicts like:
    #    [
    #      {
    #        "players": {
    #          "home": "Some Name",
    #          "away": "Another Name"
    #        },
    #        "bet365_id": "123456789",
    #        ...
    #      },
    #      ...
    #    ]

    bets_data_for_merger = []
    for item in bets_raw:
        inplay_event = item.get("inplay_event", {})
        bet365_id = item.get("bet365_id", "")
        prematch_data = item.get("raw_prematch_data", {})

        # For example, in "inplay_event":
        #   "home": {"name": "Novak Djokovic"},
        #   "away": {"name": "Matteo Berrettini"},
        home_player = inplay_event.get("home", {}).get("name", "")
        away_player = inplay_event.get("away", {}).get("name", "")

        bets_data_for_merger.append({
            "players": {
                "home": home_player,
                "away": away_player
            },
            "bet365_id": bet365_id,
            # Keep the raw data if you want to see more details
            "inplay_event": inplay_event,
            "raw_prematch_data": prematch_data
        })

    # 4) Rapid data is already in a shape the updated TennisMerger understands:
    #    [
    #      {
    #        "raw_event_data": {...}, # "team1","team2","eventId", or "FI", or "bet365_id"
    #        "raw_odds_data": {...}
    #      },
    #      ...
    #    ]
    rapid_data_for_merger = rapid_raw

    # 5) Merge
    merger = TennisMerger()
    merged_data = merger.merge(bets_data_for_merger, rapid_data_for_merger)

    logger.info(f"\n=== Merged {len(merged_data)} Records ===")
    logger.info("Review the logs above for detailed match info (ID vs fuzzy).")

    # If you want to see each record explicitly:
    for i, record in enumerate(merged_data, start=1):
        logger.info(f"\n--- Merged Record #{i} ---")
        logger.info(f"Home Player: {record.get('home_player')}")
        logger.info(f"Away Player: {record.get('away_player')}")
        if record.get("betsapi_data"):
            logger.info("BetsAPI Data: present")
        else:
            logger.info("BetsAPI Data: None")

        if record.get("rapid_data"):
            logger.info("Rapid Data: present")
        else:
            logger.info("Rapid Data: None")

    # Fuzzy fallback usage
    logger.info(f"\nFuzzy fallback count: {merger.fuzzy_fallback_count}")

    # Count successful matches (where both APIs had data)
    successful_matches = sum(1 for record in merged_data if record.get("betsapi_data") and record.get("rapid_data"))
    logger.info(f"Successfully matched events: {successful_matches}")
    
    # Count unmatched records
    unmatched_bets = sum(1 for record in merged_data if record.get("betsapi_data") and not record.get("rapid_data"))
    unmatched_rapid = sum(1 for record in merged_data if record.get("rapid_data") and not record.get("betsapi_data"))
    logger.info(f"Unmatched events:")
    logger.info(f"  - BetsAPI only: {unmatched_bets}")
    logger.info(f"  - RapidAPI only: {unmatched_rapid}")

    if merger.fuzzy_fallback_count > 10:
        logger.warning("A large number of merges had to fall back on fuzzy matching.")

    logger.info("=== Done testing with live data. ===\n")

# -------------------------------------------------------------------------
# Entry Point
# -------------------------------------------------------------------------
if __name__ == "__main__":
    asyncio.run(main())
