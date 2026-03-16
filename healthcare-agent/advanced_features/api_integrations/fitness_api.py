import requests

def get_steps_data(user_id):
    url = f"https://api.mockfitness.com/steps/{user_id}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return {"error": "Unable to fetch fitness data"}