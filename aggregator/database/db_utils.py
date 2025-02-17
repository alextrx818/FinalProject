"""
Database connection logic and helper functions for insert/update/query operations.
"""

import psycopg2
from psycopg2.extras import RealDictCursor
from typing import Dict, List
import logging
from ..config import DB_CONFIG

logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self):
        self.config = DB_CONFIG

    def get_connection(self):
        """Create a new database connection"""
        try:
            return psycopg2.connect(**self.config)
        except psycopg2.Error as e:
            logger.error(f"Error connecting to database: {str(e)}")
            return None

    def store_tennis_data(self, data: List[Dict]):
        """Store tennis match data in the database"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            for match in data:
                cur.execute("""
                    INSERT INTO tennis_odds 
                    (match_id, event_name, status, odds_data, timestamp)
                    VALUES (%s, %s, %s, %s, NOW())
                    ON CONFLICT (match_id) 
                    DO UPDATE SET odds_data = %s, timestamp = NOW()
                """, (
                    match["match_id"],
                    match["event_name"],
                    match["status"],
                    match["odds"],
                    match["odds"]
                ))
            
            conn.commit()
            logger.info(f"Successfully stored {len(data)} tennis matches")
        except Exception as e:
            conn.rollback()
            logger.error(f"Error storing tennis data: {str(e)}")
        finally:
            cur.close()
            conn.close()

    def get_live_tennis_matches(self) -> List[Dict]:
        """Retrieve live tennis matches from the database"""
        conn = self.get_connection()
        cur = conn.cursor()
        
        try:
            cur.execute("""
                SELECT * FROM tennis_odds 
                WHERE status = 'Live'
                ORDER BY timestamp DESC
            """)
            return cur.fetchall()
        finally:
            cur.close()
            conn.close()
