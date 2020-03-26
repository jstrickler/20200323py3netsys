
colors = ["red", "blue", "green", "yellow", "brown", "black"]

for color in colors:
    print(color)
print('-' * 60)

for i, color in enumerate(colors):
    print(i, color)
print('-' * 60)

e = enumerate(colors)
print(list(e), '\n')
print(list(e), '\n')

for i, color in enumerate(colors, 1000):
    print(i, color)
print('-' * 60)
