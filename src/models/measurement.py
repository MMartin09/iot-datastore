from datetime import datetime
from typing import Dict, List, Union

from beanie import Document, Granularity, TimeSeriesConfig
from pydantic import BaseModel, Field


class SensorValue(BaseModel):
    name: str
    value: Union[int, float]


class MeasurementBase(BaseModel):
    ...


class MeasurementCreate(MeasurementBase):
    sensor_values: List[SensorValue]


class Measurement(Document, MeasurementBase):
    ts: datetime = Field(default_factory=datetime.now)
    meta: Dict[str, str] = {}

    sensor_values: List[SensorValue] = []

    class Settings:
        timeseries = TimeSeriesConfig(
            time_field="ts",
            meta_field="meta",
            granularity=Granularity.seconds,
        )
