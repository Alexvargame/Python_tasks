from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod

V=TypeVar('V')
D=TypeVar('D')


class Constraint(Generic[V,D],ABC):
    def __init__(self, variables):
        self.variables=variables

    @abstractmethod
    def satisfied(self, assigment):
        pass



class CSP(Generic[V,D]):
    def __init__(self, variables,domains):
        self.variables=variables
        self.domains=domains
        self.constraints={}
        for variable in self.variables:
            self.constraints[variable]=[]
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it")
           
    def add_constraint(self,constraint):
      
        for variable in constraint.variables:
    
            if variable not in self.variables:
                raise LookupError("Variable in constraint not in CSP")
            else:
                self.constraints[variable].append(constraint)
                
    def consistent(self, variable, assigment):
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assigment):
                return False
        return True

    def backtracking_search(self, assignment={}):
# присваивание завершено, если существует присваивание
# для каждой переменной (базовый случай)
        if len(assignment) == len(self.variables):
            return assignment
# получить все переменные из CSP, но не из присваивания
        unassigned= [v for v in self.variables if v not in assignment]
        # получить все возможные значения области определения
# для первой переменной без присваивани
        first = unassigned[0]
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value
# если нет противоречий, продолжаем рекурсию
            if self.consistent(first, local_assignment):
                result=self.backtracking_search(local_assignment)
# если результат не найден, заканчиваем возвраты
                if result is not None:
                    return result
        return None 
    

if __name__=="__main__":
    pass
