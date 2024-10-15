#https://pythonist.ru/kolichestvo-sushhnostej/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


class User:
    count=[]
    def __init__(self, name):
        self.name=name
        

    def user_count(self):
        self.count.append(self.name)
        return len(self.count)

    def username(self):
        return self.name
        
        

    



def main():

    u1=User("A")
    u2=User('B')
    print(u1, u1.username())
    print(u1.user_count())
    print(u2.user_count())


if __name__ == "__main__":
    main()


