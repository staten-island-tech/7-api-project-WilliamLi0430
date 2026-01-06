import requests

def getBook(book):
    peguin = requests.get(f"https://stephen-king-api.onrender.com/api/books/{book.lower()}")
    if peguin.status_code != 200:
        print(f"Error, got {peguin.status_code}")
        return None
    
    data = peguin.json()
    return {
        "id": data["id"],
        "year": data["Year"],
        "title": data["Title"],
        "handle": data["handle"],
        "publisher": data["Publisher"],
        "isbn": data["ISBN"],
        "pages": data["Pages"],
        "notes": data["Notes"],
        "created_at": data["created_at"],
        "villians": data["villians"]
    }

books = getBook("Carrie")
print(books)