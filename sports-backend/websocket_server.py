import asyncio
import logging
import websockets
from aggregator.sports.tennis.tennis_bridge import TennisBridge

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def main():
    # Create and start the WebSocket server
    bridge = TennisBridge(host="0.0.0.0", port=8765)
    server = await bridge.start_server()
    
    try:
        logger.info("WebSocket server started. Press Ctrl+C to stop.")
        await server.wait_closed()
    except KeyboardInterrupt:
        logger.info("Received keyboard interrupt. Shutting down...")
    finally:
        logger.info("WebSocket server stopped")
