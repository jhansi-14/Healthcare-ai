from functools import lru_cache

# Simple in-memory caching

@lru_cache(maxsize=100)
def get_cached_health_data(user_id: str):
    print("Fetching from DB...")
    return {
        "user_id": user_id,
        "bp": "120/80",
        "sugar": "90 mg/dL"
    }