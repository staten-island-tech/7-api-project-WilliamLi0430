import tkinter as tk
import requests

def open_search_popup():
    popup = tk.Toplevel(root)
    popup.title("Search")
    popup.geometry("300x100")
    popup.transient(root)   # Keep popup on top of parent
    popup.grab_set()        # Make it modal

    tk.Label(popup, text="Which character are you looking for?").pack(pady=(10, 0))

    search_var = tk.StringVar()

    entry = tk.Entry(popup, textvariable=search_var, width=30)
    entry.pack(pady=5)
    entry.focus_set()
    
    entry = tk.Entry(popup, font=("Arial", 14), width=40)
    entry.pack(pady=5)

    searchButton = tk.Button(popup, text="Find character", font=("Arial", 14), command=open_search_popup)
    searchButton.pack(pady=10)

    result = tk.Label(popup, text="", font=("Arial", 15), wraplength=450, justify="center", fg="purple")
    result.pack(pady=10)

    def submit():
        print("You searched for:", search_var.get())
        popup.destroy()

    tk.Button(popup, text="OK", command=submit).pack(pady=5)


root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

tk.Button(root, text="Open Search Popup", command=open_search_popup).pack(pady=50)

def getCharacters():
    input = search_var.get().strip().lower()

    if not input:
        print("Please enter a character name.")
        return
    
    response = requests.get(f"https://stephen-king-api.onrender.com/api/villains")
    if response.status_code != 200:
        print(f"Error, got {response.status_code}")
        return None
    
    data = response.json()["data"]
    

    for villain in data:
        if input in villain["name"].lower():
            print(text=f"Name: {villain['name']}\nBook: {villain['books']}")
            return


root.mainloop()
