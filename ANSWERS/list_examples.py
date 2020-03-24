#!/usr/bin/env python

list1 = list()
list2 = ['apple', 'banana', 'mango']
list3 = []
list4 = 'fee:fi:fo:fum'.split(':')
print(list4)

dogs = ['mutt', 'pug', 'poodle', 'rottweiler', 'German shepherd']

print(dogs, len(dogs))
print(dogs[0], dogs[3], dogs[-1])
print(dogs[-2], dogs[-5])
print(dogs[-3], dogs[len(dogs)-3])

dogs.append('sharpei')
dogs.append('Javanese')
dogs.append('chihuahua')
print(dogs, '\n')

dogs.insert(0, 'English shepherd')
dogs.insert(3, 'Springer spaniel')
print(dogs, '\n')

more_pooches = ['Schnauzer', 'akita', 'golden retriever']

dogs.extend(more_pooches)

print(dogs, '\n')

dogs[1] = "Heinz 57"

print(dogs, '\n')

# dogs[99] = 'chesapeake bay retriever'   INVALID

del dogs[3]   # remove...

print(dogs, '\n')

x = dogs.pop()
print(x)
print(dogs, '\n')

x = dogs.pop(1)
print(x)
print(dogs, '\n')

dogs.remove('sharpei')
print(dogs, '\n')

#  del  remove completely
#  pop(n)  remove but keep value
#  .remove(xxxx) remove by value

dogs.reverse()
print(dogs, '\n')

dogs.sort()
print(dogs, '\n')

print(dogs, '\n')

print(dogs[0:3])
print(dogs[2:5])
print(dogs[6:9])

print(dogs[:3])
print(dogs[5:])

actor = "William Powell"
print(actor[:4])
print(actor[8:11])
print(actor[-6:])

print(f"{actor[:4]}.{actor[4:5]}.{actor[5:7]}")

print(dogs, '\n')

for dog in dogs:
    print(dog.upper())
print()

udogs = []
for dog in dogs:
    udogs.append(dog.upper())
print(udogs)

# for VAR in ITERABLE:
#    ....

for char in actor:
    print(char)

