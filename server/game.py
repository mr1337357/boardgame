from board import board
from player import player
import random

class game():
    def __init__(self,players):
        self.players=players
        self.board = board()
        self.currentplayer = players[0]

    def roll(self,player):
        steps = random.choice([1,2,3,4,5,6])
        while steps:
            n = self.board.getnext(player.pos)
            player.pos = n
            
