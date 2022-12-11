from typing import Any

from fastapi import APIRouter, HTTPException, status

from src import models
from src.crud import crud_device
from src.db.init_db import init_db

router = APIRouter()


@router.get("/", response_model=list[models.DeviceOut])
async def get_devices() -> Any:
    await init_db()

    devices = await crud_device.get_all()
    return devices


@router.post("/")
async def create_device(device_in: models.DeviceCreate) -> Any:
    await init_db()

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
