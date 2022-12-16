from beanie import Document
from pydantic import BaseModel


class SensorBase(BaseModel):
    name: str
    type: str


class SensorCreate(SensorBase):
    class Config:
        schema_extra = {"example": {"name": "sps30", "type": "sensirion_sps30"}}


class SensorOut(SensorBase):
    class Config:
        schema_extra = {"example": {"name": "sps30", "type": "sensirion_sps30"}}


class Sensor(Document, SensorBase):
    ...
