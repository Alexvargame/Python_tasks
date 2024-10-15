#https://pythonist.ru/naibolee-chasto-vstrechayushhiesya-slovo-i-dlinnoe-slovo-v-tekste/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def often_word(atxt):
    adict={}
    
    for a in atxt.split():
        key, value=atxt.split().count(a),a
        l=adict.get(key,[])
        l.append(value)
        adict[key]=l
    
    
    
    print(adict)
    return   set(adict[max(adict)])



def longest_word(atxt):
    adict={}

    for a in atxt.split():
        key, value=len(a),a
        l=adict.get(key,[])
        l.append(value)
        adict[key]=l
    
    print(adict)
    
  
    return   set(adict[max(adict)])
    
def main():
    print(often_word("Напишите программу, которая принимает текст выводит два слова: то, которое встречается в тексте чаще всего, и самое длинное  самое длинноеи самое длинное"))
    print(longest_word("Напишите программу, которая принимает текст выводит два слова: то, которое встречается в тексте чаще всего, и самое длинное  самое длинноеи самое длинное"))






if __name__ == "__main__":
    main()


