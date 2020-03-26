#!/usr/bin/env python
from carddeck import CardDeck
from jokerdeck import JokerDeck

d1 = CardDeck('Seth')
d2 = CardDeck('James')

print(d1, d2)

print(d1.get_dealer())

print(d1.dealer)

d1.dealer = 'Clare'  # CardDeck.dealer(d1, 'Clare')

print(d1.dealer)

try:
    d1.dealer = 1234
except TypeError as err:
    print(err)

print(d1.dealer)

d1.shuffle()

print(d1.cards)


for i in range(7):
    print(d1.draw())

print(d1.get_ranks())
print(CardDeck.get_ranks())

CardDeck.bark()

j1 = JokerDeck("Jimmy")
j1.shuffle()
print(j1.cards)
print(j1)

print(len(j1), len(d1), len(d2))

print(d1 + j1)

x = str(d1)
print(x)

print(j1, d1, d2)
