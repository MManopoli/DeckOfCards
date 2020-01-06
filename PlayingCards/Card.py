from Constants import VALID_SUITS, VALID_VALUES

class Card:
    def __init__(self, suit, value):
        # Validate and set the card's suit
        if suit in VALID_SUITS:
            self.suit = suit
        else:
            raise IllegalCardSuitError("A playing card must have one of the "
                                        "following suits: " + ', '.join(
                                            VALID_SUITS
                                  ))

        # Validate and set the card's value
        if value in VALID_VALUES:
            self.value = value
        else:
            raise IllegalCardValueError("A playing card must have one of the "
                                        "following values: " + ', '.join(
                                            VALID_VALUES
                                        ))

    def __repr__(self):
        return (f"(value: {self.value}, suit: {self.suit})")

    def __str__(self):
        return (f"The {self.value} of {self.suit}")


class IllegalCardSuitError(Exception):
    pass


class IllegalCardValueError(Exception):
    pass


if __name__ == "__main__":
    card = Card(suit='hearts', value='Ace')
    print(card)
    print(repr(card))

    try:
        bad_card = Card(suit='notasuit', value='Ace')
    except IllegalCardSuitError:
        print("IllegalCardSuitError successfully triggered")
        pass

    try:
        bad_card = Card(suit='spades', value='Turkey')
    except IllegalCardValueError:
        print("IllegalCardValueError successfully triggered")
        pass
