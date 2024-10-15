from socket import *
import numpy

def send_from(arr,dest):
    view=memoryview(arr).cast('B')
    while len(view):
        nsent=dest.send(view)
        view=view[nsent:]

def recv_into(arr,source):
    view=memoryview(arr).cast('B')
    while len(view):
        nrecv=source.recv_into(view)
        view=view[nrecv:]

        


if __name__ == '__main__':
    

    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', 25000))
    s.listen(1)
    c,a = s.accept()
    a = numpy.arange(0.0, 50000000.0)
    send_from(a,c)
    
