#!/usr/bin/env python
w = "123"  # string
x = [1, 2, 3]   # list
y = {1, 2, 3}   # set
z1 = 1, 2, 3  # tuple
z2 = (1, 2, 3) # tuple

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'   # tuple

print(person[0], person[1])

first_name = person[0]
last_name = person[1]
product = person[2]
dob = person[3]

first_name, last_name, product, dob = person  # unpack the tuple into variables

place = ['Scottsdale', 'AZ']

city, state = place

print(city, state)

provence = 'Quebec'

a, b, c, d, e, f = provence

print(a, b, c, d, e, f)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git',  '1969-12-28'),
    ('John', 'Strickler', '1956-10-31'),
]

for person in people:
    # person = next(people)
    print(person)
print('-' * 60)

for first_name, last_name, *product, dob in people:
    # first_name, last_name, product, dob = next(people)
    print(first_name, last_name, product)
print('-' * 60)

cities = [('Montreal', 'QC'), ('Victoria', 'BC'), ('St. John', 'NL'), ('Calgary', 'AL')]

for city, provence in cities:
    print("{} is in {}".format(city, provence))
print()

values = 'one', 'two', 'three', 'four', 'five', 'six'

a, b, *c = values
print(a, b, c)
a, *b, c = values
print(a, b, c)
*a, b, c = values
print(a, b, c)
