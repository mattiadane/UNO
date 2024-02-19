from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard


class PlusTwo(ColoredCard) :

    def __init__(self, color):
        super().__init__(color,CardProperty.PLUS_TWO)

    def __str__(self):
        return super().__str__()