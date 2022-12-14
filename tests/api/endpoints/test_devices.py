import httpx
import pytest
import pytest_asyncio

from src import models


@pytest_asyncio.fixture(scope="module")
async def mock_device() -> models.Device:
    device = models.Device(
        name="pico_one",
        type="raspberry_pico_w"
    )

    await models.Device.insert_one(device)
    yield device


@pytest.mark.asyncio
async def test_get_devices(default_client: httpx.AsyncClient, mock_device: models.Device):
    url = "/api/devices/"
    response = await default_client.get(url)

    assert response.status_code == 200
    assert response.json()[0]["name"] == str(mock_device.name)


@pytest.mark.asyncio
async def test_get_device(default_client: httpx.AsyncClient, mock_device: models.Device):
    url = f"/api/devices/{mock_device.name}"
    response = await default_client.get(url)

    assert response.status_code == 200
    assert response.json()["name"] == str(mock_device.name)
