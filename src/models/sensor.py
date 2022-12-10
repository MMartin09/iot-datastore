from beanie import Document
from pydantic import BaseModel


class SensorBase(BaseModel):
    name: str
    type: str


class SensorCreate(SensorBase):
    ...


class SensorOut(SensorBase):
    ...


class Sensor(Document, SensorBase):
    ...
