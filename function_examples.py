#!/usr/bin/env python

def get_message():
    return "Hello Python World!"

x = get_message()
y = get_message()

print("printing messages:", x, y)

def print_message():
    msg = get_message()
    print(msg)

print_message()

def avg(a, b):
    return (a + b) / 2

print(avg(10, 28))
print(avg(5, 1000000))

print(avg(28, 10))

# foo(file_name='bar.txt', count=25)

def better_avg(*nums):
    if len(nums) == 0:
        return 0

    total = 0
    for num in nums:
        total += num

    return total / len(nums)

print(better_avg(10, 28))
print(better_avg(10, 28, 13, 5, 8, 47))
print(better_avg(10))
print(better_avg())
print('-' * 60)

def whoopee(a, b, *c):
    print(a)
    print(b)
    print(c)
    print('==')

whoopee(1, 2)
whoopee(1, 2, 3, 4, 5, 6)


