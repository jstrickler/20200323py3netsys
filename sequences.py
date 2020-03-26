#!/usr/bin/python3

ctemps = [-40, 0, 37, 75, 100]

fruits = [
    '    MANGO', 'Apple', '   peach   ', 'PLUM   ', '  Apricot',
    'BaNaNa', 'Persimmon   '
]

for ctemp in ctemps:
    ftemp = ((9 * ctemp) / 5) + 32
    print("{} is {}".format(ctemp, ftemp))
