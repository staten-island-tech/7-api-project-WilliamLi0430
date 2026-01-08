import requests

def h():
    response = requests.get("https://stephen-king-api.onrender.com/api/book")
    print(response.json())

h()