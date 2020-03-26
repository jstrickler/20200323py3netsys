#!/usr/bin/env python

limit = 101

is_prime = [True] * limit

for n in range(2, limit):
    if is_prime[n]:
        print(n, end=' ')
        for m in range(2 * n, limit, n):
            is_prime[m] = False
print()
