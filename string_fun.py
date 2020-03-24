#!/usr/bin/env python

full_name = input("Enter full name: ")

print("as is:", full_name)
print("upper:", full_name.upper())
print("title:", full_name.title())
print("#js:", full_name.lower().count('j'))
print("length:", len(full_name))
print("index of 'jacob':", full_name.lower().index('jacob'))
