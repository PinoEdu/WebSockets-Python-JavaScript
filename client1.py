import asyncio
import websockets

IP = "localhost"
PORT = 5000

async def send_first_message():
    async with websockets.connect(f"ws://{IP}:{PORT}") as websocket:
        while True: 
            await websocket.send("The database was updated")
            await asyncio.sleep(1)

async def main():
    asyncio.create_task(send_first_message())
    await asyncio.Future()

asyncio.run(main())