"""
Tennis-specific database operations for storing and retrieving tennis match data.
Extends the core DatabaseManager with tennis-focused functionality.
"""

import logging
from typing import Dict, List, Optional, Any
from ...database.db_utils import DatabaseManager

logger = logging.getLogger(__name__)

class TennisDatabase:
    """
    Tennis-specific database operations.
    Handles storage and retrieval of:
    - Live match data from RapidAPI
    - Prematch data from BetsAPI
    - Combined and processed tennis odds
    """

    def __init__(self):
        self.db = DatabaseManager()

    async def store_rapid_tennis_data(self, matches: List[Dict[str, Any]]) -> bool:
        """
        Store live tennis match data from RapidAPI.
        
        Args:
            matches: List of match data from RapidInplayOddsFetcher
                    Each match contains raw_event_data and raw_odds_data
        
        Returns:
            bool: True if storage was successful
        """
        try:
            formatted_matches = []
            for match in matches:
                event_data = match.get('raw_event_data', {})
                formatted_matches.append({
                    'match_id': event_data.get('marketFI', ''),
                    'event_name': event_data.get('eventName', ''),
                    'status': 'Live',
                    'odds': match.get('raw_odds_data', {})
                })
            
            if formatted_matches:
                self.db.store_tennis_data(formatted_matches)
                logger.info(f"Stored {len(formatted_matches)} RapidAPI tennis matches")
                return True
            return False
            
        except Exception as e:
            logger.error(f"Error storing RapidAPI tennis data: {e}")
            return False

    async def store_betsapi_tennis_data(self, matches: List[Dict[str, Any]]) -> bool:
        """
        Store tennis prematch data from BetsAPI.
        
        Args:
            matches: List of match data from BetsapiPrematch
                    Each match contains inplay_event, bet365_id, and raw_prematch_data
        
        Returns:
            bool: True if storage was successful
        """
        try:
            formatted_matches = []
            for match in matches:
                event = match.get('inplay_event', {})
                formatted_matches.append({
                    'match_id': match.get('bet365_id', ''),
                    'event_name': f"{event.get('home', {}).get('name', '')} vs {event.get('away', {}).get('name', '')}",
                    'status': 'Prematch',
                    'odds': match.get('raw_prematch_data', {})
                })
            
            if formatted_matches:
                self.db.store_tennis_data(formatted_matches)
                logger.info(f"Stored {len(formatted_matches)} BetsAPI tennis matches")
                return True
            return False
            
        except Exception as e:
            logger.error(f"Error storing BetsAPI tennis data: {e}")
            return False

    def get_live_matches(self) -> List[Dict[str, Any]]:
        """Get all live tennis matches from the database"""
        try:
            return self.db.get_live_tennis_matches()
        except Exception as e:
            logger.error(f"Error retrieving live tennis matches: {e}")
            return []

    def get_match_by_id(self, match_id: str) -> Optional[Dict[str, Any]]:
        """
        Get a specific tennis match by its ID.
        
        Args:
            match_id: The match ID (either RapidAPI marketFI or BetsAPI bet365_id)
        
        Returns:
            Optional[Dict]: Match data if found, None if not found
        """
        try:
            conn = self.db.get_connection()
            cur = conn.cursor()
            
            cur.execute("""
                SELECT * FROM tennis_odds 
                WHERE match_id = %s
                ORDER BY timestamp DESC 
                LIMIT 1
            """, (match_id,))
            
            result = cur.fetchone()
            return dict(result) if result else None
            
        except Exception as e:
            logger.error(f"Error retrieving tennis match {match_id}: {e}")
            return None
        finally:
            if 'cur' in locals():
                cur.close()
            if 'conn' in locals():
                conn.close()

# Quick test of the database operations
if __name__ == "__main__":
    import asyncio
    from rapid_tennis_fetcher import RapidInplayOddsFetcher
    from betsapi_prematch import BetsapiPrematch
    
    async def test_db():
        db = TennisDatabase()
        
        # Test RapidAPI storage
        rapid_fetcher = RapidInplayOddsFetcher()
        rapid_matches = await rapid_fetcher.get_tennis_data()
        if rapid_matches:
            success = await db.store_rapid_tennis_data(rapid_matches)
            print(f"Stored RapidAPI matches: {success}")
        
        # Test BetsAPI storage
        bets_fetcher = BetsapiPrematch()
        bets_matches = await bets_fetcher.get_tennis_data()
        if bets_matches:
            success = await db.store_betsapi_tennis_data(bets_matches)
            print(f"Stored BetsAPI matches: {success}")
        
        # Test retrieval
        live_matches = db.get_live_matches()
        print(f"Retrieved {len(live_matches)} live matches")
        
        if live_matches:
            # Test get by ID
            match_id = live_matches[0]['match_id']
            match = db.get_match_by_id(match_id)
            print(f"Retrieved match by ID {match_id}: {bool(match)}")
    
    asyncio.run(test_db())
