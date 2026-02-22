import tkinter as tk
from tkinter import filedialog, messagebox

def do_encrypt_or_decrypt():
    imgfile = filedialog.askopenfilename(
        title="Choose image file",
        filetypes=[("All files", "*.*")]
    )
    if imgfile == "":
        return

    k = key_box.get()
    if k == "":
        messagebox.showerror("Error", "Enter a key between 0 and 255")
        return

    try:
        k = int(k)
    except:
        messagebox.showerror("Error", "Key must be a number")
        return

    if k < 0 or k > 255:
        messagebox.showerror("Error", "Key must be between 0 and 255")
        return

    f = open(imgfile, "rb")
    stuff = f.read()
    f.close()

    out_bytes = []
    for b in stuff:
        out_bytes.append(b ^ k)
    final_data = bytes(out_bytes)

    savefile = filedialog.asksaveasfilename(
        title="Save new file",
        defaultextension=".bin",
        filetypes=[("All files", "*.*")]
    )
    if savefile == "":
        return

    f2 = open(savefile, "wb")
    f2.write(final_data)
    f2.close()

    messagebox.showinfo("Done", "Your file has been processed!")

win = tk.Tk()
win.title("Image Encrypt/Decrypt")
win.geometry("340x190")
win.config(bg="lightblue")

lbl1 = tk.Label(win, text="Image Encryption Tool", font=("Arial", 12, "bold"), bg="lightblue")
lbl1.pack(pady=8)

lbl2 = tk.Label(win, text="Key (0–255):", bg="lightblue")
lbl2.pack()

key_box = tk.Entry(win)
key_box.pack(pady=5)

btn1 = tk.Button(win, text="Pick Image & Process", command=do_encrypt_or_decrypt, bg="green", fg="white")
btn1.pack(pady=15)

win.mainloop()
