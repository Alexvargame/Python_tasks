#https://pythonist.ru/gruppy-iz-treh-bukv/
from functools import wraps
from time import time
from collections import Counter
from math import *




def three_letter_collection(astr):

    return sorted([astr[i:i+3] for i in range(len(astr)-2)])
    

def three_letter_collection1(astr):
    return sorted(a+b+c for a,b,c in zip(s, s[1::], s[2::]))

def main():
   
     print(three_letter_collection("python"))
     print(three_letter_collection("slap"))
     print(three_letter_collection("click"))
     print(three_letter_collection("hi"))
     print(three_letter_collection("cat"))
    
    
        
if __name__ == "__main__":
    main()


