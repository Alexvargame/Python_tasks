#https://pythonist.ru/skolko-zhivotnyh/
from functools import wraps
from time import time
from collections import Counter
from math import *



def count_animals(astr):

    animals = ["dog", "cat", "bat", "cock", "cow", "pig",
           "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
           "frog", "hen", "mole", "duck", "goat"]
    result=[]
    adict={}
    for j in range(len(animals)):
        res=[]
        astr1=astr
        for an in animals[j:]:        
            if len(astr1)<3:
                break
            else:
                if [i for i in an if i in list(astr1)]==list(an):                   
                    res.append(an)             
                    astr1=dis(an,astr1)              
        result.append(res)
    for r in result:
        key, value=len(r), r
        l=adict.get(key,[])
        l.append(value)
    return  adict[max(adict)]

def dis(an,astr1):
    ss1=astr1
    for i in an:
        as1=ss1.replace(i,'',1)
        ss1=as1
    return as1
    


def main():
   
    print(count_animals("goatcode"))
    print(count_animals("cockdogwdufrbir"))
    print(count_animals("dogdogdogdogdog"))
    

 


if __name__ == "__main__":
    main()


