from socketserver import BaseRequestHandler, TCPServer, StreamRequestHandler
class EchoHandler(StreamRequestHandler):
    timeout=5
    rbufsize=-1
    wbufsize=0
    disable_nagle_algorithm=False
    def handle(self):
        print('Got connection from', self.client_address)
        try:
            for line in self.rfile:
                self.wfile.write(line)
        except socket.timeout:
            print('Timed out')
            
if __name__ == '__main__':
    TCPServer.allow_reuse_address=True
    serv = TCPServer(('', 20000), EchoHandler)
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
