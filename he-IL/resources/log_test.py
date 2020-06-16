from card import Card
from deck import Deck
import logging

logging.basicConfig(level=logging.DEBUG)

my_card = Card("hearts", "6")
my_card.suit = "blobs"

deck = Deck()
