class bgplayer:
    def __init__(self):
        self.position = 0
        n = input('name: ')
        self.name = n
    
    def move(self,distance):
        self.position += distance
