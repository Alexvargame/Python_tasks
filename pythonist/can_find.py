#https://pythonist.ru/bigrammy/
from functools import wraps
from time import time
from collections import Counter
from math import *


def can_find(alst,blst):
    if len([w for w in alst if w in ('.').join(blst)])==len(alst):
           return True
    return False


    
def main():

    print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
    print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))# "cu" не встречается ни в одном слове
    print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
    print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))
    
    
if __name__ == "__main__":
    main()


