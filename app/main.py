from fastapi import FastAPI
from app.event_bus import event_bus
import asyncio
from app.worker import worker

app = FastAPI()

@app.on_event("startup")
async def startup():
    asyncio.create_task(worker())

@app.post("/event")
async def send_event(data: dict):
    await event_bus.publish(data)
    return {"status": "event received"}