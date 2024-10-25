from csp import CSP,Constraint
from typing import Dict,List,Optional,NamedTuple
from string import ascii_uppercase
from random import choice

Grid=[[]]


class GridLocation(NamedTuple):
    row:int
    column:int

def generate_grid(rows,columns):
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]

def display_grid(grid):
    for row in grid:
        print(''.join(row))

def generate_domain(word,grid):
    domain=[]
    height=len(grid)
    width=len(grid[0])
    length=len(word)
    for row in range(height):
        for col in range(width):
            columns=range(col,col+length+1)
            rows=range(row,row+length+1)
            if col+length<=width:
                domain.append([GridLocation(row,c) for c in columns])
                if row+length<=height:
                    domain.append([GridLocation(r,col+(r-row)) for r in rows])
            if row+length<=height:
                domain.append([GridLocation(r,col) for r in rows])
                if col-length>=0:
                    domain.append([GridLocation(r,col-(r-row)) for r in rows])
    return domain

class WordSearchConstraint(Constraint[str,List[GridLocation]]):
    def __init__(self,words):
        super().__init__(words)
        self.words=words
    def satisfied(self,assignment):
        print('asss',assignment)
        all_locations=[locs for values in assignment.values() for locs in values]
        print(all_locations)
        print()
        print(list(set(all_locations)))
        return len(set(all_locations))==len(all_locations)



def main():
    words = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations={}
    grid=generate_grid(9,9)
    for word in words:
        locations[word]=generate_domain(word,grid)
    csp=CSP(words,locations)
    csp.add_constraint(WordSearchConstraint(words))
    solution=csp.backtracking_search()
    print(solution)
    if solution is None:
        print('No solution found')
    else:
        for word,grid_locations in solution.items():
            if choice([True,False]):
                grid_locations.reverse()
            for index,letter in enumerate(word):
                (row,col)=(grid_locations[index].row,grid_locations[index].column)
                grid[row][col]=letter
        display_grid(grid)






if __name__=="__main__":
    main()
