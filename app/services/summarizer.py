import httpx
import asyncio

class SummarizerService:
    def __init__(self, model_url: str = "http://localhost:11434/api/generate"):
        self.model_url = model_url

    async def generate_summary(self, content: str) -> str:
        payload = {
            "model": "llama3",
            "prompt": f"Summarize the following book content:\n{content}",
            "stream": False
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(self.model_url, json=payload)
            response.raise_for_status()
            return response.json().get("response", "")
