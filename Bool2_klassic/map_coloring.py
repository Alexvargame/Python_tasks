from csp import Constraint, CSP
from typing import Dict, List, Optional

class MapColorConstraint(Constraint[str,str]):
    def __init__(self, place1, place2):
        super().__init__([place1,place2])
        self.place1=place1
        self.place2=place2
    def satisfied(self, assigment):
        if self.place1 not in assigment or self.place2 not in assigment:
            return True

        return assigment[self.place1]!=assigment[self.place2]

if __name__=="__main__":
    variables=['Western Australia', 'Northern Territory','South Australia',
               'Queensland','New South Wales', 'Victoria','Tasmania']
    domains={}
    for variable in variables:
        domains[variable]=['red','green','blue']
        
    csp=CSP(variables, domains)
    csp.add_constraint(MapColorConstraint('Western Australia', 'Northern Territory'))
    csp.add_constraint(MapColorConstraint('Western Australia', 'South Australia'))
    csp.add_constraint(MapColorConstraint('Queensland', 'South Australia'))
    csp.add_constraint(MapColorConstraint('Queensland', 'New South Wales'))
    csp.add_constraint(MapColorConstraint('New South Wales', 'South Australia'))
    csp.add_constraint(MapColorConstraint('Victoria', 'South Australia'))
    csp.add_constraint(MapColorConstraint('Victoria', 'New South Wales'))
    csp.add_constraint(MapColorConstraint('Victoria', 'Tasmania'))
    csp.add_constraint(MapColorConstraint('South Australia', 'Northern Territory'))
    csp.add_constraint(MapColorConstraint('Queensland', 'Northern Territory'))
    
    
    solution=csp.backtracking_search()
    if solution is None:
        print("No")
    else:
        print(solution)
        
