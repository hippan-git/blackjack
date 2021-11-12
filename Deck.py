from const import *
from random import shuffle


class Card:
    def __init__(self, suit, point):
        self.suit = suit
        self.points = point
        self.picture = None

    def __str__(self):
        message = f"{self.suit} point {self.points}"
        return message


class Deck:
    def __init__(self):
        self.cards = self.__create_deck()
        shuffle(self.cards)

    def __create_deck(self):
        cards = []
        for s in SUITS:
            for r, p in RANKS.items():
                cards.append(Card(r + " " + s, p))
        return cards

    def get_card(self):
        return self.cards.pop(0)

    def __len__(self):
        return len(self.cards)