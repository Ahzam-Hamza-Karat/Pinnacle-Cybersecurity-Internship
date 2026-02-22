import tkinter as tk
from tkinter import messagebox
import string

app = tk.Tk()
app.title("Password Analyzer")
app.geometry("400x300")
app.config(bg="lightblue")

title_label = tk.Label(app, text="Enter your password:", font=("Arial", 12), bg="lightblue")
title_label.pack(pady=10)

password_box = tk.Entry(app, width=30, show="*", font=("Arial", 12))
password_box.pack(pady=5)

def check_password():
    password = password_box.get()
    score = 0
    result_text = ""

    if len(password) >= 12:
        result_text += "✔️ Length is good\n"
        score += 1
    else:
        result_text += "❌ Too short (at least 12 chars needed)\n"

    if any(letter.isupper() for letter in password):
        result_text += "✔️ Has uppercase letter\n"
        score += 1
    else:
        result_text += "❌ No uppercase letter\n"

    if any(letter.islower() for letter in password):
        result_text += "✔️ Has lowercase letter\n"
        score += 1
    else:
        result_text += "❌ No lowercase letter\n"

    if any(letter.isdigit() for letter in password):
        result_text += "✔️ Has a number\n"
        score += 1
    else:
        result_text += "❌ No number\n"

    if any(letter in string.punctuation for letter in password):
        result_text += "✔️ Has special symbol\n"
        score += 1
    else:
        result_text += "❌ No special symbol\n"

    result_text += f"\nPassword Score: {score}/5\n"

    if score == 5:
        result_text += "✅ Strong password!"
    elif score >= 3:
        result_text += "⚠️ Okay password, can be improved."
    else:
        result_text += "❌ Weak password. Change it."

    messagebox.showinfo("Password Analysis", result_text)

check_button = tk.Button(app, text="Check Password", command=check_password, font=("Arial", 12), bg="green", fg="white")
check_button.pack(pady=20)

app.mainloop()
