"""
def sum_(*args):
   
    try:
        for i in args:
            if type(i)==int:
                pass
        return sum(args)
    except TypeError:
        return "::"
print(sum_(2,'w'))
def interv():
    
    n=int(input())
    n1=int(input())
    print(type(n1), type(n))    
    try:
        if type(n)==int and type(n1)==int:
            return n
    except TypeError:
        print("::")

print(interv())
print("(a**2-1)*x=b")
def q():
    a=int(input())
    b=int(input())
    try:
        if (a**2-1)!=0:
            return ("x=", b/(a**2-1))
    except ValueError:
        print("0")
print(q())


print("-----------------")
class MyError(Exception):

 def __init__(self):
     self.values=[]
 def __add__(self, val):
     self.values.append(chr(val))
     return self
def getMyError(n):
     try:
         if ord(n)<=ord('A'):
             raise MyError
         getMyError(chr(ord(n)-1))
     except MyError as error:
            raise error+ord(n)
def getList(n):
     try:
         getMyError(n)
     except MyError as error:
         return error.values

A=getList('D')
print(A)
B=getList('B')
print(B)
print("--------")

from threading import *
from time import sleep

def mysum():
 global num
 k=1
 txt=str(num)
 while myevent.is_set():
     num+=k
     txt+=" + "+str(k)
     print("[", k,"] ", txt," = ", num, sep="")
     k+=1

     sleep(0.3)

t=Thread(target=mysum)

num=0
myevent=Event()
myevent.set()
t.start()
sleep(1)
myevent.clear()

if t.is_alive():
 t.join()

print("S", num)
print("------------")

""""
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
"""
print("------------")
from threading import *
from time import sleep
A=[1,2,3,4,5]
B=['A','B','C','D','F']
class twolist():
    def __init__(self, l, l1):
        self.l=l
        self.l1=l1
    
    def mylist(self):
        
        sleep(1)
        print("#")
        myevent.wait()
        myevent.clear()
        for a in A:
            self.l.append(a)
            print(self.l)
        myevent.set()
        sleep(1)
        myevent.wait()
        myevent.clear()
   
        myevent.set()

    def mylist1(self):
       
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
aa=twolist(A,B)
myevent=Event()
myevent.set()
F=Thread(target=aa.mylist)
S=Thread(target=aa.mylist1)
F.start()
S.start()
F.join()
S.join()
print(aa.l)
print(aa.l1)
"""


