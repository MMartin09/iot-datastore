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


@router.get("/{sensor_name}")
async def get_measurements_by_sensor(device_name: str, sensor_name: str) -> Any:
    ...


@router.post("/{sensor_name}", status_code=status.HTTP_201_CREATED)
async def create_measurement(
    device_name: str, sensor_name: str, measurement_in: models.MeasurementCreate
) -> Any:
    device = await models.Device.find_one(
        models.Device.name == device_name,
        fetch_links=True,
    )

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )

    idx: int = -1
    for i, sensor in enumerate(device.sensors):
        if sensor.name == sensor_name:
            idx = i

    if idx == -1:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Sensor not found"
        )

    measurement_create = models.Measurement(
        **measurement_in.dict(),
    )
    measurement_create.meta["sensorId"] = device.sensors[idx].id
    measurement_create.meta["type"] = device.sensors[idx].type

    await models.Measurement.insert(measurement_create, link_rule=WriteRules.WRITE)
