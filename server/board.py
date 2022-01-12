#todo: load board from file

class board():
    def __init__(self):
        pass

    def getnext(self,pos):
        p = pos[:]
        p[1] += 1
        return [p]

    def getevent(self,pos):
        if pos[1] >= 20:
            return 'win'
        return 'none'
