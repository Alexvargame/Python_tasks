#https://pythonist.ru/mnozhestvennoe-chislo-sushhestvitelnyh/
from functools import wraps
from time import time
from collections import Counter
from math import *
import re


def pluralize(alst):
    

    return set([i+'s' if alst.count(i)>1 else i for i in alst ])




    
def main():
    print(pluralize(["cow", "pig", "cow", "cow"]))
    print(pluralize(["table", "table", "table"]))
    print(pluralize(["chair", "pencil", "arm"]))
    





if __name__ == "__main__":
    main()


