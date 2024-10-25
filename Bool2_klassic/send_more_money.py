from csp import Constraint, CSP
from typing import Dict, List, Optional


class SendMoreMoneyConstraint(Constraint[str, int]):
    def __init__(self,letters):
        super().__init__(letters)
        self.letters=letters

    def satisfied(self, assigment):
        if len(set(assigment.values()))<len(assigment):
            return False
        if len(self.letters)==len(assigment):
            s=assigment['S']
            e=assigment['E']
            n=assigment['N']
            d=assigment['D']
            m=assigment['M']
            o=assigment['O']
            r=assigment['R']
            y=assigment['Y']
            send=s*1000+e*100+n*10+d
            more=m*1000+o*100+r*10+e
            money=m*10000+o*1000+n*100+e*10+y
            return send+more==money
        return True
            
            
if __name__=="__main__":

    
    letters=['S','E','N','D', 'M','O','R','Y']
    possible_digits={}
    for letter in letters:
        possible_digits[letter]=[0,1,2,3,4,5,6,7,8,9]
    
    possible_digits['M']=[1]
    csp=CSP(letters, possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution=csp.backtracking_search()
    if solution is None:
        print("No")
    else:
       print(solution)
                
    

