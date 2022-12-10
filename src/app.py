from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.api.api import api_router
from src.db.init_db import init_db


def get_app() -> FastAPI:
    service = FastAPI()

    service.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @service.on_event("startup")
    async def startup_event():
        await init_db()

    service.include_router(api_router, prefix="/api")

    return service
