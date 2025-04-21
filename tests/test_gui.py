# test_gui.py

import unittest
from src.gui import encrypt_caesar, decrypt_caesar, encrypt_vigenere, decrypt_vigenere

class TestGUI(unittest.TestCase):
    def test_encrypt_caesar(self):
        self.assertEqual(encrypt_caesar("abc", 3), "def")

    def test_decrypt_caesar(self):
        self.assertEqual(decrypt_caesar("def", 3), "abc")

    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("hello", "key"), "riijm")

    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("riijm", "key"), "hello")

if __name__ == "__main__":
    unittest.main()
