#https://pythonist.ru/schastlivaya-semerka/
from functools import wraps
from time import time
from collections import Counter
from math import *



def lucky_seven(alst):

    if len(alst)<3: return False
    for i in range(len(alst)):
        if alst[i]<6:
            for j in range(i+1, len(alst)):
                if alst[j]<6:
                    for k in range(j+1, len(alst)):
                        if alst[i]+alst[j]+alst[k]==7:
                            print(alst[i],alst[j],alst[k])
                            return True
                                   
    return False                           
   

def main():
   
    print(lucky_seven([2,3,4,7,8,9,1]))
    print(lucky_seven([1,2,5,4,6,5,9,1]))
    print(lucky_seven([0,0,2,0,3]))
    print(lucky_seven([3,4]))



if __name__ == "__main__":
    main()


