#!/usr/bin/env python

from knight import Knight

for name in 'Arthur', 'Fred', 'Lancelot', 'Robin':
    try:
        k = Knight(name)
    except ValueError as err:
        print("****", err)
        continue

    print(f"{k.title} {k.name} ({k.color}) -- {k.quest}")
