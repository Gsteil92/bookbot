"""
Project Name: Bookbot
Author: George Steil
Creation Date: 10/14/2024
"""

# Global Variables
book_path = "books/frankenstein.txt"
test_path = "books/test_count.txt"



# Functions
def main():
    text = get_book_text(book_path)
    count_of_words = word_count(text)
    count_of_char = char_count(text)
    print(f"THIS IS THE COUNT OF WORDS: {count_of_words}")
    print(f"THIS IS THE COUNT OF CHARACTERS: {count_of_char}")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    w = 0
    while w < len(words):
        w = w + 1

    return w


def char_count(text):
    lowered_string = text.lower()
    chars_dict = {}
    for char in lowered_string:
        if char in chars_dict:
            chars_dict[char] += 1
        else:
            chars_dict[char] = 1
    return chars_dict


main()