#!/usr/bin/env python

from carddeck import CardDeck

class JokerDeck(CardDeck):  # JokerDeck inherits from CardDeck

    def _make_cards(self):
        super()._make_cards()
        self._cards.append('1-Joker')
        self._cards.append('2-Joker')

    def __init__(self):
        # read file....
        self._name = ...

    @property
    def name(self):
        return self._name

