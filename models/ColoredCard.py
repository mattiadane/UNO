from enums.CardType import CardType
from models.Card import Card


class ColoredCard(Card):
    type = CardType.COLORED
    type_property = None

    def __init__(self, color, type_property):
        self.color = color
        self.type_property = type_property

    def __str__(self):
        return "(t: %s, p: %s, c: %s )" % (self.type, self.type_property, self.color)
