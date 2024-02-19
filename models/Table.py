from models.Deck import Deck
from models.ColoredCard import ColoredCard
from enums.Colors import Colors
class Table :
    
    def __init__(self):
        self.deck = Deck()
        self.played_cards = []
        self.current_color = Colors.BLUE
    
    # Metodo che mescola il deck da gioco
    def shuffle(self):
        self.deck.shuffle()
    #Metodo che svuota il deck
    def clear(self):
        self.deck.clear()
    # Metodo che pesca una carta dal deck
    def draw(self):
        return self.deck.draw()
    # Metodo che stampa la lista di carte del deck
    def string_deck(self):
        self.deck.string_deck()
    # Metodo che restituisce il numero di carte nel mazzo
    def len_deck(self):
        return self.deck.len_deck()
    # Metodo che controlla se il mazzo è vuoto
    def check_deck_is_empty(self):
        return self.deck.check_deck_is_empty()
    # Metodo che gioca una carta e la aggiunge alle carte in gioco
    def play_card(self, card):
        self.played_cards.append(card)
        if isinstance(card,ColoredCard):
            self.current_color = card.color
        else:
            self.current_color = None
    # Metodo che mostra l'ultima carta giocata
    def show_last_played_card(self):
        return self.played_cards[-1]
    # Metodo che gestisce la carta cambia colore
    def change_table_color(self):
        found = False
        while not found:
            choosen_color = input("Choose the color : 0-Red, 1-Blue, 2-Green, 3-Yellow\n")
            if (not choosen_color.isnumeric()) or (int(choosen_color) not in [0,1,2,3]):
                print("Bad selection, retry")
            else :
                found = True
        print("Selected " + str(Colors(int(choosen_color))))
        self.current_color = Colors(int(choosen_color))
        return self.current_color
        


