#https://pythonist.ru/morskoj-boj/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def fire(alst, astr):
    l=['A','B','C','D','E']
    adict={}
    for i in range(len(alst)):
        key, value=l[i], alst[i]
        adict[key]=value
        

    if adict[astr[0]][int(astr[1])-1] =='*':
        return 'BOOM'
    return 'splash'

def fire(matrix, coordinates):
    x, y = coordinates
    return 'BOOM' if matrix[ord(x) - 65][int(y) - 1] == '*' else 'splash'

def main():
    matrix=[
  ['-', '-', '-', '*', '*'],
  ['-', '*', '-', '-', '-'],
  ['-', '*', '-', '-', '-'],
  ['-', '*', '-', '-', '-'],
  ['-', '-', '*', '*', '-']]
    print(fire(matrix, 'A1'))
    print(fire(matrix, 'A4'))
    print(fire(matrix, 'D2'))



if __name__ == "__main__":
    main()


