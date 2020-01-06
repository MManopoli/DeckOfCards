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

def test_card_equivalence():
    card1 = Card(suit='Hearts', value='Ace')
    card2 = Card(suit='Hearts', value='Ace')
    assert card1 == card2

@raises(IllegalCardSuitError)
def test_bad_suit():
    Card(suit='NotASuit', value='Ace')
    assert False

@raises(IllegalCardValueError)
def test_bad_value():
    Card(suit='Spades', value='NotAValue')
    assert False

def test_create_unshuffled_deck():
    deck = Deck()
    assert str(deck) == "This is a 52 card deck."
    assert str(deck.dealOneCard()) == "The Ace of Hearts"

def test_deck_equivalence():
    deck1 = Deck()
    deck2 = Deck()
    assert deck1 == deck2

def test_create_and_shuffle_deck():
    deck1 = Deck()
    deck2 = Deck()
    deck1.shuffle()
    assert not deck1 == deck2
    assert len(deck1.cards) == len(deck2.cards)
