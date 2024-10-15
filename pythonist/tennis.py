from functools import wraps
from time import time
from collections import Counter
from math import *



def count_games(n):
    res=n//2
    m=round(log2(n//2))
    for i in range(m):
        res=res+2**i
        
    return res

def main():
    n = 127

    print(f"Колв-во игроков: {n}")

    print(f"Кол-во матчей: {count_games(n)}")
 

if __name__ == "__main__":
    main()


