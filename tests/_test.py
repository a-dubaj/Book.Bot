# tests/test_main.py

from main import get_num_words, get_chars_dict, chars_dict_to_sorted_list


def test_get_num_words():
    text = "Hello world"
    assert get_num_words(text) == 2


def test_get_chars_dict():
    text = "Hello"
    expected_dict = {"h": 1, "e": 1, "l": 2, "o": 1}
    assert get_chars_dict(text) == expected_dict


def test_chars_dict_to_sorted_list():
    chars_dict = {"h": 1, "e": 1, "l": 2, "o": 1}
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    expected_list = [
        {"char": "l", "num": 2},
        {"char": "h", "num": 1},
        {"char": "e", "num": 1},
        {"char": "o", "num": 1},
    ]
    assert sorted_list == expected_list
