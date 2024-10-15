#@from typing import Dict,List,Optional,TypeVar,Generic
from string import ascii_uppercase
from random import choice
from collections import namedtuple
from abc import ABC, abstractmethod



#Grid=[[]]
GridLocation=namedtuple('GridLocation','row column')

# V=TypeVar('V')
# D=TypeVar('D')

class Constraint(ABC):#Generic[V,D],ABC):
    def __init__(self,variables):
        self.variables=variables
    @abstractmethod
    def satisfied(self,assignment):
        ...
class CSP():#Generic[V,D]):
    def __init__(self,variables,domains):
        self.variables=variables
        self.domains=domains
        self.constraints={}

        for variable in self.variables:
            self.constraints[variable]=[]
            if variable not in self.domains:
                raise LookupError("Every variable should have a domian assigned to it")
    def add_constraint(self,constraint):
        #print('CVASR',constraint.variables,self.variables)
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)
    def consistent(self,variable,assignment):
        print('AAAAADDD',assignment,self.constraints[variable])
        for constraint in self.constraints[variable]:
            print('CONS', constraint.satisfied(assignment))
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self,assignment={}):
        print(assignment,self.variables,len(assignment)==len(self.variables))
        if len(assignment)==len(self.variables):
            print('BASE')
            return assignment
        unassigned=[v for v in self.variables if v not in assignment]
        print('U',unassigned)
        first=unassigned[0]
        for value in self.domains[first]:
            local_assignment=assignment.copy()
            print('LA',local_assignment)
            local_assignment[first]=value
            print('VALUE',value,local_assignment)
            if self.consistent(first,local_assignment):
                result=self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None



def generate_grid(rows,columns):
    return [[choice(ascii_uppercase) for c in range(columns)] for r in range(rows)]

def display_grid(grid):
    for row in grid:
        row=[str(i) for i in row]
        print(''.join(row))

def generate_domain(ship,grid):
    domain=[]
    height=len(grid)
    width=len(grid[0])
    length=len(ship)
    for row in range(height):
        for col in range(width):
            columns=range(col,col+length)
            rows=range(row,row+length)
            if col+length<=width:
                domain.append([GridLocation(row,c) for c in columns])
            #if length>1:
            if row+length<=height:
                domain.append([GridLocation(r,col) for r in rows])

    return domain

class ShipSearchConstraint(Constraint):#[str,List[GridLocation]]):
    def __init__(self,ships):
        super().__init__(ships)
        self.ships=ships
    def satisfied(self,assignment):
        print('assi',assignment.values())
        loc=[]
        all_locations=[locs for values in assignment.values() for locs in values]
        for values in assignment.values():
            print('VV',values)
            for locs in values:
                print('LOC',locs)
                loc.append(locs)
        print('ALLLOC',all_locations)
        print('LOCCCC',loc)
        print()
        print('SET',list(set(all_locations)))
        return len(set(all_locations))==len(all_locations)


def validate_battlefield(field):
    print(field)
    display_grid(field)
    solutions={}
    ships=['AAAA']#,'AAA','BBB','AA','BB','CC','A','B','C','D']#['A','B','C','D','AA','BB','CC','AAA','BBB','AAAA']
    locations = {}
    for ship in ships:
        locations[ship] = generate_domain(ship, field)
    # print('locations')
    # for v in locations.values():
    #     for vv in v:
    #         print(vv)
    csp = CSP(ships, locations)
    #print('DOM',csp.domains)
    csp.add_constraint(ShipSearchConstraint(ships))

    solution = csp.backtracking_search()
    print('SOL', solution)

    # for ship in ships:
    #     locations = {}
    #     locations[ship]=generate_domain(ship,field)
    #     csp=CSP([ship],locations)
    #     csp.add_constraint(ShipSearchConstraint([ship]))
    #     solution=csp.backtracking_search()
    #     print('SOL',solution)
    #     solutions[ship]=solution
    #     input()
def main():
    
    # print(validate_battlefield([[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
    #                            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    #                            [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    #                            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    #                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    #                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    #                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    #                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))
    print(validate_battlefield([[0, 0, 0, 0, 0, 'A', 'A', 0, 0, 0],
                                ['A', 0, 'B', 0, 0, 0, 0, 0, 'C', 0],
                                ['A', 0, 'B', 0, 'A', 'A', 'A', 0, 'C', 0],
                                ['A', 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                ['A', 0, 0, 0, 0, 0, 0, 0, 'B', 0],
                                [0, 0, 0, 0, 'B', 'B', 'B', 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 'A', 0],
                                [0, 0, 0, 'C', 0, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 'D', 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]))


if __name__ == "__main__":
    main()

