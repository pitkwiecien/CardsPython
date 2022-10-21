from CardDeck import CardDeck

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pathlib

pathlib.Path(".").joinpath('resources/card_images')

figure, axes_list = plt.subplots(nrows=4, ncols=13)
plt.show()

deck = CardDeck()
print(deck)
print(repr(deck))

deck.shuffle()
print(deck)