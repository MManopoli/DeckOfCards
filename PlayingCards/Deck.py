from Card import Card
from Constants import VALID_VALUES, VALID_SUITS
import random


class Deck:
    def __init__(self):
        self.cards = []
        self.construct_new_full_deck()

    def construct_new_full_deck(self):
        for suit in VALID_SUITS:
            for value in VALID_VALUES:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        deck_size = len(self.cards)
        for i in range(deck_size - 1, 0, -1):
            r_int = random.randint(0, i)
            self.cards[i], self.cards[r_int] = self.cards[r_int], self.cards[i]

    def dealOneCard(self):
        return self.cards.pop(0)


    def __str__(self):
        return f"This is a {len(self.cards)} card deck."

    def __repr__(self):
        return f"{len(self.cards)} cards: {self.cards}"

    def __eq__(self, other):
        if isinstance(other, Deck):
            if self.cards == other.cards:
                return True
        return False

    def __len__(self):
        return len(self.cards)
