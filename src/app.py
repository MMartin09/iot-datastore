from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from src.api.api import api_router
from src.core.settings.api import get_api_settings
from src.core.settings.app import get_app_settings
from src.db.init_db import init_db


def get_app() -> FastAPI:
    app_settings = get_app_settings()
    api_settings = get_api_settings()

    service = FastAPI(
        title=app_settings.APP_TITLE,
        description=app_settings.APP_DESCRIPTION,
        version=app_settings.APP_VERSION,
        redoc_url=None,  # disable Redoc
        openapi_tags=[
            {"name": "devices", "description": "Lorem ipsum dolor sit amet"},
            {"name": "sensors", "description": "Lorem ipsum dolor sit amet"},
            {"name": "measurements", "description": "Lorem ipsum dolor sit amet"},
        ],
    )

    service.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @service.get("/", include_in_schema=False)
    def get_main() -> RedirectResponse:
        return RedirectResponse(api_settings.OPENAPI_ROUTE)

    @service.on_event("startup")
    async def startup_event():
        await init_db()

    service.include_router(api_router, prefix=api_settings.API_PREFIX)

    return service
