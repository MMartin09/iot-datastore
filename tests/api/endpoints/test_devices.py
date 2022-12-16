from typing import Any

import httpx
import pytest
import pytest_asyncio

from src import models


@pytest_asyncio.fixture(scope="module")
async def mock_device() -> models.Device:
    device = models.Device(name="pico_one", type="raspberry_pico_w")

    await models.Device.insert_one(device)
    yield device


@pytest.mark.asyncio
async def test_get_devices(
    default_client: httpx.AsyncClient, mock_device: models.Device
) -> None:
    headers = {
        "Content-Type": "application/json",
    }

    url = "/api/devices/"
    response = await default_client.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json()[0]["name"] == str(mock_device.name)


@pytest.mark.asyncio
async def test_create_device(default_client: httpx.AsyncClient) -> None:
    headers = {
        "Content-Type": "application/json",
    }

    payload = {"name": "arduino_one", "type": "arduino_mkr_wifi_1010"}

    response = await default_client.post("/api/devices/", headers=headers, json=payload)

    assert response.status_code == 201


@pytest.mark.asyncio
async def test_get_device_by_name(
    default_client: httpx.AsyncClient, mock_device: models.Device
) -> None:
    headers = {
        "Content-Type": "application/json",
    }

    url = f"/api/devices/{mock_device.name}"
    response = await default_client.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json()["name"] == str(mock_device.name)


@pytest.mark.asyncio
async def test_update_device_by_name(
    default_client: httpx.AsyncClient, mock_device: models.Device
) -> Any:
    headers = {
        "Content-Type": "application/json",
    }

    device = models.DeviceCreate(**mock_device.dict())
    device.type = "new_sensor_type"

    url = f"/api/devices/{device.name}"
    response = await default_client.put(url, headers=headers, json=device.dict())

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_delete_device_by_name(default_client: httpx.AsyncClient) -> None:
    headers = {
        "Content-Type": "application/json",
    }

    device = models.Device(name="device_delete", type="raspberry_pico_w")
    await models.Device.insert_one(device)

    url = f"/api/devices/{device.name}"
    response = await default_client.delete(url, headers=headers)

    assert response.status_code == 200


@pytest.mark.asyncio
async def test_create_device_already_exist(
    default_client: httpx.AsyncClient, mock_device: models.Device
) -> None:
    headers = {
        "Content-Type": "application/json",
    }

    payload = {"name": mock_device.name, "type": mock_device.type}

    response = await default_client.post("/api/devices/", headers=headers, json=payload)

    assert response.status_code == 409


@pytest.mark.asyncio
async def test_get_device_by_name_not_found(
    default_client: httpx.AsyncClient, mock_device: models.Device
) -> None:
    ...
