# test_cipher.py

import unittest
from cipher import caesar_cipher, vigenere_cipher, aes_encrypt, aes_decrypt

class TestCipherAlgorithms(unittest.TestCase):
    def test_caesar_cipher(self):
        self.assertEqual(caesar_cipher("abc", 3), "def")
        self.assertEqual(caesar_cipher("xyz", -3), "uvw")

    def test_vigenere_cipher(self):
        self.assertEqual(vigenere_cipher("hello", "key"), "riijm")
        self.assertEqual(vigenere_cipher("riijm", "key", mode="decrypt"), "hello")

    def test_aes_encryption(self):
        password = "mysecretpassword"
        text = "hello world"
        encrypted = aes_encrypt(text, password)
        decrypted = aes_decrypt(encrypted, password)
        self.assertEqual(decrypted, text)

if __name__ == "__main__":
    unittest.main()
