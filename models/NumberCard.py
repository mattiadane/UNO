from enums.CardProperty import CardProperty
from models.ColoredCard import ColoredCard 

class NumberCard(ColoredCard) :

    def __init__(self,color,number):
        self.number = number
        super().__init__(color,CardProperty.NUMBER)
        
    def __str__(self):
        return "(t: %s, p: %s, c: %s, n: %d )" % (self.type, self.type_property, self.color, self.number)