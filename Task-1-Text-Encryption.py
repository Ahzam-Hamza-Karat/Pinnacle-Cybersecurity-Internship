import tkinter as tk

app = tk.Tk()
app.title("Text Encryption Tool")
app.geometry("500x400")
app.config(bg="lightyellow")

def encrypt():
    text = input_box.get("1.0", tk.END).strip()
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, ''.join(
        chr((ord(c)-65+3)%26+65) if c.isupper() else
        chr((ord(c)-97+3)%26+97) if c.islower() else c for c in text))

def decrypt():
    text = input_box.get("1.0", tk.END).strip()
    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, ''.join(
        chr((ord(c)-65-3)%26+65) if c.isupper() else
        chr((ord(c)-97-3)%26+97) if c.islower() else c for c in text))

def clear():
    input_box.delete("1.0", tk.END)
    output_box.delete("1.0", tk.END)

tk.Label(app, text="Enter Text:", font=("Arial", 12), bg="lightyellow").pack()
input_box = tk.Text(app, height=5, width=50, font=("Arial", 12))
input_box.pack()
tk.Label(app, text="Output:", font=("Arial", 12), bg="lightyellow").pack()
output_box = tk.Text(app, height=5, width=50, font=("Arial", 12))
output_box.pack()

tk.Button(app, text="Encrypt", command=encrypt, font=("Arial", 12), bg="green", fg="white").pack(pady=5)
tk.Button(app, text="Decrypt", command=decrypt, font=("Arial", 12), bg="blue", fg="white").pack(pady=5)
tk.Button(app, text="Clear", command=clear, font=("Arial", 12), bg="red", fg="white").pack(pady=5)

app.mainloop()
