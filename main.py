
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


# Create a function to perform encryption
def encrypt():
    # Get the key and message from the input fields
    key = key_entry.get()
    message = message_entry.get()

    # Pad the message to be a multiple of 16 bytes
    message = message + " " * (16 - (len(message) % 16))

    # Convert the key and message to bytes
    key = key.encode()
    message = message.encode()

    # Create the AES cipher object
    cipher = AES.new(key, AES.MODE_ECB)

    # Encrypt the message 10 times
    for i in range(10):
        message = cipher.encrypt(message)

    # Encode the encrypted message as a base64 string
    encrypted_message = base64.b64encode(message).decode()

    # Update the message input field with the encrypted message
    message_entry.delete(0, 'end')
    message_entry.insert(0, encrypted_message)

    
    # Create a function to perform decryption
def decrypt():
    # Get the key and message from the input fields
    key = key_entry.get()
    message = message_entry.get()

    # Convert the key to bytes
    key = key.encode()

    # Decode the message from a base64 string
    message = base64.b64decode(message)

    # Create the AES cipher object
    cipher = AES.new(key, AES.MODE_ECB)

    # Decrypt the message 10 times
    for i in range(10):
        message = cipher.decrypt(message)

    # Convert the decrypted message to a string
    decrypted_message = message.decode().strip()

    # Update the message input field with the decrypted message
    message_entry.delete(0, 'end')
    message_entry.insert(0, decrypted_message)

    # Create
# Create an "Encrypt" button
encrypt_button = Button(window, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0)

# Create a "Decrypt" button
decrypt_button = Button(window, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=1)

# Run the main loop
window.mainloop()
