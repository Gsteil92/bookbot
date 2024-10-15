"""
Project Name: Bookbot
Author: George Steil
Creation Date: 10/14/2024
"""

# Global Variables
book_path = "books/frankenstein.txt"
test_path = "books/test_count.txt"

def main():
    text = get_book_text(book_path)
    count_of_words = word_count(text)
    print(count_of_words)


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()


def word_count(text):
    words = text.split()
    w = 0
    while w < len(words):
        w = w + 1

    return w



main()