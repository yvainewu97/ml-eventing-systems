import asyncio
from app.event_bus import event_bus
from app.processor import process_event

async def worker():
    while True:
        event = await event_bus.consume()
        result = process_event(event)
        print("processed:", result)