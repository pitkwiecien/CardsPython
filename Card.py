class Card:
    def __init__(self, value, colour):
        self.value = value
        self.colour = colour
        self.image = self.get_image()

    def __str__(self):
        if self.value in range(2,11):
            value = self.value
        elif self.value == 1:
            value = "ace"
        elif self.value == 11:
            value = "jack"
        elif self.value == 12:
            value = "queen"
        elif self.value == 13:
            value = "king"
        else:
            return f"ERROR - value: {self.value}, colour: {self.colour}"
        return f"{value} of {self.colour}"

    def __repr__(self):
        return f"Card(value={self.value}, colour={self.colour}, image={self.image})"

    def get_image(self):
        return f"resources/card_images/{str(self).replace(' ', '_')}.png"
