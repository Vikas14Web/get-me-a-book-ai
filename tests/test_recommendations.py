import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_get_recommendations():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/recommendations", json={"preferences": ["sci-fi", "fantasy"]})
    assert response.status_code == 200
    data = response.json()
    assert "recommendations" in data
    assert isinstance(data["recommendations"], list)
    assert len(data["recommendations"]) > 0