"""TODO: Find a better name for the file"""
from functools import lru_cache
from typing import Optional


@lru_cache(maxsize=1)
def get_db_connection_string(
    user: str,
    passwd: str,
    url: str,
    port: Optional[int] = None,
    params: Optional[str] = None
) -> str:
    """Builds the connection string for MongDB.

    Args:
        user: Database user
        passwd: Password for the provided user
        url: Url of the database
        port: Optional connection port
        params: Optional connection parameters

    Returns:
        Full formatted connection string.

    """

    conn = "mongodb+srv://"
    conn += f"{user}:{passwd}"
    conn += f"@{url}"

    if port is not None:
        conn += f":{port}"

    if params is not None:
        conn += f"/?{params}"

    return conn
