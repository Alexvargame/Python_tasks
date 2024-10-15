#https://pythonist.ru/smozhete-li-vy-vyjti-iz-labirinta/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def can_exit(alst):
    if alst[-1][-1]!=0:
        return False
    for i in range(len(alst)):
        for j in range(len(alst[0])):
            #print("i",i,"j", j, alst[i][j])
            if alst[i][j]!=1:
                if not ways(alst,i,j):
                    return False
    return True
            



def ways (alst, n,m):
    l=[]
    #print("nm", n,m)
    for ii in range(0 if n==0 else n-1, n+1 if n==len(alst)-1 else n+2):
        for jj in range(0 if m==0 else m-1, m+1 if m==len(alst[0])-1 else m+2):
            if (ii+jj)%2!=0:
                #print("*",ii, jj, alst[ii][jj])
                l.append(alst[ii][jj])
                #input()
    #print("l",l)
    if all(l):
        return False
    return True
                    
def main():
    print(can_exit([
  [0, 1, 1, 1, 1, 1, 1],
  [0, 0, 1, 1, 0, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 0, 0]
]))
  
    print(can_exit([
  [0, 1, 1, 1, 1, 0, 0],
  [0, 0, 0, 0, 1, 0, 0],
  [1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0]
]))
##def num_grid(alst):
##    for i in range(len(alst)):
##        for j in range(len(alst[i])):
##            if alst[i][j]!="#":
##                alst[i][j]=mines(alst,i,j)
##                
##    return alst         
##def mines (alst, n,m):
##    count=0
##    for i in range(0 if n==0 else n-1, n+1 if n==len(alst)-1 else n+2):
##        for j in range(0 if m==0 else m-1, m+1 if m==len(alst)-1 else m+2):
##                if alst[i][j]=='#':
##                    count=count+1                
##    return count
##




if __name__ == "__main__":
    main()


