import tkinter as tk
import requests

def open_search_popup():
    popup = tk.Toplevel(root)
    popup.title("Search")
    popup.geometry("500x500")

    tk.Label(
        popup,
        text="Which character are you looking for?",
        font=("Arial", 12)
    ).pack(pady=(10, 5))

    search_var = tk.StringVar()

    entry = tk.Entry(popup, textvariable=search_var, font=("Arial", 14), width=30)
    entry.pack(pady=5)
    entry.focus_set()

    result_label = tk.Label(
        popup,
        text="",
        font=("Arial", 12),
        wraplength=450,
        justify="center",
        fg="purple"
    )
    result_label.pack(pady=10)

    def getCharacters():
        name = search_var.get().strip().lower()

        if not name:
            result_label.config(text="Please enter a character name.")
            return

        response = requests.get("https://stephen-king-api.onrender.com/api/villains")
        if response.status_code != 200:
            print(f"Error, got code {response.status_code}")
            return

        data = response.json()["data"]

        for villain in data:
            if name in villain["name"].lower():
                result_label.config(text=f"Name: {villain['name']}\nBook(s): {', '.join(villain['books'])}")
                return

        result_label.config(text="No matching character found.")

    tk.Button(
        popup,
        text="Find character",
        font=("Arial", 12),
        command=getCharacters
    ).pack(pady=5)


root = tk.Tk()
root.geometry("500x300")

tk.Button(
    root,
    text="Start searching!",
    font=("Arial", 12),
    command=open_search_popup
).pack(pady=60)

root.mainloop()
