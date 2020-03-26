#!/usr/bin/env python

phil_countries = ['UK', 'India', 'Bulgaria', 'Spain', 'Burkina Faso',
    'France', 'Thailand', 'El Salvador', 'India', 'India']

bill_countries = ['Togo', 'South Africa', 'Burkina Faso', 'France', 'Spain',
    'Kazakhstan', 'UK']



phil = set(phil_countries)
bill = set(bill_countries)

bill.add("Luxembourg")
phil.add("Greece")
phil.add("Serbia")



print(phil)
print(bill)
print()

print("Both:", phil & bill)  # intersection
print("Just one:", phil ^ bill)   # Xor (AKA symmetric difference)
print("All:", phil | bill)   # union
print("Just Phil:", phil - bill)
print("Just Bill:", bill - phil)

