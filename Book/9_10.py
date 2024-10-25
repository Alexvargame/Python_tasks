from threading import *
from time import sleep
n=int(input())
def fact(n):
    if n==1:
        return 1
    
    else:
        return n*fact(n-1)
def fact2(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact2(n-2)
def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fact(10))
print(fact2(10))
print(fib(10))

def display(f):
   
    mylock.acquire()
    t=current_thread()
    print(f)
    mylock.release()
    
mylock=Lock()
funcs=[fact(n), fact2(n), fib(n)]
T=[Thread(target=display, args=[funcs[k]], name=funcs[k]) for k in range(len(funcs))]
          
print(T)
for t in T:
    t.start()
for t in T:
    t.join()
