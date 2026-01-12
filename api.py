import requests





def getBook():
    response = requests.get(f"https://stephen-king-api.onrender.com/api/villains")
    if response.status_code != 200:
        print(f"Error, got {response.status_code}")
        return None




books = getBook("Carrie")
print(books)

