#!/usr/bin/env python

x = 100  # global


def spam():
    y = 42  # local
    print("in y(): x is", x)
    print("in y(): y is", y)

spam()
print("in main: x is", x)
# print("in main: y is", y)

