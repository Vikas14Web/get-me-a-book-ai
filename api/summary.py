from fastapi import APIRouter, HTTPException, Body
from app.services.summarizer import SummarizerService

router = APIRouter()
summarizer = SummarizerService()

@router.post("/generate-summary")
async def generate_summary(content: str = Body(..., embed=True)):
    try:
        summary = await summarizer.generate_summary(content)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
