from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard

class ChangeLap(ColoredCard) :

    def __init__(self, color):
        super().__init__(color,CardProperty.CHANGE_LAP)
        
    def __str__(self):
        return super().__str__()