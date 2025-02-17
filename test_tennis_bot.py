import json
from aggregator.sports.tennis.tennis_odds_bot import TennisOddsBot

def print_match_summary(match: dict):
    print(f"\nMatch: {match['home_player']} vs {match['away_player']}")
    print(f"League: {match['league']}")
    print(f"Score: {match['score']}")
    print(f"Event ID: {match['event_id']}")
    print(f"Bet365 ID: {match['bet365_id']}")
    
    # Print in-play odds
    if match['inplay_data']['odds']:
        print("\nIn-play Odds:")
        for market, odds in match['inplay_data']['odds'].items():
            print(f"  {market}:")
            for selection in odds:
                print(f"    {selection['name']}: {selection['odds']}")
    
    # Print prematch odds if available
    if match.get('prematch_data', {}).get('results'):
        print("\nPrematch Markets:")
        markets = match['prematch_data']['results'][0].get('main', {}).get('sp', {})
        for market_name, market_data in markets.items():
            print(f"  {market_name}:")
            for odd in market_data.get('odds', []):
                header = odd.get('header', '')
                name = odd.get('name', '')
                odds = odd.get('odds', '')
                if header and name:
                    print(f"    {header} {name}: {odds}")
                else:
                    print(f"    {name}: {odds}")

def main():
    print("Initializing TennisOddsBot...\n")
    bot = TennisOddsBot()

    print("Fetching consolidated tennis odds...\n")
    matches = bot.get_consolidated_odds()

    print(f"Found {len(matches)} tennis matches with odds data.\n")
    
    # Print summary of each match
    for match in matches:
        print_match_summary(match)

if __name__ == "__main__":
    main()
