import asyncio
import json
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.tennis_merger import TennisMerger

async def save_sample_data():
    # Initialize fetchers and merger
    bets_fetcher = BetsapiPrematch()
    rapid_fetcher = RapidInplayOddsFetcher()
    merger = TennisMerger()
    
    print("Fetching data from both APIs...")
    bets_data = await bets_fetcher.get_tennis_data()
    rapid_data = await rapid_fetcher.get_tennis_data()
    
    # Merge the data
    merged_data = merger.merge(bets_data, rapid_data)
    
    if merged_data and len(merged_data) >= 2:
        # Save first two merged matches to file with complete data
        matches = {
            'match1': merged_data[0],
            'match2': merged_data[1]
        }
        
        with open('merged_matches_data.json', 'w') as f:
            json.dump(matches, f, indent=2, ensure_ascii=False)
        
        print("\nMerged match data has been saved to 'merged_matches_data.json'")
        print(f"\nTotal matches found:")
        print(f"- BetsAPI: {len(bets_data)} events")
        print(f"- RapidAPI: {len(rapid_data)} events")
        print(f"- Successfully merged: {len(merged_data)} events")
        
        # Print basic info about the two matches
        print("\nMatch 1:")
        print(f"- {merged_data[0]['home_player']} vs {merged_data[0]['away_player']}")
        print(f"- Score: {merged_data[0]['betsapi_data']['inplay_event']['ss']}")
        
        print("\nMatch 2:")
        print(f"- {merged_data[1]['home_player']} vs {merged_data[1]['away_player']}")
        print(f"- Score: {merged_data[1]['betsapi_data']['inplay_event']['ss']}")
    else:
        print("\nNot enough matches were successfully merged!")

if __name__ == "__main__":
    asyncio.run(save_sample_data())
