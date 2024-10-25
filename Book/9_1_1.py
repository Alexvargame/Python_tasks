
from threading import Thread, Lock, Event

from time import sleep
"""
def alpha():
 for k in range(5):

     sleep(1.5)
     print("[", k+1,"] Alpha", sep="")

def bravo():
 for k in range(5):
     print("[", k+1,"] Bravo", sep="")

     sleep(1)
t=Thread(target=bravo)

t.start()

alpha()



def display(count, time, text):
 for k in range(count):
     sleep(time)     
     print("[", k+1,"] ", text, sep="")
print("E")	
t=Thread(target=display, args=(5,2,"AAA"))

t.start()

display(3,1.5,"BBB")

t.join()
print("yy")

class MyClass:

 def __init__(self, text):
     self.text=text

 def __call__(self, count, time):
     for k in range(count):
         sleep(time)
         print("[", k+1,"] ", self.text, sep="")
print("E")
obj=MyClass("6")

t=Thread(target=obj, kwargs={"time":2,"count":5})

t.start()

MyClass("AAA")(3,1.5)

if t.is_alive():
 t.join()
print("zzx")


class MyThread(Thread):
    def __init__(self, count,time,text):
        super().__init__()
        self.count=count
        self.time=time
        self.text=text
    def run(self):
        for k in range(self.count):
            sleep(self.time)
            print("[",k+1,"]", self.text, sep="")
print("Begin")
A=MyThread(5,2,"Alf")
B=MyThread(3,1,"Bra")
A.start()
B.start()

if A.is_alive():
    A.join()
if B.is_alive():
    B.join()
    


def calc(txt, op):

 global number

 for k in range(3):
     mylock.acquire()
     print(txt,"lock ", sep="")
     try:
         print(txt,"ooo", number)
         val=number
         sleep(1)
         if op:
             number=val+1
         else:
             number=val-1
         print(txt," uuu", number)
     finally:
         print(txt,":unlock", sep="") 
         print("-----------------------")
         mylock.release()
     sleep(1)

number=0

mylock=Lock()
A=Thread(target=calc, args=["A", True])
B=Thread(target=calc, args=["B", False])
A.start()
B.start()

A.join()
B.join()
"""
def display(txt):
    A=[1,2]
    B=["A","B"]
    sleep(1)
    myevent.wait()
    myevent.clear()
    for a in A:
        print("[",a,"]", txt, sep="")
    myevent.set()
    sleep(1)
    myevent.wait()
    myevent.clear()
    for b in B:
        print("[",b,"]", txt, sep="")

    myevent.set()
myevent=Event()
myevent.set()
F=Thread(target=display, args=["One"])
S=Thread(target=display, args=["Second"])
F.start()
S.start()
F.join()
S.join()


def from_left():
 global first, last, L
 val=10
 while True:
     if first<last:
         L[first]=val
         val+=10
         first+=1
         sleep(0.3)
     else:
         break
def from_right():
 global first, last, L
 val="A"
 while True:
     if first<last:
         L[last]=val
         val=chr(ord(val)+1)
         last-=1
         sleep(0.3)
     else:
            break

size=11

L=["*" for k in range(size)]

first=0
last=len(L)-1
print("a")
print(L)

A=Thread(target=from_left)
B=Thread(target=from_right)

A.start()
B.start()

A.join()
B.join()

print("jj")
print(L)
