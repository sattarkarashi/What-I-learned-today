import collections
from random import choice, shuffle  
"""
Dunder methods are special methods that are called by Python when you use certain syntax.
They are always surrounded by double underscores, hence the name.
"""
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


# Add sorting to the deck
def spades_high(card):
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    print()
    return rank_value * len(suit_values) + suit_values[card.suit]

deck = FrenchDeck()
print(sorted(deck, key=spades_high))

# Adding the shuffle method
def set_card(deck, position, card):
    deck._cards[position] = card

FrenchDeck.__setitem__ = set_card
deck = FrenchDeck()
shuffle(deck)
print(deck[:5])

# Mathemtical operations and dunder methods

from math import hypot
class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'

    def __abs__(self):  
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# By default, instance of user defined classes are considered True unless either __bool__ or __len__ is implemented.
# bool() calls x.__bool__() and uses the result. If __bool__ is not implemented, Python tries to invoke x.__len__(),
#  and if that returns zero, bool returns False. Otherwise, bool returns True.

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1, v2)
print(v1 + v2)
