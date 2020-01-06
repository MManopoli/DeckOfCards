from pathlib import Path
import sys

path = str(Path(__file__).parent.parent) + '/PlayingCards'
sys.path.append(path)

print(path)

from Card import Card, IllegalCardSuitError, IllegalCardValueError
from Deck import Deck
from nose.tools import raises

def test_create_card():
    card = Card(suit='Hearts', value='Ace')
    assert str(card) == "The Ace of Hearts"
    assert repr(card) == "(value: Ace, suit: Hearts)"

@raises(IllegalCardSuitError)
def test_bad_suit():
    Card(suit='NotASuit', value='Ace')
    assert False

@raises(IllegalCardValueError)
def test_bad_value():
    Card(suit='Spades', value='NotAValue')
    assert False