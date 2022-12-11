from datetime import datetime
from typing import List

from beanie import Document, Granularity, TimeSeriesConfig
from pydantic import BaseModel, Field

# class SensorValueBase(BaseModel):
#    sensor: str
#    value: str
#
#
# class SensorValueCreate(SensorValueBase):
#    ...
#
#
# class SensorValue(Document, SensorValueBase):
#    ...


class SensorValue(BaseModel):
    sensor: str
    value: str


class MeasurementBase(BaseModel):
    meta: str


class MeasurementCreate(MeasurementBase):
    sensor_values: List[SensorValue]


class Measurement(Document, MeasurementBase):
    ts: datetime = Field(default_factory=datetime.now)
    meta: str

    sensor_values: List[SensorValue] = []

    class Settings:
        timeseries = TimeSeriesConfig(
            time_field="ts",
            meta_field="meta",
            granularity=Granularity.seconds,
        )
