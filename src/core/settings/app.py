from functools import lru_cache

from pydantic import BaseSettings


class AppSettings(BaseSettings):
    DB_USER: str
    DB_PASSWD: str
    DB_URL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_app_settings() -> AppSettings:
    return AppSettings()
