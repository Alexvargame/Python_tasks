from socketserver import BaseRequestHandler,UDPServer
import time
class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from', self.client_address)
        msg,sock=self.request
        resp=time.ctime()
        sock.sendto(resp.encode('ascii'),self.client_address)
            
if __name__ == '__main__':
   
    serv = UDPServer(('', 20000), TimeHandler)
    serv.serve_forever()

##    from threading import Thread
##        MARKERS=16
##        
##        serv = TCPServer(('', 20000), EchoHandler)
##        for n in range(MARKERS):
##            t=Thread(target=serv.serve_forever)
##            t.daemon=True
##            t.start()
##        serv.serve_forever()

##class EchoHandler(BaseRequestHandler):
##    def handle(self):
##        print('Got connection from', self.client_address)
##        while True:
##            msg = self.request.recv(8192)
##            if not msg:
##                break
##            self.request.send(msg)
