from typing import Optional

from src.crud.base import CRUDBase
from src.models import Device, DeviceCreate

# async def get_by_name(name: str) -> Optional[Device]:
#    device = await Device.find_one(Device.name == name)
#    return device


async def get_all() -> Optional[list[Device]]:
    devices = await Device.find_all().to_list()
    return devices


class CRUDDevice(CRUDBase[Device, DeviceCreate]):
    ...


device = CRUDDevice(Device)
