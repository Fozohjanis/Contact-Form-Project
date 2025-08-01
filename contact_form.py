import tkinter as tk
from tkinter import messagebox
import csv

# Function to save contact info to CSV
def save_data():
    name = entry_name.get()
    email = entry_email.get()
    phone = entry_phone.get()
    address = entry_address.get("1.0", tk.END).strip()

    if not (name and email and phone and address):
        messagebox.showwarning("Input Error", "All fields are required!")
        return

    with open('contacts.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, email, phone, address])

    messagebox.showinfo("Success", "Contact saved successfully!")

    # Clear the form fields
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_address.delete("1.0", tk.END)

# Create GUI window
window = tk.Tk()
window.title("Contact Form")
window.geometry("400x400")

# Form fields
tk.Label(window, text="Name:").pack()
entry_name = tk.Entry(window, width=40)
entry_name.pack()

tk.Label(window, text="Email:").pack()
entry_email = tk.Entry(window, width=40)
entry_email.pack()

tk.Label(window, text="Phone Number:").pack()
entry_phone = tk.Entry(window, width=40)
entry_phone.pack()

tk.Label(window, text="Address:").pack()
entry_address = tk.Text(window, width=30, height=4)
entry_address.pack()

# Submit button
tk.Button(window, text="Submit", command=save_data).pack(pady=10)

# Run the app
window.mainloop()