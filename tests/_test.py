# tests/test_main.py

import unittest
from unittest.mock import patch, mock_open, MagicMock
from main import get_num_words, get_chars_dict, chars_dict_to_sorted_list, get_book_text, sort_on

class TestMain(unittest.TestCase):

    def test_get_num_words(self):
        text = "Hello world"
        self.assertEqual(get_num_words(text), 2)

    def test_get_chars_dict(self):
        text = "Hello"
        expected_dict = {"h": 1, "e": 1, "l": 2, "o": 1}
        self.assertEqual(get_chars_dict(text), expected_dict)

    def test_chars_dict_to_sorted_list(self):
        chars_dict = {"h": 1, "e": 1, "l": 2, "o": 1}
        sorted_list = chars_dict_to_sorted_list(chars_dict)
        expected_list = [
            {"char": "l", "num": 2},
            {"char": "h", "num": 1},
            {"char": "e", "num": 1},
            {"char": "o", "num": 1},
        ]
        self.assertEqual(sorted_list, expected_list)

    @patch("builtins.open", new_callable=mock_open, read_data="sample text")
    def test_get_book_text(self, mock_file):
        path = "books/frankenstein.txt"
        text = get_book_text(path)
        self.assertEqual(text, "sample text")
        mock_file.assert_called_with(path, "r", encoding="utf-8")

    def test_get_num_words_empty_text(self):
        text = ""
        self.assertEqual(get_num_words(text), 0)

    def test_get_chars_dict_empty_text(self):
        text = ""
        expected_dict = {}
        self.assertEqual(get_chars_dict(text), expected_dict)

    def test_chars_dict_to_sorted_list_empty_dict(self):
        chars_dict = {}
        sorted_list = chars_dict_to_sorted_list(chars_dict)
        expected_list = []
        self.assertEqual(sorted_list, expected_list)

    def test_sort_on_identical_values(self):
        dict_list = [{"char": "a", "num": 1}, {"char": "b", "num": 1}, {"char": "c", "num": 1}]
        sorted_list = sorted(dict_list, key=sort_on, reverse=True)
        expected_list = [{"char": "a", "num": 1}, {"char": "b", "num": 1}, {"char": "c", "num": 1}]
        self.assertEqual(sorted_list, expected_list)

    def test_sort_on_large_values(self):
        dict_list = [{"char": "a", "num": 1000}, {"char": "b", "num": 500}, {"char": "c", "num": 2000}]
        sorted_list = sorted(dict_list, key=sort_on, reverse=True)
        expected_list = [{"char": "c", "num": 2000}, {"char": "a", "num": 1000}, {"char": "b", "num": 500}]
        self.assertEqual(sorted_list, expected_list)

    @patch("builtins.open", side_effect=FileNotFoundError)
    def test_get_book_text_file_not_found(self, mock_file):
        path = "books/nonexistent.txt"
        with self.assertRaises(FileNotFoundError):
            get_book_text(path)

if __name__ == '__main__':
    unittest.main()
