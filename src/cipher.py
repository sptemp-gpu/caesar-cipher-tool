# cipher.py

from Crypto.Cipher import AES
import string
import random

# Caesar Cipher
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - shift_amount) % 26 + shift_amount)
        else:
            result += char
    return result

# Vigenère Cipher
def vigenere_cipher(text, key, mode="encrypt"):
    result = []
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)].lower()) - 97
            if mode == "decrypt":
                shift = -shift
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# AES Encryption & Decryption
def aes_encrypt(text, password):
    key = password.encode('utf-8')[:32]  # AES needs 16, 24, or 32 bytes key length
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return cipher.nonce + tag + ciphertext

def aes_decrypt(ciphertext, password):
    key = password.encode('utf-8')[:32]
    nonce, tag, ciphertext = ciphertext[:16], ciphertext[16:32], ciphertext[32:]
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')
