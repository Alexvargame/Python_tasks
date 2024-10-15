#https://pythonist.ru/luchshaya-oczenka/
from functools import wraps
from time import time
from collections import Counter
from math import *



def top_notes(adict):
    return {'name':adict['name'], "top_note": max(adict['notes'])}



     
def main():
   
    print(top_notes({"name": "John", "notes": [3, 5, 4] }))
    print(top_notes({"name": "Max", "notes": [1, 4, 6] }))
    print(top_notes({"name": "Zygmund", "notes": [1, 2, 3]}))

    
    
    
    
        
if __name__ == "__main__":
    main()


