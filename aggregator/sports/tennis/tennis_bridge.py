import asyncio
import websockets
import logging

logger = logging.getLogger(__name__)

class TennisBridge:
    """
    A WebSocket bridge to forward data from the back end to the Vue front end.
    """
    def __init__(self, host="localhost", port=8765):
        self.host = host
        self.port = port
        self.connected_clients = set()

    async def register(self, websocket):
        """Register a new client connection."""
        self.connected_clients.add(websocket)
        logger.info(f"Client connected from {websocket.remote_address}")

    async def unregister(self, websocket):
        """Unregister a client connection."""
        self.connected_clients.remove(websocket)
        logger.info(f"Client disconnected from {websocket.remote_address}")

    async def broadcast(self, message: str):
        """
        Broadcast a message (JSON string) to all connected clients.
        
        :param message: The JSON string message to send.
        """
        if self.connected_clients:
            logger.info(f"Broadcasting to {len(self.connected_clients)} clients")
            await asyncio.wait([client.send(message) for client in self.connected_clients])
        else:
            logger.info("No clients connected")

    async def handler(self, websocket):
        """
        Handle incoming WebSocket connections.
        
        :param websocket: The WebSocket connection.
        """
        await self.register(websocket)
        try:
            # Keep the connection open to listen for incoming messages if needed.
            async for message in websocket:
                # Optionally handle incoming messages from the client.
                logger.info(f"Received from client: {message}")
        except websockets.exceptions.ConnectionClosed:
            pass
        finally:
            await self.unregister(websocket)

    async def start_server(self):
        """
        Start the WebSocket server and run it forever.
        """
        logger.info(f"Starting TennisBridge on {self.host}:{self.port}")
        server = await websockets.serve(self.handler, self.host, self.port)
        await server.wait_closed()
