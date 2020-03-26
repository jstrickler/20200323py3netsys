#!/usr/bin/env python
from pprint import pprint

FRUITS = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

def main():
    data = read_knight_file()
    pretty_print(data)
    print()
    print(get_attribute(data, 'Robin', 3))
    print_fruit_letters()
    print_letter_counts()

def read_knight_file():
    knight_data = {}  # local name

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knight_data[name] = title, color, quest, comment
    return knight_data


def get_attribute(data, knight, attribute):
    return data[knight][attribute]


def get_fruits_by_letter():
    fruit_letters = {}
    for fruit in FRUITS:
        first_letter = fruit[0]
        if first_letter not in fruit_letters:
            fruit_letters[first_letter] = []
        fruit_letters[first_letter].append(fruit)
    return fruit_letters


def get_letter_counts():
    letter_counts = {}
    with open('DATA/words.txt') as words_in:
        for word in words_in:
            first_letter = word[0]
            if first_letter not in letter_counts:
                letter_counts[first_letter] = 0

            # letter_counts[first_letter] = letter_counts[first_letter] + 1
            letter_counts[first_letter] += 1
    return letter_counts

def pretty_print(data):
    pprint(data)
    print()

def print_fruit_letters():
    fruit_letters = get_fruits_by_letter()
    pprint(fruit_letters)
    print()

def print_letter_counts():
    letter_counts = get_letter_counts()
    pprint(letter_counts)

main()


