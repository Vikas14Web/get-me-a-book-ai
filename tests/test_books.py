import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_create_and_get_book():
    book_data = {
        "title": "Test Book",
        "author": "Test Author",
        "genre": "Fantasy",
        "year_published": 2023
    }
    async with AsyncClient(app=app, base_url="http://test") as ac:
        post_response = await ac.post("/books", json=book_data)
        assert post_response.status_code == 200
        book = post_response.json()
        assert book["title"] == "Test Book"

        get_response = await ac.get(f"/books/{book['id']}")
        assert get_response.status_code == 200
        fetched_book = get_response.json()
        assert fetched_book["id"] == book["id"]
