import requests

def getBook(villian):
    peguin = requests.get(f"https://stephen-king-api.onrender.com/api/books/{villian.lower()}")
    if peguin.status_code != 200:
        print(f"Error, got {peguin.status_code}")
        return None
    
    data = peguin.json()
    return {
        "id": data["id"],
        "name": data["name"],
        "gender": data["gender"],
        "status": data["status"]
    }

books = getBook("Tina Blake")
print(books)