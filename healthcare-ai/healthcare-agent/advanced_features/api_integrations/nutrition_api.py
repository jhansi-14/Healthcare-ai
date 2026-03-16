import requests

def get_nutrition_data(food):
    url = f"https://api.edamam.com/search?q={food}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return {"error": "Nutrition API failed"}