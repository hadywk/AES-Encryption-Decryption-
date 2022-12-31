
import base64
from Cryptodome.Cipher import AES
from tkinter import Tk, Entry, Button, Label

# Create the main window
window = Tk()
window.title("AES Encryption/Decryption")

# Create a label for the key input field
key_label = Label(window, text="Key:")
key_label.grid(row=0, column=0)

# Create an input field for the key
key_entry = Entry(window, width=32)
key_entry.grid(row=0, column=1)

# Create a label for the message input field
message_label = Label(window, text="Message:")
message_label.grid(row=1, column=0)

# Create an input field for the message
message_entry = Entry(window, width=100)
message_entry.grid(row=1, column=1)
