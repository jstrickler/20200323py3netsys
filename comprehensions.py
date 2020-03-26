#!/usr/bin/env python

colors = ["red", "blue", "green", "yellow", "brown", "black"]

c0 = []
for c in colors:
    c0.append(c.upper())
print("c0:", c0, '\n')

c1 = [c.upper() for c in colors]
print("c1:", c1, '\n')

#  [EXPR for VAR ... in ITERABLE if CONDITION]

c2 = [c.upper() for c in colors if c.startswith('b')]
print("c2:", c2, '\n')

c3 = [c for c in colors if c.startswith('b')]
print("c3:", c3, '\n')

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = [i * 10 for i in nums]
print("n1:", n1, '\n')

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [p[1] for p in people]
print("last_names:", last_names, '\n')

color_gen = (c.upper() for c in colors)

print(color_gen)
for color in color_gen:
    print(color)
print()

