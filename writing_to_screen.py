#!/usr/bin/env python
actor = "Chris Hemsworth"
x = 45
y = 19.3823802380

print(actor, x, y)
print(actor)
print(x)
print(y)

print(actor, x, y, sep="/")
print(actor, x, y, sep=", ")
print(actor, x, y, sep="")

print(actor, x, y, end="A")
print(x, y, end="B")
print(y)

print(actor, "is", x, "years old")  # so-so...
print("%s is %d years old" % (actor, x))  # LEGACY formatting

print("{} is {} years old".format(actor, x))  # formatting
print("{0} is {1} years old".format(actor, x))  # formatting
print("{1} is {0} years old".format(actor, x))  # formatting

print(f"{actor} is {x} years old")  # f-string

print(y)
print("y is {:.2f}".format(y))
print(f"y is {y:.2f}")

print("{:04d}".format(5))
print("{:04d}".format(199))
print("{:04d}".format(64))
