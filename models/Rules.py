import random
from enums.Colors import Colors
from models.BotPlayer import BotPlayer
from models.ColoredCard import ColoredCard
from models.SpecialCard import SpecialCard
from models.NumberCard import NumberCard
from enums.CardProperty import CardProperty
from models.PlusFour import PlusFour
from models.PlusTwo import PlusTwo
from models.StopCard import StopCard
from models.ChangeColor import ChangeColor
from models.ChangeLap import ChangeLap

class Rules:

    # Metodo che valida se la carta giocata è corretta in base alle regole del gioco
    @staticmethod
    def validate_card(player_card, table_card, table_current_color):
        if isinstance(player_card,NumberCard) and isinstance(table_card,NumberCard):
            if (player_card.color == table_current_color) or (player_card.number == table_card.number):
                    return True
        elif isinstance(player_card,ColoredCard) and (isinstance(table_card,ColoredCard) or isinstance(table_card,SpecialCard)):
            if player_card.color == table_current_color:
                return  True
        else :
            return True
        return False
                

    # Metodo che attiva le regole per le carte +2, +4 e cambia colore
    # assegnando 2/4 carte al giocatore avversario o cmbiando il colore del tavolo
    @staticmethod
    def activate_card_rules(card, player, next_player, table):
        if isinstance(card,PlusFour):
            print("Card is +4 then add 4 cards to player " + next_player.name)
            for i in range(4):
                next_player.add_card(table.draw())
            Rules.change_color(player,table)
        elif isinstance(card,PlusTwo):
            print("Card is +2 then add 2 cards to player " + next_player.name)
            for i in range(2):
                next_player.add_card(table.draw())
        elif isinstance(card, ChangeColor):
            Rules.change_color(player,table)

    # Metodo che cambia colore al tavolo
    @staticmethod
    def change_color(player, table):
        if isinstance(player,BotPlayer):
            color = player.select_change_color()
            print("Bot player color selected: " + str(color))
            table.current_color = color
        else :
            table.change_table_color()
    
    @staticmethod
    def select_random_color(table):
        color = random.randint(0,4)
        print("Selected color is: " + str(Colors(color)))
        table.current_color = Colors(color)

