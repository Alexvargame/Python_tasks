#https://pythonist.ru/lajki-i-dizlajki-na-youtube/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def like_or_dislike(alst):
    print("*")
    if len(alst)>1 and alst[-1]==alst[-2]:
        for i in range(0,len(list(reversed(alst))),2):
            if list(reversed(alst))[i:i+2]!=list(reversed(alst))[i+2:i+4] and len(list(reversed(alst))[i+2:i+4])>0:
                print(list(reversed(alst))[i:i+2],list(reversed(alst))[i+2:i+4])
                print(list(reversed(alst))[i:i+2]!=list(reversed(alst))[i+2:i+4])
                input()
                return alst[-1]
                       
            
        return "Nothing"
       
    return alst[-1]

    
def like_or_dislike1(alst):
    state = 'Nothing'
    for vote in alst:
        if state == vote:
            state = 'Nothing'
        else:
            state = vote
  
    return state


def main():
   
    print(like_or_dislike(["Dislike"]))
    print(like_or_dislike(["Like", "Like","Like"]))
    print(like_or_dislike(["Dislike", "Like"]))
    print(like_or_dislike(["Like", "Like"]))
    print(like_or_dislike(["Like", "Dislike", "Dislike"]))
   
  
 


if __name__ == "__main__":
    main()


