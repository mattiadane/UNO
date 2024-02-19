from enums.CardType import CardType
from models.Card import Card


class SpecialCard(Card):
    type = CardType.SPECIAL
    type_property = None

    def __init__(self, type_property):
        self.type_property = type_property

    def __str__(self):
        return "(t: %s, p: %s )" % (self.type, self.type_property)
