import asyncio

import websockets
from websockets import ServerConnection


# Handler for Incoming Message
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Received a message : {message}")
        response = f"Server received: {message}"
        await websocket.send(response)  # sending a response

        for _ in range(5):
            await websocket.send(response)


# Starting a WebSocket server on port 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)#async? it`s awaitable
    print("WebSocket server is running on ws://localhost:8765")
    await server.wait_closed()#wait the closing from client (CTR+C or process stopped)


asyncio.run(main())
