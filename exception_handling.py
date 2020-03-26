#!/usr/bin/env python

try:
    with open("DATA/komododragon.txt") as komodo_in:
        pass
except FileNotFoundError as err:
    print(type(err))
    print(err)

junk = [1, 2, 3, 4]
try:
    print(junk[10])
    print("wombat")
    x = 5
except IndexError as err:
    print(err)

values = 2, 9.7, 0.0, 8.4, "123", 3.1

for v in values:
    try:
        result = 11 / v
    except ZeroDivisionError as err:
        print(err)
    except TypeError as wombat:
        print(wombat)
    except Exception as err:
        print(err)
    else:
        print(result)
    finally:
        print("X")




print("All finished.")
