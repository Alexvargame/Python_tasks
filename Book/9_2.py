from threading import *
from time import sleep
l=[]
def mylist():
    A=[1,2,3,4,5]
    sleep(1)
    myevent.wait()
    myevent.clear()
    for a in A:
        l.append(a)
        myevent.set()
        sleep(1)
        myevent.wait()
        myevent.clear()
   
    myevent.set()

def mylist1():
    B=['A','B','C','D','F']
    sleep(1)
    myevent.wait()
    myevent.clear()
    for b in B:
        l.append(b)
        myevent.set()
        sleep(1)
        myevent.wait()
        myevent.clear()
   
    myevent.set()
myevent=Event()
myevent.set()
F=Thread(target=mylist)
S=Thread(target=mylist1)
F.start()
S.start()
F.join()
S.join()
print(l)
