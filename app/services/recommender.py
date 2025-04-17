from typing import List

class RecommenderService:
    def __init__(self):
        pass

    async def recommend_books(self, user_preferences: List[str]) -> List[str]:
        recommendations = []

        for preference in user_preferences:
            if preference.lower() == "sci-fi":
                recommendations.append("Dune")
            elif preference.lower() == "fantasy":
                recommendations.append("The Hobbit")
            elif preference.lower() == "mystery":
                recommendations.append("Gone Girl")
            else:
                recommendations.append("The Alchemist")

        return recommendations[:5]