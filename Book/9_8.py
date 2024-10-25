from threading import *
from time import sleep
l=[]

class Twolist:
    def __init__(self):
        self.l=[]
        self.l1=[]
    
    def mylist(self, A):
        #A=[1,2,3,4,5]
        sleep(1)
        myevent.wait()
        myevent.clear()
        for a in A:
            self.l.append(a)
            myevent.set()
            sleep(1)
            myevent.wait()
            myevent.clear()
       
        myevent.set()

    def mylist1(self, B):
        #B=['A','B','C','D','F']
        sleep(1)
        myevent.wait()
        myevent.clear()
        for b in B:
            self.l1.append(b)
            myevent.set()
            sleep(1)
            myevent.wait()
            myevent.clear()
       
        myevent.set()
aa=Twolist()
myevent=Event()
myevent.set()
F=Thread(target=aa.mylist([1,2,3,4,5]))
S=Thread(target=aa.mylist1(['A','B','C','D','F']))
F.start()
S.start()
F.join()
S.join()
print(aa.l)
print(aa.l1)
