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
    chars_sorted = chars_dict_to_sorted_list(count_of_char)

    print(f"--- Begin report of {test_path} ---")
    print(f"{count_of_words} words found in the document")
    print()
    
    for item in chars_sorted:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


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


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num":num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_dict)
    return sorted_list


def sort_dict(dict):
    return dict["num"]

main()