#https://pythonist.ru/poslednij-element/
from functools import wraps
from time import time
from collections import Counter
from math import *


def match_last_item(alst):
    if ('').join([str(i) for i in alst[:-1]])==str(alst[-1]):
        return True
    return False


    
def main():

    print(match_last_item(["rsq", "6hi", "g", "rsq6hig"]))
    print(match_last_item([1, 1, 1, "11"]))
    print(match_last_item([8, "thunder", "True", "8thunderTrue"]))
    print(match_last_item([8, "thunder", True, "8thunderTrue"]))
    
if __name__ == "__main__":
    main()


