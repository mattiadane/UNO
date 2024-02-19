from enums.Colors import Colors
from models.ColoredCard import ColoredCard
from models.NumberCard import NumberCard
from models.Player import Player
from models.SpecialCard import SpecialCard
import random

class BotPlayer(Player):

    # Metodo che fa scegliere al bot cosa giocare (Pesco o gioco una carta)?
    def select_what_play(self, field_card, table_color):
        card = ''
        for i in range(0,len(self.hand)):
            if self.card_logic(self.hand[i],field_card,table_color):
                card = i
                break
        if card != '':
            return card
        else :
            return None

    # Metodo che una volta che decido di giocare una carta
    # Fa scegliere quale carta giocare
    def card_logic(self, my_card, field_card, table_color):
        if isinstance(my_card,NumberCard) and isinstance(field_card,NumberCard) :
            if my_card.color == table_color or my_card.number == field_card.number:
                return True
        elif (isinstance(my_card,ColoredCard) or isinstance(my_card,NumberCard)) and (isinstance(field_card,ColoredCard) or isinstance(field_card,SpecialCard)):
            if my_card.color == table_color:
                return  True
        else :
            return True
        return False
           

    # Metodo per far scegliere al bot il colore della carta cambia colore in base
    # alle carte che ho in mano
    def select_change_color(self):
        red = 0
        blue = 0
        yellow = 0
        green = 0
        for card in self.hand:
            if isinstance(card,ColoredCard):
                if card.color == Colors.RED:
                    red += 1
                elif card.color == Colors.BLUE:
                    blue += 1
                elif card.color == Colors.GREEN:
                    green += 1
                elif card.color == Colors.YELLOW:
                    yellow += 1
        if red > blue and red > yellow and red > green :
            return  Colors.RED
        elif blue > red and blue > yellow and blue > green:
            return  Colors.BLUE
        elif yellow > blue and yellow > red and yellow > green:
            return  Colors.YELLOW
        elif green > blue and green > red and green > yellow:
            return  Colors.GREEN
        else :
            return  Colors(random.randint(0,3))

