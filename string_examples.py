
s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"


print("Guido's the founder of Python")
print('Guido is the "BDFL" of Python')
print("""Guido's the "BDFL" of Python""")
print(s5)

actor = "Chris Hemsworth"
print(len(s1), len(actor), type(actor))

print(actor.upper())
print(actor.count('h'))
print(actor.count('worth'))
print(actor.count('H'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'))
print(actor.startswith('Liam'))
print("is" in actor)
print("ham" in actor)

print(actor.find("Hem"))
print(actor.index("Hem"))
print(actor.find("Liam"))
# print(actor.index("Liam"))

s = "      Four Strong Winds      "

print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print(s.replace(' ', ''))
print()


s = "tnggntgggnnntFour Strong Windsgtngtnngt"

print("|" + s.lstrip("gnt") + "|")
print("|" + s.rstrip("gnt") + "|")
print("|" + s.strip("gnt") + "|")
print()
print(s.replace('n', "*WOMBAT*"))

s = "Arizona:North Carolina:Ontario:Quebec"

cities = s.split(":")

print(cities)
print(cities[0])

s = "Arizona Quebec Ontario"
print(s.split())

print("=".join(cities))

#  result = STR.join(ITERABLE)
print("/".join(cities))
print("".join(cities))
