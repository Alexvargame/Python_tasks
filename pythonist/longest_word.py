#https://pythonist.ru/samoe-dlinnoe-slovo/
from functools import wraps
from time import time
from collections import Counter
from math import *



def longest_word(astr):
    adict={}
    for word in astr.split():
        key, value=len(word),word
        l=adict.get(key,[])
        l.append(value)
        adict[key]=l

    return adict[max(adict)][0]       

    
    
def main():
   
    print(longest_word("Margaret's toy is toy a pretty doll."))
    print(longest_word("A thing of beauty is a joy forever."))
    print(longest_word("Forgetfulness is by all means powerless!"))
    print(longest_word("QQQQ fff eeee"))
        
if __name__ == "__main__":
    main()


