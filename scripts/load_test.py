import requests

URL = "http://localhost:8000/patients"

for i in range(50):
    res = requests.get(URL)
    print(f"Request {i}: {res.status_code}")