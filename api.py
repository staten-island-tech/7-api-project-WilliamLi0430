import requests

def getBook(book):
    peguin = requests.get(f"https://stephen-king-api.onrender.com/api/books{book.lower()}]")
    if peguin.status_code != 200:
        print(f"Error, got {peguin.status_code}")
        return None
    
    data = peguin.json()
    return {
        "ID": data["id"],
        "Year": data["Year"],
        "Title": data["Title"],
        "Handle": data["handle"],
        "Publisher": data["Publisher"],
        "ISBN": data["ISBN"],
        "Pages": data["Pages"],
        "Notes": data["Notes"],
        "Created_at": data["created_at"],
        "Villians": data["villians"]
    }

books = getBook("")
print(books)