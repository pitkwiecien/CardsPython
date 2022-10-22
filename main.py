import grapher
from classes import card_deck

deck = card_deck.CardDeck()

grapher.draw(deck)
deck.shuffle()
grapher.draw(deck)
