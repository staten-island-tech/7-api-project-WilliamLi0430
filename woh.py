import tkinter as tk
import requests

def getCharacters():
    input = entry.get().strip().lower()

    if not input:
        result.config("Please enter a character name.")
        return
    
    response = requests.get(f"https://stephen-king-api.onrender.com/api/villains")
    if response.status_code != 200:
        print(f"Error, got {response.status_code}")
        return None
    
    data = response.json()["data"]
    

    for villain in data:
        if input in villain["name"].lower():
            result.config(text=f"Name: {villain['name']}\nBook: {villain['books']}")
            return
        

booking = tk.Tk()
booking.title("Stephen King book characters")
booking.geometry("500x300")

prompt = tk.Label(booking, text="Which character would you like to find?", font=("Arial", 14))
prompt.pack(pady=10)

entry = tk.Entry(booking, font=("Arial", 14), width=40)
entry.pack(pady=5)

searchButton = tk.Button(booking, text="Find character", font=("Arial", 14), command=getCharacters)
searchButton.pack(pady=10)

result = tk.Label(booking, text="", font=("Arial", 15), wraplength=450, justify="center", fg="purple")
result.pack(pady=10)



booking.mainloop()
