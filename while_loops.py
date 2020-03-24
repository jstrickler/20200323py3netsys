
i = 0
while i < 3:
    print(i)
    i += 1
print()

# True, False

while True:
    name = input("What is your name? (or q to quit) ")
    if name == 'q':
        break  # exit loop
    if name == '':
        continue  # go to top
    print("Hello,", name)

