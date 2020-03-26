import random

class CardDeck:  # inherits from object
    SUITS = 'Clubs Diamonds Hearts Spades'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self, dealer):
        self.dealer = dealer
        self._make_cards()

    def _make_cards(self):
        self._cards = []
        for suit in self.SUITS:
            for rank in self.RANKS:
                card = f"{rank}-{suit}"
                self._cards.append(card)

    @property
    def cards(self):
        return self._cards

    def draw(self):  # instance method
        return self._cards.pop(0)

    def shuffle(self):  # instance method
        random.shuffle(self._cards)

    # not the best practice!
    def get_dealer(self):  # getter method
        return self._dealer

    @property
    def dealer(self):   # getter property
        return self._dealer

    @dealer.setter
    def dealer(self, dealer):  # setter property
        if isinstance(dealer, str):
            self._dealer = dealer
        else:
            raise TypeError("Dealer must be a string")

    @classmethod
    def get_ranks(cls):
        return cls.RANKS

    @staticmethod
    def bark():
        print("Woof! woof")

    def __len__(self):
        return len(self._cards)

    def __add__(self, other):
        return 42

    def __str__(self):  # user-friendly representation
        my_name = type(self).__name__
        return f"{my_name}({self.dealer},{len(self)})"
