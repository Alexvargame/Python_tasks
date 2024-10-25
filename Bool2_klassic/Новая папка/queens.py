from csp import CSP,Constraint
from typing import List,Dict,Optional

class QueenConstraint(Constraint[int,int]):
    def __init__(self,columns):
        super().__init__(columns)
        self.columns=columns

    def satisfied(self,assignment):
        for qc1,qr1 in assignment.items():
            for qc2 in range(qc1+1,len(self.columns)+1):
                if qc2 in assignment:
                    qr2=assignment[qc2]
                    if qr1==qr2:
                        return False
                    if abs(qr1-qr2)==abs(qc1-qc2):
                        return False
        return True


def main():
    columns=[1,2,3,4,5,6,7,8]
    rows={}
    for column in columns:
        rows[column]=[1,2,3,4,5,6,7,8]
    csp=CSP(columns,rows)
    csp.add_constraint(QueenConstraint(columns))
    solution=csp.backtracking_search()
    if solution is None:
        print('No solution found')
    else:
        print(solution)




if __name__=="__main__":
    main()
