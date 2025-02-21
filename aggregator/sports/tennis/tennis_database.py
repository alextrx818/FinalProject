"""
Tennis-specific database operations for storing and retrieving tennis match data using asyncpg.
"""

import json
import logging
import asyncpg
import uuid  # For generating unique IDs
from typing import Dict, List, Optional, Any
from datetime import datetime
import asyncio

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Tennis Database Configuration
# For production, consider using environment variables instead.
TENNIS_DB_CONFIG = {
    'database': 'tennis_db',
    'user': 'amireslami',
    'password': 'LIncoln95amir',
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
    Handles storage and retrieval of tennis match data using asyncpg.
    """

    def __init__(self, pool: asyncpg.Pool):
        self.pool = pool

    @classmethod
    async def create(cls):
        """
        Asynchronously create a TennisDatabase instance with an asyncpg connection pool,
        and initialize the required tables and indexes.
        """
        pool = await asyncpg.create_pool(**TENNIS_DB_CONFIG)
        self = cls(pool)
        async with pool.acquire() as conn:
            await conn.execute(CREATE_TENNIS_MATCHES_TABLE)
            await conn.execute(CREATE_TENNIS_MATCHES_INDEX)
            logger.info("Tennis database tables initialized")
        logger.info("Successfully connected to tennis database")
        return self

    async def store_match_data(self, match_id: str, raw_data: Dict[str, Any]) -> bool:
        """
        Store tennis match data in the tennis_matches table.
        If no valid match_id is provided, generate a new unique internal ID.
        
        Args:
            match_id: Unique identifier for the match (can be empty or None)
            raw_data: Raw match data to store as JSONB
        
        Returns:
            bool: True if storage was successful
        """
        try:
            # Generate an internal UUID if match_id is not provided or empty
            if not match_id:
                match_id = str(uuid.uuid4())
                logger.info(f"No match_id found. Generated internal ID: {match_id}")
            async with self.pool.acquire() as conn:
                await conn.execute(
                    """
                    INSERT INTO tennis_matches (match_id, raw_data)
                    VALUES ($1, $2)
                    ON CONFLICT (match_id) DO UPDATE 
                    SET raw_data = EXCLUDED.raw_data,
                        inserted_at = NOW()
                    """,
                    match_id, json.dumps(raw_data)
                )
            return True
        except Exception as e:
            logger.error(f"Failed to store match data: {e}")
            return False

    async def store_merged_data(self, merged_matches: List[Dict[str, Any]]) -> bool:
        """
        Store merged tennis match data (as produced by tennis_merger.py) in the database.
        The data is stored raw in the JSONB 'raw_data' column without any modifications.
        If the merged record doesn't include a valid external ID, an internal one is generated.
        
        Args:
            merged_matches: List of merged match dictionaries
        
        Returns:
            bool: True if all matches were stored successfully, False otherwise.
        """
        try:
            success = True
            for match in merged_matches:
                # Determine a match_id from the merged data.
                # We assume that either the betsapi_data or rapid_data contains an "id" field.
                match_id = None
                if match.get("betsapi_data") and match["betsapi_data"].get("id"):
                    match_id = match["betsapi_data"]["id"]
                elif match.get("rapid_data") and match["rapid_data"].get("id"):
                    match_id = match["rapid_data"]["id"]
                
                # If no external match_id is found, log a warning with player info and let store_match_data generate one.
                if not match_id:
                    player_info = f"{match.get('home_player', 'Unknown')} vs {match.get('away_player', 'Unknown')}"
                    logger.warning("No valid external ID found for match (%s); an internal ID will be generated.", player_info)
                    match_id = ""
                    
                if not await self.store_match_data(match_id, match):
                    success = False
            return success
        except Exception as e:
            logger.error(f"Error storing merged tennis data: {e}")
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
            async with self.pool.acquire() as conn:
                row = await conn.fetchrow("SELECT raw_data FROM tennis_matches WHERE match_id = $1", match_id)
                if row:
                    return json.loads(row['raw_data'])
                return None
        except Exception as e:
            logger.error(f"Failed to retrieve match data: {e}")
            return None

    async def close(self):
        """Close the connection pool."""
        await self.pool.close()


# Quick test of the database operations (for merged data)
if __name__ == "__main__":
    async def test_merged_db():
        """
        Test database operations by storing and retrieving merged tennis match data.
        This data comes from the merger (tennis_merger.py) and is stored raw.
        """
        try:
            # Initialize database using asyncpg
            db = await TennisDatabase.create()
            logger.info("Database connection successful")
            
            # Example merged data from your merger (mock data)
            merged_data = [
                {
                    "home_player": "Joe",
                    "away_player": "Jim",
                    "betsapi_data": {"id": "M001", "details": "Prematch info for Joe vs Jim"},
                    "rapid_data": {"id": "M001", "odds": {"Joe": 1.5, "Jim": 2.5}, "inplay_stats": "Set1: 6-4, 3-6, 7-5"}
                },
                {
                    "home_player": "Karen",
                    "away_player": "Sue",
                    "betsapi_data": {"id": "M002", "details": "Prematch info for Karen vs Sue"},
                    "rapid_data": {"id": "M002", "odds": {"Karen": 1.8, "Sue": 2.2}, "inplay_stats": "Set1: 7-6, 4-6, 6-4"}
                },
                {
                    "home_player": "Alice",
                    "away_player": "Bob",
                    # No external ID provided here. An internal ID will be generated.
                    "betsapi_data": {},
                    "rapid_data": {"odds": {"Alice": 2.0, "Bob": 1.8}, "inplay_stats": "Set1: 6-3, 6-4"}
                }
            ]
            
            # Store merged data
            success = await db.store_merged_data(merged_data)
            logger.info(f"Stored merged data. Success: {success}")
            
            # Retrieve one match to verify
            retrieved = await db.get_match_data("M001")
            logger.info(f"Retrieved match M001: {retrieved is not None}")
            print("Retrieved data for M001:", retrieved)
            
            await db.close()
            
        except Exception as e:
            logger.error(f"Test failed: {e}")
    
    asyncio.run(test_merged_db())
