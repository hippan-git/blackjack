from const import *
class Card:
    def __init__(self, suit, point):
        self.sult = suit
        self.points = point
        self.picture = None



class Deck:
    def __init__(self):
        self.cards = []

    def create_deck(self):
        print(SUITS)
        for s in SUITS:
            for r, p in RANKS.items():
                self.cards.append(Card(r+" "+s, p))
        print(RANKS)
