import csv
from collections import namedtuple

with open('stocks.csv') as f:
    f_csv=csv.reader(f)
    headlings=next(f_csv)
    Row=namedtuple('Row',headlings)
    for r in f_csv:
        row=Row(*r)
        print(row)
        
