#!/usr/bin/env python
import shutil  # portable OS commands for copy, rename, move, delete
import os  # tools to work with OS (files, etc....)

# f = open("myfile")
# ...
# f.close()

# process one line at a time without \n
i = 0
with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()  # remove \n \r \t ' ' etc etc
        print(i, line)
        i += 1
print('-' * 60)
# absolute path on Windows starts with C:\ \\foo \\bar E:\   etc etc
# abs path on non-Windows starts with /

# process while file with embedded newlines
with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("normal:")
    print(contents)
    print("raw:")
    print(repr(contents))
print('-' * 60)

# get list of lines with newlines
with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)

# get list of lines without newlines
with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

bird_count = 0
with open('DATA/parrot.txt') as parrot_in:
    for line in parrot_in:
        bird_count += line.count("the")
print("bird count:", bird_count)
print('-' * 60)

target_word = 'parrot'
with open('DATA/parrot.txt') as parrot_in:
    for raw_line in parrot_in:
        single_line_count = raw_line.count(target_word)
        if single_line_count:
            line = raw_line.rstrip()
            print(single_line_count, line)
print('-' * 60)

q_words = []
with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        if raw_line.startswith('q'):
            q_words.append(raw_line.rstrip())
print(q_words)
print(len(q_words))
print('-' * 60)

with open('DATA/words.txt') as words_in:
    with open('qwords.txt', 'w') as q_words_out:
        for raw_line in words_in:
            if raw_line.startswith('q'):
                q_words_out.write(raw_line)


colors = ["red", "blue", "green", "yellow", "brown", "black"]

with open('DATA/colors.txt', 'w') as colors_out:
    for color in colors:
        colors_out.write(color + '\n')

shutil.copy('DATA/alice.txt', 'betsy.txt')

os.remove('betsy.txt')   # or os.unlink(...)
