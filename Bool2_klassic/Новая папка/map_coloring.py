from csp import CSP,Constraint
from typing import Dict,List,Optional

class MapColoringConstraint(Constraint[str,str]):
    def __init__(self,place1,place2):
        super().__init__([place1,place2])
        self.place1=place1
        self.place2=place2
    def satisfied(self,assignment):
        if self.place1 not in assignment or self.place2 not in assignment:
            return True
        return assignment[self.place1]!=assignment[self.place2]

def main():
    variables = ["Western Australia", "Northern Territory", "South Australia", "Queensland", "New South Wales", "Victoria", "Tasmania"]
    domains={}
    for variable in variables:
        domains[variable]=['red','green','blue']
    csp=CSP(variables,domains)
    csp.add_constraint(MapColoringConstraint("Western Australia","Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Western Australia","South Australia"))
    csp.add_constraint(MapColoringConstraint("South Australia","Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland","Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("New South Wales","South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))
    solution=csp.backtracking_search()
    if solution is None:
        print('No solution found')
    else:
        print(solution)





if __name__=="__main__":
    main()
