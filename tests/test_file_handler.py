# test_file_handler.py

import unittest
from src.file_handler import save_to_file, load_from_file
from io import StringIO
from unittest.mock import patch

class TestFileHandler(unittest.TestCase):
    def test_save_to_file(self):
        with patch('builtins.open', unittest.mock.mock_open()) as mocked_file:
            save_to_file("test.txt", "This is a test.")
            mocked_file.assert_called_with("test.txt", "w")

    def test_load_from_file(self):
        with patch('builtins.open', unittest.mock.mock_open(read_data="This is a test.")):
            result = load_from_file("test.txt")
            self.assertEqual(result, "This is a test.")

if __name__ == "__main__":
    unittest.main()
