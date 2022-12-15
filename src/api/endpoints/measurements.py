from typing import Any

from beanie import WriteRules
from fastapi import APIRouter, HTTPException, status

from src import models
from src.crud import crud_device

router = APIRouter()


@router.get("/")
async def get_measurements(device_name: str) -> Any:
    device = await crud_device.get_by_name(name=device_name)

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )

    measurements = await models.Measurement.find_all().to_list()
    return measurements


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_measurement(
    device_name: str, measurement_in: models.MeasurementCreate
) -> Any:
    device = await crud_device.get_by_name(name=device_name)

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )

    measurement_create = models.Measurement(**measurement_in.dict())
    await models.Measurement.insert(measurement_create, link_rule=WriteRules.WRITE)
