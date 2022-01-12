import socket
import select
import sys

def log(fmt,*args):
    sys.stderr.write('SOCK: '+fmt.format(*args))

class sockclient:
    pass

class sockapi:
    NEWUSER = 1
    DELUSER = 2
    MSG = 4
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind(('0.0.0.0',31337))
        self.sock.listen(2)
        self.clients = {}
        self.poll = select.poll()
        self.poll.register(self.sock)
        log('ready\n')

    def add_client(self):
        sock,addr = self.sock.accept()
        self.clients[sock.fileno()] = sock
        self.poll.register(sock,select.POLLIN)
        log('add client {}\n',sock.fileno())
        return (self.NEWUSER,sock.fileno())

    def handle_event(self,socket):
        msg = socket.recv(1024)
        fn = socket.fileno()
        if len(msg) == 0:
            self.clients[fn].close()
            del self.clients[fn]
            return (self.DELUSER,fn)
        else:
            return (self.MSG,fn,msg)


    def get_event(self):
        evs = self.poll.poll()
        for sock,ev in evs:
            if sock == self.sock.fileno():
                if ev == select.POLLIN:
                    return self.add_client()
            if sock in self.clients:
                return self.handle_event(self.clients[sock])
