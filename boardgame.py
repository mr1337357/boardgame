#!/usr/bin/python
import sys
from bgplayer import bgplayer
from random import randint

class game:
    def __init__(self):
        self.current_player = None
        self.player_count = None
    
    def create_players(self,players):
        self.player_count = players
        self.players = []
        for p in range(players):
            self.players.append(bgplayer())

    def start(self):
        self.current_player = 0

    def roll(self):
        value = randint(1,6)
        return value

    def get_winner(self):
        for p in self.players:
            if p.position >= 150:
                return p
        return None

    def get_current_player(self):
        return self.players[self.current_player]

    def end_turn(self,next_player=None):
        if next_player:
            self.current_player = next_player
        else:
            c = self.current_player
            c = (c + 1) % self.player_count
            self.current_player = c

if __name__ == '__main__':
    g = game()
    players = None
    while players == None:
        try:
            players = int(input('number of players: '))
        except:
            pass

    g.create_players(players)
    g.start()
    while not g.get_winner():
        p = g.get_current_player()
        input('{}: roll dice'.format(p.name))
        r = g.roll()
        print('rolled {}'.format(r))
        p.move(r)
        print('moved to {}'.format(p.position))
        g.end_turn()
    winner = g.get_winner()
    print('{} wins'.format(winner.name))
