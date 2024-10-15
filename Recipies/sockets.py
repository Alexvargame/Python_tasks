import logging
from multiprocessing import Pool
from functools import partial

from socketserver import StreamRequestHandler, TCPServer

class EchoHandler(StreamRequestHandler):

    def __init__(self,*args,ack,**kwargs):
        print(ack)
        self.ack=ack
        super().__init__(*args,**kwargs)

        
    def handler(self):
        for line in self.rfile:
            print(line)
            self.wfile.write(self.ack+line)



if __name__ == '__main__':

    
    serv=TCPServer(('',1500),partial(EchoHandler,ack=b'RECEIVED:'))
    serv.serve_forever()
