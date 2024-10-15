#https://pythonist.ru/stalaktity-ili-stalagmity/
from functools import wraps
from time import time
from collections import Counter
from math import *
import numpy as np



    
def mineralFormation(amatr):
    print(amatr)
    m=[sum(i) for i in amatr]
    if m[0]!=0 and m[-1]!=0:
        return "both"
    elif m[0]!=0 and m[-1]==0:
        return "stalactites"
    elif m[0]==0 and m[-1]!=0:
        return "stalagmites"
    else:
        return None

    
    #matrix=list(zip(*amatr[::-1]))


    #matrix1=np.array(amatr)
    #print(matrix1[:,0])
    
    #return matrix
  
    
def main():
 
    print(mineralFormation([
  [0, 1, 0, 1],
  [0, 1, 0, 1],
  [0, 0, 0, 1],
  [0, 0, 0, 0]
]))
    print(mineralFormation([
  [0, 0, 0, 0],
  [0, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))
    print(mineralFormation([
  [1, 0, 1, 0],
  [1, 1, 0, 1],
  [0, 1, 1, 1],
  [0, 1, 1, 1]
]))

    
if __name__ == "__main__":
    main()

