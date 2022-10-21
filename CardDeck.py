from Card import Card
import random


class CardDeck:
    def __init__(self):
        card_list = []
        card_list += self.compose_colour("hearts")
        card_list += self.compose_colour("spades")
        card_list += self.compose_colour("diamonds")
        card_list += self.compose_colour("clubs")
        self.card_list = card_list
        self.shuffled = False

    def __str__(self):
        return self.stringify()

    def __repr__(self):
        return self.stringify(False)

    def stringify(self, use_str = True):
        s = ""
        last_colour = None
        for item in self.card_list:
            if not self.shuffled and item.colour != last_colour:
                last_colour = item.colour
                s += f"\n\n{item.colour}:"
            s += "\n\t" if not self.shuffled else "\n"
            s += str(item) if use_str is True else repr(item)
        return s

    def shuffle(self):
        old_list: list = self.card_list.copy()
        new_list = []
        for i in range(len(old_list)):
            choice = random.choice(old_list)
            new_list.append(choice)
            old_list.remove(choice)
        self.card_list = new_list
        self.shuffled = True

    @staticmethod
    def compose_colour(colour):
        cards = []
        for i in range(1, 14):
            cards.append(Card(i, colour))
        return cards
