from models.ChangeColor import ChangeColor
from models.ChangeLap import ChangeLap
from models.PlusTwo import PlusTwo
from models.PlusFour import PlusFour
from models.NumberCard import NumberCard
from models.StopCard import StopCard
from enums.Colors import Colors
import random

class Deck :
    mazzo = []
    def __init__(self):
        self.GenerateSpecialCard()
        self.GenerateNumberCard()
        self.GenerateEventCard()

    def GenerateSpecialCard(self):
        for i in range(4):
            self.mazzo.append(PlusFour())
            self.mazzo.append(ChangeColor())

    def GenerateNumberCard(self):
        for i in range(4):
            for x in range(0,10):
                if x>0:
                    self.mazzo.append(NumberCard(Colors(i),x))
                self.mazzo.append(NumberCard(Colors(i),x))
    def GenerateEventCard(self):
        for i in range(2):
            for x in range(4):
                self.mazzo.append(PlusTwo(Colors(i)))
                self.mazzo.append(ChangeLap(Colors(i)))
                self.mazzo.append(StopCard(Colors(i)))

    # Metodo che mescola il deck da gioco
    def shuffle(self):
        random.shuffle(self.mazzo)

    # Metodo che pesca una carta dal deck
    def draw(self):
        if self.len_deck() != 0:
            return self.mazzo.pop(len(self.mazzo)-1)

    # Metodo che stampa la lista di carte del deck
    def string_deck(self):
        for i in self.mazzo:
            print(i)
    # Metodo che controlla se il mazzo è vuoto
    def check_deck_is_empty(self):
        return len(self.mazzo) == 0
    #Metodo che svuota il deck
    def clear(self):
        self.mazzo.clear()
    # Metodo che restituisce il numero di carte nel mazzo
    def len_deck(self):
        return len(self.mazzo)