from typing import Optional

from src.models import Sensor


async def get_by_name(name: str) -> Optional[Sensor]:
    sensor = await Sensor.find_one(Sensor.name == name)
    return sensor


async def get_all() -> Optional[list[Sensor]]:
    sensors = await Sensor.find_all().to_list()
    return sensors
