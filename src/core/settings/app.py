from functools import lru_cache

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    APP_TITLE: str = "IoT-Datastore"
    APP_DESCRIPTION: str = (
        "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam"
    )
    APP_VERSION: str = "0.1.0"

    DB_USER: str = "admin"
    DB_PASSWD: str = "passwd"
    DB_URL: str = "localhost:27017"

    # class Config:
    #    env_file = ".env"
    #    env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_app_settings() -> AppSettings:
    return AppSettings()
