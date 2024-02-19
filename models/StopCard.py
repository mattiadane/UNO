from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard

class StopCard(ColoredCard) :

    def __init__(self, color):
        super().__init__(color,CardProperty.PROHIBITION)  

    def __str__(self):
        return super().__str__()