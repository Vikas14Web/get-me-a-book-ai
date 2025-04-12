class SummarizerService:
    def __init__(self):
        pass

    async def generate_summary(self, content: str) -> str:
        if not content.strip():
            return "Summary not available for empty content."

        return "This is a mock summary generated for the provided content."
