from csp import Constraint, CSP
from typing import Dict, List, Optional

class QueensConstraint(Constraint[str,str]):
    def __init__(self, columns):
        super().__init__(columns)
        self.columns=columns

    def satisfied(self, assigment):
        for q1c, q1r in assigment.items():
            for q2c in range(q1c+1, len(self.columns)+1):
                if q2c in assigment:
                    q2r=assigment[q2c]
                    if q1r==q2r:
                        return False
                    if abs(q1r-q2r)==abs(q1c-q2c):
                        return False
        return True
            
if __name__=="__main__":
    
    columns= [1, 2, 3, 4, 5, 6, 7, 8]
    rows= {}
    for column in columns:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]
    csp= CSP(columns, rows)
    csp.add_constraint(QueensConstraint(columns))
    solution=csp.backtracking_search()
    if solution is None:
        print("No")
    else:
        print(solution)
