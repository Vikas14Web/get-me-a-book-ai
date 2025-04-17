import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_generate_summary():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/generate-summary", json={"content": "This is a test content for summary."})
    assert response.status_code == 200
    data = response.json()
    assert "summary" in data
    assert isinstance(data["summary"], str)
    assert len(data["summary"]) > 0