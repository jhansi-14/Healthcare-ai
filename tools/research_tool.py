import requests

def search_medical_research(query):

    url = f"https://api.duckduckgo.com/?q={query}&format=json"

    response = requests.get(url).json()

    return response.get("AbstractText", "No research summary found")