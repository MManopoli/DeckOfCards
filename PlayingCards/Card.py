from Constants import VALID_SUITS, VALID_VALUES


class Card:
    """
    Object implements a playing Card and associated errors
    """

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
        """
        Implements a string representation of the object for debugging, which
        lists both the card's value and suit.
        :return: str
        """
        return f"(value: {self.value}, suit: {self.suit})"

    def __str__(self):
        """
        Implements a string representation of the object for printing, which is
        in the format the card might be named: e.g. The Jack of Hearts
        :return: str
        """
        return f"The {self.value} of {self.suit}"

    def __eq__(self, other):
        """
        Implements equivalence for two Cards.  Two Card objects are equal if
        both are Card objects and they have the same suit and value
        :param other: Card
        :return: Boolean
        """
        if isinstance(other, Card):
            if (self.suit == other.suit) and (self.value == other.value):
                return True
        return False


class IllegalCardSuitError(Exception):
    """
    Exception for if creating a Card with an invalid suit
    """
    pass


class IllegalCardValueError(Exception):
    """
    Exception for if creating a Card with an invalid value
    """
    pass
