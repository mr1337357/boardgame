import sys
from game import game
from sockapi import sockapi

class server_instance():
    def __init__(self):
        self.games = {}

    def newgame(self,name,playernames):
        if name in self.games:
            raise Exception('game exists')
        players = [ player(n) for n in playernames]
        self.games = game(players)
    
if __name__ == '__main__':
    s = sockapi()
    while True:
        ev = s.get_event()
        print(ev)
