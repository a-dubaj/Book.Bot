import unittest
from unittest.mock import patch, mock_open
from main import get_num_words, get_chars_dict, chars_dict_to_sorted_list, get_book_text

short_text = """I see by your eagerness and the wonder and hope which your eyes express, my friend, that you expect to be informed of the secret with which I am acquainted; that cannot be; listen patiently until the end of my story, and you will easily perceive why I am reserved upon that subject."""
long_text = """I see by your eagerness and the wonder and hope which your eyes express, my friend, that you expect to be informed of the secret with which I am acquainted; that cannot be; listen patiently until the end of my story, and you will easily perceive why I am reserved upon that subject.  I will not lead you on, unguarded and ardent as I then was, to your destruction and infallible misery.  Learn from me, if not by my precepts, at least by my example, how dangerous is the acquirement of knowledge and how much happier that man is who believes his native town to be the world, than he who aspires to become greater than his nature will allow.

When I found so astonishing a power placed within my hands, I hesitated a long time concerning the manner in which I should employ it."""

class TestMain(unittest.TestCase):

    def test_get_num_words(self):
        text = short_text
        self.assertEqual(get_num_words(text), 50)

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
        self.assertEqual(get_num_words(text), 122)

    def test_get_chars_dict_long_text(self):
        text = long_text
        expected_dict = {
            'i': 23, ' ': 109, 's': 33, 'e': 64, 'b': 5, 'y': 15, 'o': 16, 'u': 20,
            'r': 22, 'a': 26, 'g': 11, 'n': 22, 'd': 18, 't': 33, 'h': 19, 'w': 9,
            'f': 7, 'c': 8, 'q': 3, 'p': 8, 'l': 9, 'm': 9, ',': 7, ';': 5, '.': 4
        }
        self.assertEqual(get_chars_dict(text), expected_dict)

    def test_chars_dict_to_sorted_list_long_text(self):
        chars_dict = {'i': 23, ' ': 109, 's': 33, 'e': 64, 'b': 5, 'y': 15, 'o': 16, 'u': 20,
                      'r': 22, 'a': 26, 'g': 11, 'n': 22, 'd': 18, 't': 33, 'h': 19, 'w': 9,
                      'f': 7, 'c': 8, 'q': 3, 'p': 8, 'l': 9, 'm': 9, ',': 7, ';': 5, '.': 4}
        sorted_list = chars_dict_to_sorted_list(chars_dict)
        expected_list = [
            {'char': ' ', 'num': 109},
            {'char': 'e', 'num': 64},
            {'char': 's', 'num': 33},
            {'char': 't', 'num': 33},
            {'char': 'a', 'num': 26},
            {'char': 'i', 'num': 23},
            {'char': 'r', 'num': 22},
            {'char': 'n', 'num': 22},
            {'char': 'u', 'num': 20},
            {'char': 'h', 'num': 19},
            {'char': 'd', 'num': 18},
            {'char': 'o', 'num': 16},
            {'char': 'y', 'num': 15},
            {'char': 'g', 'num': 11},
            {'char': 'w', 'num': 9},
            {'char': 'l', 'num': 9},
            {'char': 'm', 'num': 9},
            {'char': 'c', 'num': 8},
            {'char': 'p', 'num': 8},
            {'char': 'f', 'num': 7},
            {'char': ',', 'num': 7},
            {'char': 'b', 'num': 5},
            {'char': ';', 'num': 5},
            {'char': 'q', 'num': 3},
            {'char': '.', 'num': 4}
        ]
        self.assertEqual(sorted_list, expected_list)

if __name__ == '__main__':
    unittest.main()
