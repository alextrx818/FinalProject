# tennis_parser.py
import logging
import json
import asyncio

logger = logging.getLogger(__name__)

class TennisParser:
    """
    Pure pass-through parser: It receives merged match data and forwards it to the bridge
    without modifying the data.
    """
    def __init__(self, bridge):
        self.bridge = bridge

    async def process_data(self, merged_data):
        """
        Process the merged data with zero transformation.
        - Log the number of records.
        - Convert the raw merged data to a JSON string.
        - Broadcast the JSON string through the bridge.
        """
        logger.info(f"Parser received {len(merged_data)} merged match records.")
        
        # Transform the data for frontend
        frontend_data = []
        for match in merged_data:
            bets_data = match.get('betsapi_data', {})
            rapid_data = match.get('rapid_data', {}).get('raw_event_data', {})
            
            # Debug: Print odds data structure
            logger.info(f"Match: {match.get('home_player')} vs {match.get('away_player')}")
            logger.info(f"BetsAPI data: {json.dumps(bets_data, indent=2)}")
            logger.info(f"RapidAPI data: {json.dumps(rapid_data, indent=2)}")
            
            frontend_match = {
                'home_player': match.get('home_player', 'Unknown'),
                'away_player': match.get('away_player', 'Unknown'),
                'status': rapid_data.get('status', bets_data.get('status', 'Unknown')),
                'pre_match_odds': bets_data.get('odds', {}).get('1', 'N/A') if isinstance(bets_data.get('odds'), dict) else bets_data.get('odds', 'N/A'),
                'live_odds': rapid_data.get('odds', {}).get('1', 'N/A') if isinstance(rapid_data.get('odds'), dict) else rapid_data.get('odds', 'N/A')
            }
            frontend_data.append(frontend_match)
            
        logger.info(f"Transformed data for frontend: {json.dumps(frontend_data, indent=2)}")
        
        # Convert data to JSON string and broadcast
        data_json = json.dumps(frontend_data)
        logger.info(f"Broadcasting data to all connected clients: {data_json}")
        await self.bridge.broadcast(data_json)
