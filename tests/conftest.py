import asyncio

import httpx
import pytest
import pytest_asyncio
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src import models
from src.app import get_app
from src.models import db_models


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()


async def init_db():
    client = AsyncIOMotorClient("mongodb://admin:passwd@127.0.0.1:27017/")
    await init_beanie(database=client.db_name, document_models=db_models)


@pytest_asyncio.fixture(scope="session")
async def default_client():
    await init_db()
    app = get_app()

    async with httpx.AsyncClient(app=app, base_url="http://test") as client:
        yield client

        await models.Sensor.find_all().delete()
        await models.Device.find_all().delete()

