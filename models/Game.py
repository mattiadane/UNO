import random
from models.Player import Player
from models.SpecialCard import SpecialCard
from models.Table import Table
from models.Rules import Rules
from models.BotPlayer import  BotPlayer
from models.ChangeLap import ChangeLap
from models.StopCard import StopCard


class Game:
    first_names = ('John', 'Andy', 'Joe')
    last_names = ('Johnson', 'Smith', 'Williams')

    def __init__(self, players_number, bot_numbers):
        self.players = []
        self.player_numbers = players_number
        self.bot_numbers = bot_numbers
        self.table = Table()
        self.rules = Rules()
        print("Game launched")
        self.play_game()

    # Metodo che genera i players
    def generate_player(self):
        how_many_human = self.player_numbers - self.bot_numbers
        for i in range(how_many_human):
            player_name = input('Insert player name\n')
            print("Player name is : " + player_name)
            player = Player(player_name)
            self.add_player(player)
        for i in range(self.bot_numbers):
            bot_name = self.first_names[random.randint(0,2)] + " " + self.last_names[random.randint(0,2)]
            print("Player name is : " + bot_name)
            bot_player = BotPlayer(bot_name)
            self.add_player(bot_player)
        self.initialize_players_cards()



    # Metodo che inizializza le carte per ogni player
    def initialize_players_cards(self):
        for giocatore in self.players:
            for i in range(7):
                self.player_draw_card(giocatore)
    # Metodo che aggiunge un player alla partita
    def add_player(self, player):
        self.players.append(player)
    # Metodo che pesca una carta e la aggiunge alla mano del giocatore
    def player_draw_card(self, player):
        player.add_card(self.table.draw())
    # Metodo che implementa il motore del gioco
    def play_game(self):
        finish = False
        winner = ""
        i = 0
        self.table.shuffle()
        card = self.table.draw()
        self.table.play_card(card)
        if isinstance(card,SpecialCard):
            self.rules.select_random_color(self.table)
        self.generate_player()
        print("Deck size after dispatch cards: %d" % (self.table.len_deck()))
        for player in self.players:
            print("Player %s have %d cards" % (player.name,player.get_hand_card_number()))
        while not self.table.check_deck_is_empty() and not finish:
            if self.table.check_deck_is_empty() and winner == '':
                winner = 'draw, no winner'
            else :
                if len(self.table.played_cards) > 0:
                    if isinstance(self.table.show_last_played_card(),ChangeLap):
                        self.players.reverse()
                    if isinstance(self.table.show_last_played_card(),StopCard):
                        self.play_turn(self.players[i - 1],self.players[i])
                if i <= len(self.players):
                    if i == len(self.players)-1:
                        self.play_turn(self.players[i],self.players[0])
                        i = 0
                    else :
                        self.play_turn(self.players[i],self.players[i + 1])
                        i += 1
                    if self.players[i].get_hand_card_number() <= 0:
                        finish = True
                        winner = self.players[i].name   
        print("The player winner is: " + winner)
        replay =  input('Press 1 for replay\n')
        if replay.isnumeric() and int(replay) == 1:
            self.table.clear()
            Game(2,1)
        else :
            exit(replay)
        

    # Metodo che implementa il turno di gioco
    def play_turn(self, player, next_player):
        print("Player %s is your turn" % player.name)
        print("Last played card is: " + str(self.table.show_last_played_card()) + " and current color is: \n" + str(self.table.current_color or ''))
        print("Your hand is:")
        player.show_hand()
        if isinstance(player,BotPlayer):
            table_card = self.table.show_last_played_card()
            color = self.table.current_color
            if player.select_what_play(table_card,color) == None:
                print("%s draw a card!" % (player.name))
                player.add_card(self.table.draw())
            else :
                index = player.select_what_play(table_card,color)
                card = player.hand[index]
                print("%s play card: %s" % (player.name, str(card)))
                if self.rules.validate_card(card,table_card,color):
                    print("Card is valid!")
                    self.table.play_card(player.play_card(index))
                    self.rules.activate_card_rules(card,player,next_player,self.table)
                    color = self.table.current_color
                else :
                    print("Card play is wrong, retry!")
                    self.play_turn(player,next_player)                
        else:
            action = self.choose_play()
            if action.isnumeric():
                if int(action) < player.get_hand_card_number(): 
                    card = player.hand[int(action)] 
                    print("%s play card: %s" % (player.name, str(card)))
                    table_card = self.table.show_last_played_card()
                    color = self.table.current_color
                    if self.rules.validate_card(card,table_card,color):
                        print("Card is valid!")
                        self.table.play_card(player.play_card(int(action)))
                        self.rules.activate_card_rules(card,player,next_player,self.table)
                        color = self.table.current_color
                    else :
                        print("Card play is wrong, retry!")
                        self.play_turn(player,next_player)
                else :
                    print("Bad selection, retry")
                    self.play_turn(player,next_player)
            else :
                print("%s draw a card!" % (player.name))
                player.add_card(self.table.draw())
                          

    # Metodo che sceglie la carta da giocare
    def choose_play(self):
        print("Select your action: 0-n - Play Card, d - Draw card")
        valid_action = False
        while not valid_action:
            action = input()
            print("Your selected action is: " + action)
            if (action.isnumeric() and int(action) >= 0) or (not action.isnumeric() and action == "d"):
                valid_action = True
            else:
                print("Bad selection, retry")
        return action 