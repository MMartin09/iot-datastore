from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from src.core.settings.app import get_app_settings
from src.db.helper import get_db_connection_string
from src.models import db_models

app_settings = get_app_settings()


async def init_db() -> None:
    connection_string = get_db_connection_string(
        user=app_settings.DB_USER,
        passwd=app_settings.DB_PASSWD,
        url=app_settings.DB_URL,
        params="retryWrites=true&w=majority",
    )

    client = AsyncIOMotorClient(connection_string)
    await init_beanie(database=client.db_name, document_models=db_models)
