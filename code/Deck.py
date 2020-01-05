from Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.generate_new_deck()

    def generate_new_deck(self):
        for suit in Card.valid_suits:
            for value in Card.valid_values:
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
