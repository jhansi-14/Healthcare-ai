import requests

def fetch_medical_research(query):

    url = f"https://api.ncbi.nlm.nih.gov/lit/ctxp/v1/pubmed/?format=json&id={query}"

    r = requests.get(url)

    if r.status_code == 200:
        return r.json()

    return {"error":"Research fetch failed"}