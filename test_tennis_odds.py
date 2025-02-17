"""
Test script for tennis odds fetching from both RapidAPI and BetsAPI.
"""

import asyncio
import logging
from aggregator.sports.tennis.tennis_odds import TennisOdds
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch

logging.basicConfig(level=logging.INFO)

async def test_rapid_fetcher():
    """Test RapidAPI tennis fetcher"""
    print("\n=== Testing RapidAPI Tennis Fetcher ===")
    fetcher = RapidInplayOddsFetcher()
    data = await fetcher.get_tennis_data()
    print(f"Found {len(data)} in-play tennis matches")
    
    if data:
        # Show sample match
        match = data[0]
        print("\nSample In-play Match:")
        print(f"Event ID: {match.get('event_id')}")
        print(f"Players: {match.get('home_player')} vs {match.get('away_player')}")
        print(f"Score: {match.get('score', {}).get('current')}")
        print("Available markets:", list(match.get('odds', {}).keys()))

async def test_betsapi_fetcher():
    """Test BetsAPI tennis fetcher"""
    print("\n=== Testing BetsAPI Tennis Fetcher ===")
    fetcher = BetsapiPrematch()
    data = await fetcher.get_tennis_data()
    print(f"Found {len(data)} prematch tennis events")
    
    if data:
        # Show sample match
        match = data[0]
        info = match['event_info']
        print("\nSample Prematch Event:")
        print(f"Event ID: {info.get('bet365_id')}")
        print(f"Players: {info.get('home')} vs {info.get('away')}")
        print("Available markets:", list(match.get('prematch_data', {}).keys()))

async def test_tennis_odds():
    """Test combined tennis odds"""
    print("\n=== Testing Combined Tennis Odds ===")
    odds = TennisOdds()
    data = await odds.get_consolidated_odds()
    print(f"Found {len(data)} total tennis matches")
    
    if data:
        # Show sample match
        match = data[0]
        print("\nSample Combined Match:")
        print(f"Players: {match.get('home_player')} vs {match.get('away_player')}")
        if 'inplay_data' in match:
            print("Has in-play data:", bool(match['inplay_data']))
            print("In-play markets:", list(match.get('inplay_data', {}).get('odds', {}).keys()))
        if 'prematch_data' in match:
            print("Has prematch data:", bool(match['prematch_data']))
            print("Prematch markets:", list(match.get('prematch_data', {}).keys()))

async def main():
    """Run all tests"""
    try:
        await test_rapid_fetcher()
        await test_betsapi_fetcher()
        await test_tennis_odds()
    except Exception as e:
        print(f"Error in tests: {e}")

if __name__ == "__main__":
    asyncio.run(main())
