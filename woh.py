import tkinter as tk

def say_hello():
    print("Hello!")

root = tk.Tk()
root.title("Example")
root.geometry("500x500")

label = tk.Label(root, text="Search Stephen King Characters")
label.pack(pady=10)

button = tk.Button(root, text="Click me", command=say_hello)
button.pack()

root.mainloop()