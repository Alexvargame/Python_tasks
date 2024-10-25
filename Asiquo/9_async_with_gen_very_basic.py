import asyncio
import requests
from time import time, sleep


queue=[]


def counter():
    counter=0
    while True:
        print(counter)
        counter+=1
        yield
def printer():
    counter=0
    while True:
        if counter%3==0:
            print("B")
        counter+=1
        yield

def main():
    while True:
        g=queue.pop(0)
        next(g)
        queue.append(g)
        sleep(0.5)

if __name__ =='__main__':
    g1=counter()
    queue.append(g1)
    g2=printer()
    queue.append(g2)
    main()
