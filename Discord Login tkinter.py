import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def login():
    email = email_entry.get()
    password = password_entry.get()
    # Hier würde normalerweise eine Überprüfung der Anmeldedaten erfolgen
    messagebox.showinfo("Login Attempt", f"Email: {email}\nPassword: {password}")

root = tk.Tk()
root.title("Discord Login")
root.geometry("320x450")  # Fenstergröße anpassen für mehr Platz
root.configure(bg="#7289da")

# Logo laden und skalieren
original_logo = Image.open("logo.png")  # Ersetzen Sie 'path/to/discord_logo.png' mit dem tatsächlichen Pfad
resized_logo = original_logo.resize((100, 100), Image.LANCZOS)  # Verwendung von LANCZOS statt ANTIALIAS
logo = ImageTk.PhotoImage(resized_logo)
logo_label = tk.Label(root, image=logo, bg="#ffffff")
logo_label.pack(pady=(20, 10))  # Größeres Padding oben, kleineres unten

# Anmeldungsformular Container
form_frame = tk.Frame(root, bg="#ffffff")
form_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Email Entry
email_label = tk.Label(form_frame, text="Email:", bg="#ffffff")
email_label.grid(row=0, column=0)
email_entry = tk.Entry(form_frame, bd=1, relief="solid", font=("Arial", 12))
email_entry.grid(row=0, column=1, sticky="ew", padx=5)

# Password Entry
password_label = tk.Label(form_frame, text="Password:", bg="#ffffff")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(form_frame, show="*", bd=1, relief="solid", font=("Arial", 12))
password_entry.grid(row=1, column=1, sticky="ew", padx=5)

# Submit Button
submit_button = tk.Button(form_frame, text="Log In", command=login, bg="#7289da", fg="#ffffff", font=("Arial", 12))
submit_button.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

# Ensure proper expansion of fields
form_frame.grid_columnconfigure(1, weight=1)

root.mainloop()
