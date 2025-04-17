from fastapi import APIRouter, HTTPException, Body
from typing import List
from app.services.recommender import RecommenderService

router = APIRouter()
recommender = RecommenderService()

@router.get("/recommendations")
async def get_recommendations(preferences: List[str] = Body(..., embed=True)):
    try:
        recommended_books = await recommender.recommend_books(preferences)
        return {"recommendations": recommended_books}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))