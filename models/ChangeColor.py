from enums.CardProperty import CardProperty 
from models.SpecialCard import SpecialCard

class ChangeColor(SpecialCard) :

    def __init__(self):
        super().__init__(CardProperty.CHANGE_COLOUR)

    def __str__(self):
        return super().__str__()