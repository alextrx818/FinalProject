import asyncio
import logging
from rapid_tennis_fetcher import RapidInplayOddsFetcher

# Configure logging to show everything
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

async def main():
    print("\nStarting RapidAPI Tennis Fetcher Test...")
    
    # Initialize the fetcher
    fetcher = RapidInplayOddsFetcher()
    
    # Fetch tennis data
    print("\nFetching tennis matches...")
    matches = await fetcher.get_tennis_data()
    
    # Print results
    print(f"\nFound {len(matches)} tennis matches")
    
    if matches:
        # Show first match as example
        print("\nExample of first match data:")
        match = matches[0]
        
        print("\nEVENT DATA:")
        print("-" * 50)
        event_data = match['raw_event_data']
        print(f"Event ID: {event_data.get('marketFI')}")
        print(f"Event Name: {event_data.get('eventName')}")
        print(f"Team 1: {event_data.get('team1')}")
        print(f"Team 2: {event_data.get('team2')}")
        print(f"Score: {event_data.get('score')} (Sets: {event_data.get('sets')})")
        print(f"Current Game: {event_data.get('game')}")
        print(f"Liga: {event_data.get('liga')}")
        
        print("\nODDS DATA:")
        print("-" * 50)
        odds_data = match['raw_odds_data']
        
        # Print markets
        markets = odds_data.get('markets', [])
        print(f"Number of markets: {len(markets)}")
        
        # Show first market as example
        if markets:
            market = markets[0]  # Get first market
            print(f"\nExample Market Data:")
            print(f"Market Name: {market.get('name')}")
            print(f"Market ID: {market.get('id')}")
            print("Odds:")
            for odd in market.get('odds', []):
                print(f"  {odd.get('name')}: {odd.get('odds')}")
        
        # Print stats if available
        stats = odds_data.get('stats', {})
        if stats:
            print("\nSTATS:")
            print("-" * 50)
            print(stats)

if __name__ == "__main__":
    # Run the test
    asyncio.run(main())
