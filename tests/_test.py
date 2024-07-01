import unittest
from unittest.mock import patch, mock_open
from main import get_num_words, get_chars_dict, chars_dict_to_sorted_list, get_book_text

short_text = """I see by your eagerness and the wonder and hope which your eyes express, my friend, that you expect to be informed of the secret with which I am acquainted; that cannot be; listen patiently until the end of my story, and you will easily perceive why I am reserved upon that subject."""
long_text = """I see by your eagerness and the wonder and hope which your eyes express, my friend, that you expect to be informed of the secret with which I am acquainted; that cannot be; listen patiently until the end of my story, and you will easily perceive why I am reserved upon that subject.  I will not lead you on, unguarded and ardent as I then was, to your destruction and infallible misery.  Learn from me, if not by my precepts, at least by my example, how dangerous is the acquirement of knowledge and how much happier that man is who believes his native town to be the world, than he who aspires to become greater than his nature will allow.

When I found so astonishing a power placed within my hands, I hesitated a long time concerning the manner in which I should employ it."""

class TestMain(unittest.TestCase):

    def test_get_num_words(self):
        text = short_text
        self.assertEqual(get_num_words(text), 53)  # Zaktualizowana wartość

    def test_chars_dict_to_sorted_list(self):
        chars_dict = {"a": 3, "b": 2, "c": 1}
        sorted_list = chars_dict_to_sorted_list(chars_dict)
        expected_list = [
            {"char": "a", "num": 3},
            {"char": "b", "num": 2},
            {"char": "c", "num": 1}
        ]
        self.assertEqual(sorted_list, expected_list)

    def test_get_chars_dict(self):
        text = "aAaBbC"
        expected_dict = {'a': 3, 'b': 2, 'c': 1}
        self.assertEqual(get_chars_dict(text), expected_dict)

    @patch("builtins.open", new_callable=mock_open, read_data=short_text)
    def test_get_book_text(self, mock_file):
        path = "books/frankenstein.txt"
        text = get_book_text(path)
        expected_text = short_text
        self.assertEqual(text, expected_text)
        mock_file.assert_called_with(path, "r", encoding="utf-8")

    def test_get_num_words_long_text(self):
        text = long_text
        self.assertEqual(get_num_words(text), 145)  # Zaktualizowana wartość

    def test_get_chars_dict_long_text(self):
        text = long_text
        expected_dict = {
            'i': 46, ' ': 145, 's': 32, 'e': 78, 'b': 10, 'y': 13, 'o': 24, 'u': 30,
            'r': 34, 'a': 41, 'g': 14, 'n': 33, 'd': 19, 't': 51, 'h': 29, 'w': 15,
            'f': 14, 'c': 10, 'q': 4, 'p': 6, 'l': 16, 'm': 15, ',': 7, ';': 4, '.': 2
        }
        self.assertEqual(get_chars_dict(text), expected_dict)

    def test_chars_dict_to_sorted_list_long_text(self):
        chars_dict = {'i': 46, ' ': 145, 's': 32, 'e': 78, 'b': 10, 'y': 13, 'o': 24, 'u': 30,
                      'r': 34, 'a': 41, 'g': 14, 'n': 33, 'd': 19, 't': 51, 'h': 29, 'w': 15,
                      'f': 14, 'c': 10, 'q': 4, 'p': 6, 'l': 16, 'm': 15, ',': 7, ';': 4, '.': 2}
        sorted_list = chars_dict_to_sorted_list(chars_dict)
        expected_list = [
            {'char': ' ', 'num': 145},
            {'char': 'e', 'num': 78},
            {'char': 't', 'num': 51},
            {'char': 'a', 'num': 41},
            {'char': 'i', 'num': 46},
            {'char': 'r', 'num': 34},
            {'char': 'n', 'num': 33},
            {'char': 's', 'num': 32},
            {'char': 'u', 'num': 30},
            {'char': 'h', 'num': 29},
            {'char': 'o', 'num': 24},
            {'char': 'd', 'num': 19},
            {'char': 'l', 'num': 16},
            {'char': 'm', 'num': 15},
            {'char': 'w', 'num': 15},
            {'char': 'y', 'num': 13},
            {'char': 'g', 'num': 14},
            {'char': 'f', 'num': 14},
            {'char': 'c', 'num': 10},
            {'char': 'b', 'num': 10},
            {'char': ',', 'num': 7},
            {'char': 'p', 'num': 6},
            {'char': 'q', 'num': 4},
            {'char': ';', 'num': 4},
            {'char': '.', 'num': 2}
        ]
        self.assertEqual(sorted_list, expected_list)

if __name__ == '__main__':
    unittest.main()
