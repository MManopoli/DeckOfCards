class Card:

    # Private (name scrambled) list of valid card values
    __valid_values = [
        'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen',
        'King'
    ]

    # Private (name scrambled) list of valid card suits
    __valid_suits = ['hearts', 'spades', 'clubs', 'diamonds']

    def __init__(self, suit, value):
        # Validate and set the card's suit
        if suit in self.__valid_suits:
            self.suit = suit
        else:
            raise IllegalCardSuitError("A playing card must have one of the "
                                        "following suits: " + ', '.join(
                                            self.__valid_suits
                                  ))

        # Validate and set the card's value
        if value in self.__valid_values:
            self.value = value
        else:
            raise IllegalCardValueError("A playing card must have one of the "
                                        "following values: " + ', '.join(
                                            self.__valid_values
                                        ))

    def __repr__(self):
        return (f"value: {self.value}, suit: {self.suit}")

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
