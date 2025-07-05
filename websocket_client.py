import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # Server address
    async with websockets.connect(uri) as websocket:
        message = "Hello, server!"  # the client will send the message
        print(f"sending the: {message}")
        await websocket.send(message)  # sending the message


        for _ in range(5):
            response = await websocket.recv()  # received response from server
            print(f"response from server: {response}")


asyncio.run(client())
