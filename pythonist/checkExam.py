#https://github.com/appKODE/2018-internship-backend
from functools import reduce
from collections import deque

def checkExam(alst,blst):

    
   
    if sum(list(map(lambda a,b: check(a,b) if b else 0, alst, blst))) >0:
        return sum(list(map(lambda a,b: check(a,b) if b else 0, alst, blst)))
    else:
        return 0




def check(a,b):
    if not b:
        return 0
    elif a==b:
        return 4
    else:
        return -1





def main():
  
     print(checkExam(['a','a','b','b'],['a','c','b','d']))
     print(checkExam(['a','a','c','b'],['a','a','b','']))
     print(checkExam(['a','a','b','c'],['a','a','b','c']))
     print(checkExam(['b','c','b','a'],['','a','a','c']))


if __name__ == "__main__":
    main()


