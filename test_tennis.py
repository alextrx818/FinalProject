import json
from aggregator.sports.tennis.rapid_tennis_fetcher import RapidInplayOddsFetcher

def test_fetch_tennis_data():
    """
    Tests the RapidInplayOddsFetcher class for fetching tennis events and odds.
    """
    print("Initializing RapidInplayOddsFetcher...")
    fetcher = RapidInplayOddsFetcher()
    
    print("Fetching all live tennis matches (plus odds)...\n")
    data = fetcher.get_tennis_data()

    # Show how many matches were found
    print(f"Number of Live Tennis Matches: {len(data)}")
    print("=" * 50)

    # Print the entire data structure in JSON format (for all matches)
    # WARNING: This can be very large if there are many live matches
    print("Full Combined Data (Events + Odds):")
    print(json.dumps(data, indent=2))

    # If you also want a more selective or summarized printout,
    # you can do that below. For example, let's print a summary
    # for the first 10 matches with all their odds.
    print("\nSummary of First 10 Matches (Detailed Odds):")
    for i, match in enumerate(data[:10]):  # limit to the first 10
        print("=" * 50)
        print(f"Match #{i+1}")
        print(f"Event ID: {match.get('event_id')}")
        print(f"Event Name: {match.get('eventName')}")
        print(f"League: {match.get('liga')}")
        print(f"Score (Game): {match.get('game')}")

        # Now print *all* odds data for this match
        odds_data = match.get('odds_data', {})
        print("\nOdds Data (full):")
        print(json.dumps(odds_data, indent=2))

if __name__ == "__main__":
    test_fetch_tennis_data()
