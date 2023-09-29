from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64

FONT = ("times new roman", 12, "normal")

window = Tk()
window.title("Top Secret")
window.geometry("300x600")
window.config(padx=10, pady=15)

key_word = "Kaan"

def saveEncrypt():

    title = title_entry.get()
    text = text_text.get("1.0", END)
    key_input = key_entry.get()

    message_bytes = text.encode("ascii")
    base64_bytes = base64.b64encode(message_bytes)
    coded_text = base64_bytes.decode("ascii")
    if text_text != "" and title_entry != "":
        with open("Secret_Notes.txt", "a") as file:
            file.write(title)
            file.write("\n")
            file.write(str(coded_text))
            file.write("\n\n")
    title_entry.delete(0, "end")
    text_text.delete("1.0", "end")
    key_entry.delete(0, "end")

    return key_input, text, title

def decryptText():
    encoded_text = text_text.get("1.0", END)
    base64_bytes = encoded_text.encode("ascii")
    message_bytes = base64.b64decode(base64_bytes)
    decoded_text = message_bytes.decode("ascii")
    text_text.delete("1.0", "end")
    text_text.insert(END, decoded_text)
    key_entry.delete(0, "end")
    text_text.after(5000, deleteTime)


def wrongPassword():
    wrong_input = key_entry.get()
    key_wrong = Fernet.generate_key()
    wrong_enc = Fernet(key_wrong)
    wrong_text = str(wrong_enc.encrypt(wrong_input.encode()))
    text_text.insert(END, wrong_text)
    text_text.after(2000, deleteTime)

def deleteTime():
    text_text.delete("1.0", END)

def possibilities():
    key_input, text, title = saveEncrypt()
    if key_input == key_word:
        if title == "" and text == "":
            messagebox.showinfo("showerror", "Title and Text Please")
        elif title != "" and text == "":
            messagebox.showinfo("showerror", "Text Please")
        elif title == "" and text != "":
            decryptText()
        else:
            saveEncrypt()
    elif key_input == "":
        messagebox.showinfo("showerror", "Password Please")
    else:
        wrongPassword()

img = PhotoImage(file="topsecret.png")
img_label = Label(image=img)
img_label.pack(pady=(0, 20))

title_label = Label(text="Please Enter Your Title", font=FONT)
title_label.pack()
title_entry = Entry(width=30)
title_entry.pack()

text_label = Label(text="Please Enter Your Text", font=FONT)
text_label.pack()
text_text = Text(height=13, width=30)
text_text.pack(pady=(0, 5))

key_label = Label(text="Please Enter Key", font=FONT)
key_label.pack()
key_entry = Entry(width=30)
key_entry.config(show="*")
key_entry.pack(pady=(0, 5))

save_button = Button(text="Save & Encrypt", font=FONT, command=possibilities)
save_button.pack(pady=(0, 5))

decrypt_button = Button(text="Decrypt", font=FONT, command=decryptText)
decrypt_button.pack()

mainloop()