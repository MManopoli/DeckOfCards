from Card import Card
from Constants import VALID_VALUES, VALID_SUITS


class Deck:
    def __init__(self):
        self.cards = []
        self.generate_new_deck()

    def generate_new_deck(self):
        for suit in VALID_SUITS:
            for value in VALID_VALUES:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        # TODO:
        pass

    def dealOneCard(self):
        # TODO:
        pass

    def __str__(self):
        return f"This is a {len(self.cards)} card deck."

    def __repr__(self):
        return f"{len(self.cards)} cards: {self.cards}"


if __name__ == '__main__':
    deck = Deck()
    print(deck)
    print(repr(deck))
