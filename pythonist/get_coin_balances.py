#https://pythonist.ru/monetnaya-kooperacziya/
from functools import wraps
from time import time
from collections import Counter
from math import *



def get_coin_balances(alst, blst):

    result=[3,3]             
    for i in list(zip(alst,blst)):
        if i[0]<i[1] :
            result[0]=result[0]-1
            result[1]=result[1]+3

        elif i[0]>i[1]:
            result[1]=result[1]-1
            result[0]=result[0]+3

        elif i[0]==i[1]=='share':
            result[1]=result[1]+2
            result[0]=result[0]+2
    
    
    return result    
 
def main():
   
    print(get_coin_balances(["share"], ["share"]))
    print()
    
    print(get_coin_balances(["share", "share", "share"], ["steal", "share", "steal"]))
    
    print(get_coin_balances(["steel"], ["share"]))
    print()
    print(get_coin_balances(["steel"], ["steel"]))
    print()
        

 


if __name__ == "__main__":
    main()


