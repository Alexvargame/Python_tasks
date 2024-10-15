#https://pythonist.ru/snimaem-vneshnie-sloi/
from functools import wraps
from time import time
from collections import Counter
from math import *



def peel_layer_off(amatr):

    return  [amatr[i][1:-1] for i in range(1,len(amatr)-1) ]
 
def main():
   
    print(peel_layer_off([
  ["a", "b", "c", "d"],
  ["e", "f", "g", "h"],
  ["i", "j", "k", "l"],
  ["m", "n", "o", "p"]
]))
    
    print(peel_layer_off([
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25],
  [26, 27, 28, 29, 30],
  [31, 32, 33, 34, 35]
]))
    print(peel_layer_off([
  [True, False, True],
  [False, False, True],
  [True, True, True]
]) )
    print(peel_layer_off([
  ["hello", "world"],
  ["hello", "world"]
]))
 


if __name__ == "__main__":
    main()


