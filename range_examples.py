#!/usr/bin/env python

r = range(1, 11)

print(r)

for i in range(1, 11):
    print(i)
print()

#  range(start, stop)
#  range(stop)  # assumes start is 0
#  range(start, stop, step)

for _ in range(5):
    print("We love Python!")
print()

for i in range(5, 101, 5):
    print(i, end=' ')
print('\n')
