"""Module implements a deck of playing cards"""

from Card import Card
from Constants import VALID_VALUES, VALID_SUITS
import random


class Deck:
    def __init__(self):
        """
        Constructs a new deck containing 52 cards in a non-random order
        """
        self.cards = []
        self.construct_new_full_deck()

    def construct_new_full_deck(self):
        """
        Resets the deck, re-creating all 52 cards in the original non-random
        order
        :return: None
        """
        self.cards = []
        for suit in VALID_SUITS:
            for value in VALID_VALUES:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        """
        Randomly shuffles all cards currently in the deck
        :return: None
        """
        deck_size = len(self.cards)
        for i in range(deck_size - 1, 0, -1):
            r_int = random.randint(0, i)
            self.cards[i], self.cards[r_int] = self.cards[r_int], self.cards[i]

    def dealOneCard(self):
        """
        Removes the first Card object in the deck and returns it
        :return: Card
        """
        return self.cards.pop(0)

    def __str__(self):
        """
        Implements the string representation of the deck object; which gives the
        number of cards in the deck
        :return: str
        """
        return f"This is a {len(self.cards)} card deck."

    def __repr__(self):
        """
        Implements a string representation of the deck object for debugging;
        which lists both the count of Cards and each Card in order
        :return: str
        """
        return f"{len(self.cards)} cards: {self.cards}"

    def __eq__(self, other):
        """
        Establishes that both objects are instances of Deck and that the Cards
        in each Deck are equivalent and that they appear in the same order
        :param other: Deck
        :return: Boolean
        """
        if isinstance(other, Deck):
            if self.cards == other.cards:
                return True
        return False

    def __len__(self):
        """
        The length of a deck is defined as the number of cards in the deck
        :return: int
        """
        return len(self.cards)
