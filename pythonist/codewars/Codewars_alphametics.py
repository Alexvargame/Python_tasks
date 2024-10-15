#from csp import CSP,Constraint
#from typing import Dict,List,Optional
import string
from typing import Generic,TypeVar#,Dict,List,Optional
from abc import ABC, abstractmethod

V=str
D=int

class Constraint(ABC):
    def __init__(self,variables):
        self.variables=variables
    @abstractmethod
    def satisfied(self,assignment):
        ...
class CSP():
    def __init__(self,variables,domains):
        self.variables=variables
        self.domains=domains
        self.constraints={}
        for variable in self.variables:
            self.constraints[variable]=[]
            if variable not in self.domains:
                raise LookupError("Every variable should have a domian assigned to it")
    def add_constraint(self,constraint):
        for variable in constraint.variables:
            if variable not in self.variables:
                
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)
    def consistent(self,variable,assignment):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True

    def backtracking_search(self,assignment={}):
        if len(assignment)==len(self.variables):
            return assignment
        unassigned=[v for v in self.variables if v not in assignment]
        first=unassigned[0]
        for value in self.domains[first]:
            local_assignment=assignment.copy()
            local_assignment[first]=value
            if self.consistent(first,local_assignment):
                result=self.backtracking_search(local_assignment)
                if result is not None:
                    return result
        return None

class SendMoreMoneyConstraint(Constraint):
    def __init__(self,letters,puzzle):
        super().__init__(letters)
        self.letters=letters
        self.puzzle=puzzle

    def satisfied(self,assignment):
        if len(set(assignment.values()))<len(assignment):
            return False
        if len(assignment)==len(self.letters):
            orders=[ord(i.lower()) for i in self.variables]
            #print(orders)
            vlst=[chr(i) for i in orders]
            #print(vlst)
            
            ldict=dict(zip(vlst,[assignment[i.upper()] for i in vlst]))
            for i in range(len(vlst)):
                vlst[i]=assignment[vlst[i].upper()]
            #print(vlst)
##            s=assignment["S"]
##            e=assignment["E"]
##            n=assignment["N"]
##            d=assignment["D"]
##            m=assignment["M"]
##            o=assignment["O"]
##            r=assignment["R"]
##            y=assignment["Y"]
            #print(s,e,n,d,m,o,r,y)
            
            plst=[pi.strip().lower() for pi in self.puzzle.split('=')[0].split('+')]#+[self.puzzle.split('=')[1].strip().lower()]
            #print('plst',plst,'ld',ldict)
            wdict=dict(zip(plst,[0]*len(plst)))
            for pi in plst:
                for i in range(len(pi)):
                    #print(type(ldict[pi[i]]),pow(10,len(pi)-i-1))
                    wdict[pi]+=ldict[pi[i]]*pow(10,len(pi)-i-1)
                    #print(wdict[pi])
##            print('wd',wdict)
##            print(sum(wdict.values()))
            res=0
            for i in range(len(self.puzzle.split('=')[1].strip().lower())):
                res+=ldict[self.puzzle.split('=')[1].strip().lower()[i]]*pow(10,len(self.puzzle.split('=')[1].strip().lower())-i-1)
##            send=s*1000+e*100+n*10+d
##            more=m*1000+o*100+r*10+e
##            money=m*10000+o*1000+n*100+e*10+y
            return sum(wdict.values())==res#send+more==money
        return True
def alphametics(puzzle):
    pl=[]
    p=puzzle.split('=')
    letters=list(set(list(''.join(p[0].split('+')).replace(' ',''))+list(p[-1].strip())))
    possible_digits={}
    for letter in letters:
        possible_digits[letter]=[0,1,2,3,4,5,6,7,8,9]

    possible_digits[list(p[-1].strip())[0]]=[1]
    csp=CSP(letters,possible_digits)
    csp.add_constraint(SendMoreMoneyConstraint(letters,puzzle))
    solution=csp.backtracking_search()
    solution_str=''
    print(puzzle.split('=')[0].split('+'))
    if solution is None:
        print('No solution found')
    else:
        for w in puzzle.split('=')[0].split('+'):
                for i in w.strip():
                    solution_str+=str(solution[i])
                solution_str=solution_str+' + '
        solution_str=solution_str[:-2]+'= '
        for i in puzzle.split('=')[-1].strip():
                solution_str+=str(solution[i])
        print(solution)
        return solution_str
       #return solution
    
def main():
    print(alphametics('DO + YOU + FEEL = LUCKY'))
    #print(alphametics('SEND + MORE = MONEY'))
    #print(alphametics('ELEVEN + NINE + FIVE + FIVE = THIRTY'))
    
    
  
    
if __name__ == "__main__":
    main()



