"""
Main entry point for the sports backend service.
Orchestrates all components: sports data fetchers, API server, and database.
"""

import logging
import argparse
import asyncio
from aggregator.database.db_utils import DatabaseManager
from aggregator.serveAPI.server import start_api_server

# Import sport-specific data fetchers
from aggregator.sports.tennis.tennis_odds import TennisOdds
from aggregator.sports.soccer.soccer_odds import SoccerOdds
from aggregator.sports.basketball.basketball_odds import BasketballOdds

def parse_args():
    parser = argparse.ArgumentParser(description='Sports Backend Service')
    parser.add_argument(
        '--interval',
        type=int,
        default=60,
        help='Data update interval in seconds (default: 60)'
    )
    parser.add_argument(
        '--port',
        type=int,
        default=8000,
        help='API server port (default: 8000)'
    )
    return parser.parse_args()

async def run_sports_fetchers(db: DatabaseManager, interval: int):
    """Run all sports data fetchers concurrently"""
    # Initialize fetchers
    tennis = TennisOdds(db)
    soccer = SoccerOdds(db)
    basketball = BasketballOdds(db)
    
    while True:
        try:
            # Run all fetchers concurrently
            tasks = [
                tennis.run_once(),
                soccer.run_once(),
                basketball.run_once()
            ]
            await asyncio.gather(*tasks, return_exceptions=True)
            
            # Wait for next update
            await asyncio.sleep(interval)
            
        except Exception as e:
            logging.error(f"Error in sports fetchers: {e}")
            await asyncio.sleep(10)

async def main():
    # Set up logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    logger = logging.getLogger(__name__)

    # Parse command line arguments
    args = parse_args()

    try:
        logger.info("Initializing Sports Backend Service")
        
        # Initialize database
        db = DatabaseManager()
        
        # Start API server
        api_server = await start_api_server(port=args.port)
        logger.info(f"API server running on port {args.port}")
        
        # Start sports data fetchers
        logger.info(f"Starting sports fetchers with {args.interval}s interval")
        await run_sports_fetchers(db, args.interval)
        
    except KeyboardInterrupt:
        logger.info("Service stopped by user")
    except Exception as e:
        logger.error(f"Service error: {e}")
        raise
    finally:
        # Cleanup
        await api_server.shutdown()
        db.close()

if __name__ == "__main__":
    asyncio.run(main())
