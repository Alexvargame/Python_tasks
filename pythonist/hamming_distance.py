#https://pythonist.ru/rasstoyanie-hemminga/
from functools import wraps
from time import time
from collections import Counter
from math import *



    
def hamming_distance(astr,bstr):
    
    return len([astr[i] for i in range(len(astr)) if astr[i]!=bstr[i]])
  
    
def main():
 
    print(hamming_distance("abcde", "bcdef"))
    print(hamming_distance("abcde", "abcde"))
    print(hamming_distance("strong", "strung"))


    
if __name__ == "__main__":
    main()

