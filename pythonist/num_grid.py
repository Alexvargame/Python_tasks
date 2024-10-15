#https://pythonist.ru/sapyor/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def num_grid(alst):
    for i in range(len(alst)):
        for j in range(len(alst[i])):
            if alst[i][j]!="#":
                alst[i][j]=mines(alst,i,j)
                
    return alst         
def mines (alst, n,m):
    count=0
    for i in range(0 if n==0 else n-1, n+1 if n==len(alst)-1 else n+2):
        for j in range(0 if m==0 else m-1, m+1 if m==len(alst)-1 else m+2):
                if alst[i][j]=='#':
                    count=count+1                
    return count


def main():
    print(num_grid([
  ['-', '-', '-'],
  ['-', '#', '-'],
  ['#', '-', '#']]
  ))
    print(num_grid([
  ['-', '-', '-', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '#', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '-', '-', '-']]
  ))
    print(num_grid([
  ['-', '-', '-', '#', '#'],
  ['-', '#', '-', '-', '-'],
  ['-', '-', '#', '-', '-'],
  ['-', '#', '#', '-', '-'],
  ['-', '-', '-', '-', '-']]
  ))
    print(num_grid([
  ['-', '-', '-', '-', '#'],
  ['-', '-', '-', '-', '-'],
  ['-', '-', '#', '-', '-'],
  ['-', '-', '-', '-', '-'],
  ['#', '-', '-', '-', '-']]
  ))
##     print(num_grid([
##  [1, 2, 3],
##  [4, 2, 6],
##  [7, 8, 9]]
##  ))


if __name__ == "__main__":
    main()


