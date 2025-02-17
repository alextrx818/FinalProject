from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher
import json

def main():
    print("Initializing RapidInplayOddsFetcher...\n")
    fetcher = RapidInplayOddsFetcher()
    
    print("Fetching tennis data (events + odds)...\n")
    tennis_data = fetcher.get_tennis_data()
    
    print("Raw Tennis Data (Pretty Printed):")
    print(json.dumps(tennis_data, indent=2))
    
    print(f"\nTotal events fetched: {len(tennis_data)}")
    
    # Print summary of each event
    for event in tennis_data:
        print(f"\nEvent: {event.get('eventName')}")
        print(f"Teams: {event.get('team1')} vs {event.get('team2')}")
        print(f"League: {event.get('liga')}")
        print(f"Markets Count: {event.get('marketsCount')}")
        
        odds_data = event.get('odds_data', {})
        if odds_data:
            print(f"Odds Data Keys: {list(odds_data.keys())}")
        else:
            print("No odds data available")

if __name__ == "__main__":
    main()
