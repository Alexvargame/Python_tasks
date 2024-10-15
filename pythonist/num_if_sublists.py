#https://pythonist.ru/kolichestvo-spiskov-vnutri-spiska/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def num_of_sublists(alst):
  
    return len([i for i in alst if type(i)==list])



  
  
    
def main():
    print(num_of_sublists([[1, 2, 3]]))
    print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(num_of_sublists([[1, 2, 3],[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
    print(num_of_sublists([1, 2, 3]))
    






if __name__ == "__main__":
    main()


