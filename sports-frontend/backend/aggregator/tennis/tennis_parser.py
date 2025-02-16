import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TennisParser:
    def parse_rapid_inplay(self, raw_inplay):
        """Parse RapidAPI inplay data"""
        if not raw_inplay or 'results' not in raw_inplay:
            return []

        parsed_matches = []
        for match in raw_inplay['results']:
            try:
                parsed_match = {
                    'source': 'rapid_inplay',
                    'players': {
                        'home': match.get('home', {}).get('name'),
                        'away': match.get('away', {}).get('name')
                    },
                    'match_key': self._generate_match_key(
                        match.get('home', {}).get('name'),
                        match.get('away', {}).get('name')
                    ),
                    'details': {
                        'league': match.get('league', {}).get('name'),
                        'status': match.get('status'),
                        'score': match.get('score'),
                        'current_set': match.get('set'),
                        'current_game': match.get('game')
                    },
                    'timestamp': datetime.now().isoformat()
                }
                parsed_matches.append(parsed_match)
                logger.info(f"Parsed RapidAPI inplay match: {parsed_match['match_key']}")
            except Exception as e:
                logger.error(f"Error parsing RapidAPI inplay match: {str(e)}")
                continue

        return parsed_matches

    def parse_bets_inplay(self, raw_inplay):
        """Parse BetsAPI inplay data"""
        if not raw_inplay or 'results' not in raw_inplay:
            return []

        parsed_matches = []
        for match in raw_inplay['results']:
            try:
                # BetsAPI has different field names
                parsed_match = {
                    'source': 'bets_inplay',
                    'players': {
                        'home': match.get('home', {}).get('name'),
                        'away': match.get('away', {}).get('name')
                    },
                    'match_key': self._generate_match_key(
                        match.get('home', {}).get('name'),
                        match.get('away', {}).get('name')
                    ),
                    'details': {
                        'league': match.get('league', {}).get('name'),
                        'status': match.get('timer'),
                        'score': match.get('ss'),  # BetsAPI score format
                        'current_set': match.get('current_set'),
                        'current_game': match.get('current_game')
                    },
                    'timestamp': datetime.now().isoformat()
                }
                parsed_matches.append(parsed_match)
                logger.info(f"Parsed BetsAPI inplay match: {parsed_match['match_key']}")
            except Exception as e:
                logger.error(f"Error parsing BetsAPI inplay match: {str(e)}")
                continue

        return parsed_matches

    def parse_rapid_odds(self, raw_odds):
        """Parse RapidAPI odds data"""
        if not raw_odds or 'results' not in raw_odds:
            return []

        parsed_odds = []
        for market in raw_odds['results'].get('markets', []):
            try:
                parsed_match = {
                    'source': 'rapid_odds',
                    'market_name': market.get('name'),
                    'odds': [
                        {
                            'name': sel.get('name'),
                            'odds': sel.get('odds'),
                            'status': sel.get('status')
                        }
                        for sel in market.get('selections', [])
                    ],
                    'timestamp': datetime.now().isoformat()
                }
                parsed_odds.append(parsed_match)
            except Exception as e:
                logger.error(f"Error parsing RapidAPI odds: {str(e)}")
                continue

        return parsed_odds

    def parse_bets_odds(self, raw_odds):
        """Parse BetsAPI odds data"""
        if not raw_odds or 'results' not in raw_odds:
            return []

        parsed_odds = []
        for market in raw_odds['results'].get('odds', {}).values():
            try:
                parsed_match = {
                    'source': 'bets_odds',
                    'market_name': market.get('name'),
                    'odds': [
                        {
                            'name': odd.get('name'),
                            'odds': odd.get('odds'),
                            'status': odd.get('status')
                        }
                        for odd in market.get('odds', [])
                    ],
                    'timestamp': datetime.now().isoformat()
                }
                parsed_odds.append(parsed_match)
            except Exception as e:
                logger.error(f"Error parsing BetsAPI odds: {str(e)}")
                continue

        return parsed_odds

    def _generate_match_key(self, home, away):
        """Generate consistent match key from player names"""
        if not home or not away:
            return None
        # Sort names to ensure "Nadal-Federer" and "Federer-Nadal" create same key
        return '-'.join(sorted([home.lower(), away.lower()]))

if __name__ == "__main__":
    # Test the parser
    parser = TennisParser()
    
    # Example raw data
    test_inplay = {
        'results': [{
            'home': {'name': 'Nadal'},
            'away': {'name': 'Federer'},
            'league': {'name': 'ATP'},
            'status': 'In-Play',
            'score': '6-4, 2-1'
        }]
    }
    
    test_odds = {
        'results': {
            'odds': {
                'Match Winner': {
                    'name': 'Match Winner',
                    'odds': [
                        {'name': 'Nadal', 'odds': 1.85},
                        {'name': 'Federer', 'odds': 2.10}
                    ]
                }
            }
        }
    }
    
    # Test parsing
    inplay_matches = parser.parse_bets_inplay(test_inplay)
    odds_matches = parser.parse_bets_odds(test_odds)
    
    print("\nParsed data has matching keys:")
    print(f"Inplay key: {inplay_matches[0]['match_key']}")
    print(f"Odds key: {odds_matches[0]['market_name']}")
