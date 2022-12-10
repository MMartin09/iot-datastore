from typing import Optional, List

from beanie import Document, Link
from pydantic import BaseModel

from src.models.sensor import Sensor


class DeviceBase(BaseModel):
    name: str
    type: str


class DeviceCreate(DeviceBase):

    class Config:
        schema_extra = {
            "example": {
                "name": "pico_one",
                "type": "raspberry_pico_w"
            }
        }


class DeviceOut(DeviceBase):

    class Config:
        schema_extra = {
            "example": {
                "name": "pico_one",
                "type": "raspberry_pico_w"
            }
        }


class Device(Document, DeviceBase):
    sensors: List[Link[Sensor]] = []
