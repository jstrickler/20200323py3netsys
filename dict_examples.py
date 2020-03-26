
d1 = dict()
d2 = {'bird': 5, 'parrot': 8, 'wildebeest': 2}
d3 = {}

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['YOW'], airports['SFO'])
print(airports.get("RDU", "Not found"))
print(airports.get("PHX", "Not found"))
print(airports.get("PHX"))

print(len(airports))
for abbr in 'RDU', 'PHX', 'LAX', 'ELM', 'YYZ':
    print(abbr, abbr in airports)
print()

print(airports.keys())
print(airports.values())

del airports['EWR']

print(airports, '\n')

print(airports.items(), '\n')

for abbr, name in airports.items():
    print(abbr, name)
print()

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

