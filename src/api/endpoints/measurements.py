from typing import Any

from beanie import WriteRules
from fastapi import APIRouter

from src import models

router = APIRouter()


@router.post("/")
async def create_measurement(
    device_name: str,
    measurement_in: models.MeasurementCreate
) -> Any:
    measurement_create = models.Measurement(**measurement_in.dict())
    await models.Measurement.insert(measurement_create, link_rule=WriteRules.WRITE)

