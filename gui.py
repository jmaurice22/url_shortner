import tkinter as tk
from tkinter import messagebox
import requests

def shorten_url_gui():
    original_url = url_entry.get()
    if not original_url:
        messagebox.showerror("Error", "Please enter a URL")
        return

    try:
        response = requests.post("http://127.0.0.1:5000/shorten", json={"url": original_url})
        if response.status_code == 201:
            short_url = response.json().get("short_url")
            result_label.config(text=f"Shortened URL: http://127.0.0.1:5000/{short_url}")
        else:
            messagebox.showerror("Error", response.json().get("error", "Unknown error"))
    except Exception as e:
        messagebox.showerror("Error", f"Failed to connect to the server: {e}")

# Function to clear the input field
def clear_input():
    url_entry.delete(0, tk.END)

# Create the Tkinter GUI
root = tk.Tk()
root.title("URL Shortener")

frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

url_label = tk.Label(frame, text="Enter URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(frame, width=40)
url_entry.grid(row=0, column=1, padx=5, pady=5)

# Bind the Enter key to the shorten_url_gui function
url_entry.bind('<Return>', lambda event: shorten_url_gui())

shorten_button = tk.Button(frame, text="Shorten", command=shorten_url_gui)
shorten_button.grid(row=1, column=0, pady=10)

# Add a Clear button to the GUI
clear_button = tk.Button(frame, text="Clear", command=clear_input)
clear_button.grid(row=1, column=1, pady=10)

result_label = tk.Label(root, text="", fg="blue")
result_label.pack(pady=10)

if __name__ == '__main__':
    root.mainloop()
