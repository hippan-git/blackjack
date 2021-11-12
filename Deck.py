from const import *


class Card:
    sult = ''
    points = None
    picture = None


class Deck:
    def __init__(self):
        self.cards = []

    def _create_deck(self):
        print(SUITS)
        print(RANKS)
