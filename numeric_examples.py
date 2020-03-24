#!/usr/bin/env python

i1 = 100
i2 = 0b100
i3 = 0x100
i4 = 0o100

print(i1, i2, i3, i4)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.23456e22
print()

a = 29
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)  # floored division
print(a ** b)  # a ^ b (a to the bth power)
print(a % b)  # modulo (AKA remainder after division)

#   a++ ++a a-- --a   NOT IN PYTHON!

a += 1  #  a = a + 1
b /= 4  #  b = b / 4
print(a, b)
