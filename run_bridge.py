import asyncio
import logging
from aggregator.sports.tennis.tennis_bridge import TennisBridge

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

async def main():
    bridge = TennisBridge(host="0.0.0.0", port=8765)
    await bridge.start_server()

if __name__ == "__main__":
    asyncio.run(main())
