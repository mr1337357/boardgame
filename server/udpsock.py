import socket
import select
import sys

def log(fmt,*args):
    sys.stderr.write('SOCK: '+fmt.format(*args))

class udpsock:
    NEWUSER = 1
    DELUSER = 2
    MSG = 4
    def __init__(self,port):
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind(('0.0.0.0',31337))
        self.clients = {}
        self.nextuser = 0
        log('ready\n')

    def get_event(self):
        data,addr = sock.recvfrom(1024)
        if not addr in self.clients:
            self.clients[addr] = self.nextuser
            self.nextuser += 1
        return (self.MSG,self.clients[addr],data)
