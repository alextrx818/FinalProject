import json
from aggregator.sports.tennis.betsapi_prematch import BetsapiPrematch

def print_market_odds(market_name: str, market_data: dict):
    print(f"\n    {market_name}:")
    odds = market_data.get("odds", [])
    for odd in odds:
        header = odd.get("header", "")
        name = odd.get("name", "")
        odds_value = odd.get("odds", "")
        if header and name:
            print(f"      {header} {name}: {odds_value}")
        else:
            print(f"      {name}: {odds_value}")

def main():
    print("Initializing BetsapiPrematch...\n")
    fetcher = BetsapiPrematch()

    print("Fetching tennis data (in-play events + prematch data)...\n")
    data = fetcher.get_tennis_data()

    # Take the first match with available markets
    for item in data:
        event_info = item["event_info"]
        prematch = item["prematch_data"]
        
        if prematch.get("results"):
            print(f"Detailed markets for: {event_info['home']} vs {event_info['away']}")
            print(f"League: {event_info['league']}")
            print(f"Current Score: {event_info['score']}")
            print("\nAvailable Markets:")
            
            markets = prematch["results"][0].get("main", {}).get("sp", {})
            for market_name, market_data in markets.items():
                print_market_odds(market_name, market_data)
            
            # Only show first match with markets
            break

if __name__ == "__main__":
    main()
