import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TennisMerger:
    def merge_matches(self, rapid_inplay, bets_inplay, rapid_odds, bets_odds):
        """Merge data from both RapidAPI and BetsAPI using player names"""
        merged_matches = []
        
        # Create lookup dictionaries for odds data
        rapid_odds_lookup = {
            market['market_name']: market 
            for market in rapid_odds 
            if market.get('market_name')
        }
        
        bets_odds_lookup = {
            market['market_name']: market 
            for market in bets_odds 
            if market.get('market_name')
        }

        # Start with RapidAPI inplay matches
        for rapid_match in rapid_inplay:
            match_key = rapid_match.get('match_key')
            if not match_key:
                continue

            # Find matching BetsAPI match
            bets_match = next(
                (m for m in bets_inplay if m.get('match_key') == match_key),
                None
            )

            # Get odds from both sources
            rapid_match_odds = rapid_odds_lookup.get('Match Winner', {})
            bets_match_odds = bets_odds_lookup.get('Match Winner', {})

            merged_match = {
                'players': rapid_match['players'],  # Use RapidAPI player names
                'match_details': {
                    # Combine match details from both sources
                    **rapid_match['details'],
                    'bets_status': bets_match['details']['status'] if bets_match else None,
                    'bets_score': bets_match['details']['score'] if bets_match else None
                },
                'odds': {
                    'rapid_api': rapid_match_odds.get('odds', []),
                    'bets_api': bets_match_odds.get('odds', [])
                },
                'timestamps': {
                    'rapid_inplay': rapid_match.get('timestamp'),
                    'bets_inplay': bets_match.get('timestamp') if bets_match else None,
                    'rapid_odds': rapid_match_odds.get('timestamp'),
                    'bets_odds': bets_match_odds.get('timestamp')
                },
                'sources': {
                    'inplay': ['rapid_api'] + (['bets_api'] if bets_match else []),
                    'odds': [
                        s for s in ['rapid_api', 'bets_api'] 
                        if rapid_match_odds or bets_match_odds
                    ]
                }
            }
            merged_matches.append(merged_match)
            logger.info(f"Merged match data for: {match_key}")

        return merged_matches

if __name__ == "__main__":
    # Test the merger
    from tennis_parser import TennisParser
    
    parser = TennisParser()
    merger = TennisMerger()
    
    # Example raw data from both APIs
    rapid_inplay_data = {
        'results': [{
            'home': {'name': 'Nadal'},
            'away': {'name': 'Federer'},
            'league': {'name': 'ATP'},
            'status': 'In-Play',
            'score': '6-4, 2-1'
        }]
    }
    
    bets_inplay_data = {
        'results': [{
            'home': {'name': 'Nadal'},
            'away': {'name': 'Federer'},
            'league': {'name': 'ATP'},
            'timer': '45',
            'ss': '6-4, 2-1'
        }]
    }
    
    rapid_odds_data = {
        'results': {
            'markets': [{
                'name': 'Match Winner',
                'selections': [
                    {'name': 'Nadal', 'odds': 1.85},
                    {'name': 'Federer', 'odds': 2.10}
                ]
            }]
        }
    }
    
    bets_odds_data = {
        'results': {
            'odds': {
                'Match Winner': {
                    'name': 'Match Winner',
                    'odds': [
                        {'name': 'Nadal', 'odds': 1.90},
                        {'name': 'Federer', 'odds': 2.05}
                    ]
                }
            }
        }
    }
    
    # Parse data from both sources
    rapid_inplay = parser.parse_rapid_inplay(rapid_inplay_data)
    bets_inplay = parser.parse_bets_inplay(bets_inplay_data)
    rapid_odds = parser.parse_rapid_odds(rapid_odds_data)
    bets_odds = parser.parse_bets_odds(bets_odds_data)
    
    # Merge all data
    merged = merger.merge_matches(rapid_inplay, bets_inplay, rapid_odds, bets_odds)
    
    # Show merged data
    for match in merged:
        print("\nMerged Match Data:")
        print(f"Players: {match['players']['home']} vs {match['players']['away']}")
        print(f"RapidAPI Score: {match['match_details']['score']}")
        print(f"BetsAPI Score: {match['match_details']['bets_score']}")
        print("\nOdds Comparison:")
        print("RapidAPI:", match['odds']['rapid_api'])
        print("BetsAPI:", match['odds']['bets_api'])
        print(f"Data Sources: {match['sources']}")
