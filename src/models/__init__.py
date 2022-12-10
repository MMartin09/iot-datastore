from src.models.device import Device, DeviceOut, DeviceCreate
from src.models.sensor import Sensor, SensorOut, SensorCreate
from src.models.measurement import Measurement, MeasurementCreate, SensorValue

db_models = [
    Device,
    Sensor,
    Measurement
]
