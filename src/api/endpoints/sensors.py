from typing import Any, List

from beanie import WriteRules
from fastapi import APIRouter, HTTPException, status

from src import models
from src.crud import crud_device

router = APIRouter()


@router.get(
    "/", summary="Get all sensors of a device.", response_model=List[models.DeviceOut]
)
async def get_sensors(device_name: str) -> Any:
    device = await models.Device.find_one(
        models.Device.name == device_name, fetch_links=True
    )

    return device.sensors


@router.post(
    "/", status_code=status.HTTP_201_CREATED, summary="Add a new sensor to a device."
)
async def create_sensor(device_name: str, sensor_in: models.SensorCreate) -> Any:
    device = await crud_device.get_by_name(name=device_name)

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )

    # Create new sensor object and await it's insert
    sensor_create = models.Sensor(**sensor_in.dict())
    await models.Sensor.insert_one(sensor_create)

    # Add the sensor to the list of sensors for the device and replace the device data
    device.sensors.append(sensor_create)
    await models.Device.replace(device, link_rule=WriteRules.WRITE)


@router.put("/{sensor_name}")
def update_sensor_by_name(sensor_name: str) -> Any:
    # TODO Implement
    ...


@router.delete("/{sensor_name}")
def delete_sensor_by_name(sensor_name: str) -> Any:
    # TODO Implement
    ...
