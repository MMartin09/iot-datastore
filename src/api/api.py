from fastapi import APIRouter

from src.api.endpoints import devices, sensors, measurements

api_router = APIRouter()
api_router.include_router(devices.router, prefix="/devices", tags=["devices"])
api_router.include_router(sensors.router, prefix="/devices/{device_name}/sensors", tags=["sensors"])
api_router.include_router(measurements.router, prefix="/devices/{device_name}/measurements", tags=["measurements"])
