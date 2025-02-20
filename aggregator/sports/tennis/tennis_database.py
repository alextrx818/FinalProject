"""
Tennis-specific database operations for storing and retrieving tennis match data.
"""

import json
import logging
import psycopg2
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)

# Tennis Database Configuration
TENNIS_DB_CONFIG = {
    'dbname': 'tennis_db',
    'user': 'postgres',
    'password': '',  # Using peer authentication
    'host': 'localhost'
}

# SQL for creating tennis_matches table
CREATE_TENNIS_MATCHES_TABLE = """
CREATE TABLE IF NOT EXISTS tennis_matches (
    match_id    VARCHAR(50) PRIMARY KEY,
    raw_data    JSONB NOT NULL,
    inserted_at TIMESTAMP DEFAULT NOW()
);
"""

# Index for faster JSON queries
CREATE_TENNIS_MATCHES_INDEX = """
CREATE INDEX IF NOT EXISTS idx_tennis_matches_raw_data 
ON tennis_matches USING gin (raw_data);
"""

class TennisDatabase:
    """
    Tennis-specific database operations.
    Handles storage and retrieval of tennis match data.
    """

    def __init__(self):
        """Initialize tennis database"""
        try:
            self.conn = psycopg2.connect(**TENNIS_DB_CONFIG)
            self.conn.autocommit = True
            self._init_tables()
            logger.info("Successfully connected to tennis database")
        except Exception as e:
            logger.error(f"Failed to connect to tennis database: {e}")
            raise

    def __del__(self):
        """Cleanup database connection"""
        if hasattr(self, 'conn'):
            self.conn.close()
    
    def _init_tables(self):
        """Initialize required tables and indexes"""
        with self.conn.cursor() as cur:
            cur.execute(CREATE_TENNIS_MATCHES_TABLE)
            cur.execute(CREATE_TENNIS_MATCHES_INDEX)
            logger.info("Tennis database tables initialized")

    async def store_match_data(self, match_id: str, raw_data: Dict[str, Any]) -> bool:
        """
        Store tennis match data in the tennis_matches table.
        
        Args:
            match_id: Unique identifier for the match
            raw_data: Raw match data to store as JSONB
        
        Returns:
            bool: True if storage was successful
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO tennis_matches (match_id, raw_data)
                    VALUES (%s, %s)
                    ON CONFLICT (match_id) DO UPDATE 
                    SET raw_data = EXCLUDED.raw_data,
                        inserted_at = NOW()
                    """,
                    (match_id, json.dumps(raw_data))
                )
                return True
        except Exception as e:
            logger.error(f"Failed to store match data: {e}")
            return False

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
            success = True
            for match in matches:
                event_data = match.get('raw_event_data', {})
                match_id = event_data.get('marketFI', '')
                if not match_id:
                    logger.warning("Skipping match with no marketFI")
                    continue
                
                # Store complete raw data
                raw_data = {
                    'event_data': event_data,
                    'odds_data': match.get('raw_odds_data', {}),
                    'status': 'Live',
                    'source': 'RapidAPI',
                    'stored_at': datetime.utcnow().isoformat()
                }
                
                if not await self.store_match_data(match_id, raw_data):
                    success = False
            
            return success
        except Exception as e:
            logger.error(f"Error storing RapidAPI tennis data: {e}")
            return False

    async def store_bets_tennis_data(self, matches: List[Dict[str, Any]]) -> bool:
        """
        Store tennis match data from BetsAPI.
        
        Args:
            matches: List of match data from BetsAPI
        
        Returns:
            bool: True if storage was successful
        """
        try:
            success = True
            for match in matches:
                match_id = str(match.get('id', ''))
                if not match_id:
                    logger.warning("Skipping BetsAPI match with no id")
                    continue
                
                # Store complete raw data
                raw_data = {
                    'match_data': match,
                    'status': 'Prematch',
                    'source': 'BetsAPI',
                    'stored_at': datetime.utcnow().isoformat()
                }
                
                if not await self.store_match_data(match_id, raw_data):
                    success = False
            
            return success
        except Exception as e:
            logger.error(f"Error storing BetsAPI tennis data: {e}")
            return False

    async def get_match_data(self, match_id: str) -> Optional[Dict[str, Any]]:
        """
        Retrieve tennis match data by ID.
        
        Args:
            match_id: Match ID to retrieve
            
        Returns:
            Optional[Dict]: Match data if found, None otherwise
        """
        try:
            with self.conn.cursor() as cur:
                cur.execute(
                    "SELECT raw_data FROM tennis_matches WHERE match_id = %s",
                    (match_id,)
                )
                result = cur.fetchone()
                return json.loads(result[0]) if result else None
        except Exception as e:
            logger.error(f"Failed to retrieve match data: {e}")
            return None

# Quick test of the database operations
if __name__ == "__main__":
    import asyncio
    from rapid_tennis_fetcher import RapidInplayOddsFetcher
    
    async def test_db():
        """Test database operations with real tennis data"""
        try:
            # Initialize database
            db = TennisDatabase()
            logger.info("Database connection successful")
            
            # Fetch some live tennis data
            fetcher = RapidInplayOddsFetcher()
            matches = await fetcher.get_tennis_data()
            
            # Store the data
            if matches:
                success = await db.store_rapid_tennis_data(matches)
                logger.info(f"Stored {len(matches)} matches. Success: {success}")
                
                # Try to retrieve first match
                first_match = matches[0]
                match_id = first_match['raw_event_data'].get('marketFI', '')
                if match_id:
                    retrieved = await db.get_match_data(match_id)
                    logger.info(f"Retrieved match {match_id}: {retrieved is not None}")
            
        except Exception as e:
            logger.error(f"Test failed: {e}")
    
    asyncio.run(test_db())
