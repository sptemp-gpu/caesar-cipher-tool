import tkinter as tk
from tkinter import messagebox, simpledialog
from cipher import caesar_cipher, vigenere_cipher, aes_encrypt, aes_decrypt

# Function to set up the GUI components
def setup_gui(root):
    root.title("Cipher Tool")
    root.geometry("600x500")

    # Title label
    label_title = tk.Label(root, text="Cipher Tool", font=("Arial", 18, "bold"))
    label_title.grid(row=0, column=0, columnspan=2, pady=10)

    # Text input for the user to enter the message
    label_text = tk.Label(root, text="Enter Text:")
    label_text.grid(row=1, column=0, sticky="w", padx=10)
    entry_text = tk.Text(root, height=6, width=40)
    entry_text.grid(row=1, column=1, padx=10, pady=5)

    # Text input for the shift value or key
    label_shift = tk.Label(root, text="Shift/Key:")
    label_shift.grid(row=2, column=0, sticky="w", padx=10)
    entry_shift = tk.Entry(root, width=15)
    entry_shift.grid(row=2, column=1, padx=10, pady=5)

    # Encrypt and Decrypt buttons for each cipher
    button_encrypt_caesar = tk.Button(root, text="Encrypt Caesar", width=20, command=encrypt_caesar)
    button_encrypt_caesar.grid(row=3, column=0, padx=10, pady=10)
    
    button_decrypt_caesar = tk.Button(root, text="Decrypt Caesar", width=20, command=decrypt_caesar)
    button_decrypt_caesar.grid(row=3, column=1, padx=10, pady=10)

    button_encrypt_vigenere = tk.Button(root, text="Encrypt Vigenère", width=20, command=encrypt_vigenere)
    button_encrypt_vigenere.grid(row=4, column=0, padx=10, pady=10)

    button_decrypt_vigenere = tk.Button(root, text="Decrypt Vigenère", width=20, command=decrypt_vigenere)
    button_decrypt_vigenere.grid(row=4, column=1, padx=10, pady=10)

    button_encrypt_aes = tk.Button(root, text="Encrypt AES", width=20, command=encrypt_aes)
    button_encrypt_aes.grid(row=5, column=0, padx=10, pady=10)

    button_decrypt_aes = tk.Button(root, text="Decrypt AES", width=20, command=decrypt_aes)
    button_decrypt_aes.grid(row=5, column=1, padx=10, pady=10)

    # Output field for showing the result
    label_result = tk.Label(root, text="Result:")
    label_result.grid(row=6, column=0, sticky="w", padx=10)
    text_result = tk.Text(root, height=6, width=40)
    text_result.grid(row=6, column=1, padx=10, pady=5)

    # Help button
    button_help = tk.Button(root, text="Help", width=20, command=show_help)
    button_help.grid(row=7, column=0, columnspan=2, pady=10)

    return entry_text, entry_shift, text_result

# Function to show help dialog
def show_help():
    help_message = """
    This tool helps you encrypt and decrypt text using various ciphers:
    
    1. Caesar Cipher: A simple shift cipher.
    2. Vigenère Cipher: A cipher that uses a key string.
    3. AES Encryption: A strong symmetric encryption method.
    
    Instructions:
    - Enter the text you want to encrypt or decrypt.
    - Specify the shift value (for Caesar) or key (for Vigenère and AES).
    - Click the appropriate encryption or decryption button.
    - The result will be displayed below.
    """
    messagebox.showinfo("Help", help_message)

# Caesar Cipher functions
def encrypt_caesar():
    try:
        text = entry_text.get("1.0", "end-1c")
        shift = int(entry_shift.get())
        encrypted_text = caesar_cipher(text, shift)
        text_result.delete("1.0", "end")
        text_result.insert("1.0", encrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

def decrypt_caesar():
    try:
        text = entry_text.get("1.0", "end-1c")
        shift = int(entry_shift.get())
        decrypted_text = caesar_cipher(text, -shift)
        text_result.delete("1.0", "end")
        text_result.insert("1.0", decrypted_text)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid shift value.")

# Vigenère Cipher functions
def encrypt_vigenere():
    text = entry_text.get("1.0", "end-1c")
    key = entry_shift.get()
    encrypted_text = vigenere_cipher(text, key)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", encrypted_text)

def decrypt_vigenere():
    text = entry_text.get("1.0", "end-1c")
    key = entry_shift.get()
    decrypted_text = vigenere_cipher(text, key, mode="decrypt")
    text_result.delete("1.0", "end")
    text_result.insert("1.0", decrypted_text)

# AES Encryption/Decryption functions
def encrypt_aes():
    text = entry_text.get("1.0", "end-1c")
    password = entry_shift.get()
    encrypted_text = aes_encrypt(text, password)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", encrypted_text)

def decrypt_aes():
    text = entry_text.get("1.0", "end-1c")
    password = entry_shift.get()
    decrypted_text = aes_decrypt(bytes.fromhex(text), password)
    text_result.delete("1.0", "end")
    text_result.insert("1.0", decrypted_text)

if __name__ == "__main__":
    root = tk.Tk()
    entry_text, entry_shift, text_result = setup_gui(root)
    root.mainloop()
