from typing import Any

from fastapi import APIRouter, HTTPException, status

from src import models
from src.crud import crud_device

router = APIRouter()


@router.get("/", response_model=list[models.DeviceOut])
async def get_devices() -> Any:
    devices = await crud_device.get_all()
    return devices


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_device(device_in: models.DeviceCreate) -> Any:
    device = await crud_device.get_by_name(name=device_in.name)
    if device is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Device already exist"
        )

    device_create = models.Device(**device_in.dict())
    await models.Device.insert_one(device_create)


@router.get("/{device_name}", response_model=models.DeviceOut)
async def get_device_by_name(device_name: str) -> Any:
    device = await crud_device.get_by_name(name=device_name)

    if not device:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Device not found"
        )

    return device
