from __future__ import annotations
from typing import Tuple,List
from chromosome import Chromosome
from generic_algorithm import GenericAlgorithm
from random import randrange,random
from copy import deepcopy


class SimpleEquation(Chromosome):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def fitness(self):
        return 6*self.x-self.x*self.x+4*self.y-self.y*self.y
    @classmethod
    def random_instance(cls):
        return SimpleEquation(randrange(100),randrange(100))
    def crossover(self,other):
        child1=deepcopy(self)
        child2=deepcopy(other)
        child1.y=other.y
        child2.y=self.y
        return child1,child2
    def mutate(self):
        if random()>0.5:
            if random()>0.5:
                self.x+=1
            else:
                self.x-=1
        else:
            if random()>0.5:
                self.y+=1
            else:
                self.y-=1

    def __str__(self):
        return f'X: {self.x} Y:{self.y} Fitness {self.fitness()}'

def main():
    initial_population=[SimpleEquation.random_instance() for _ in range(20)]
    for i in initial_population:
        print(i)
    ga=GenericAlgorithm(initial_population=initial_population,threshold=13.0,max_generations=100,
                        mutation_chance=0.1,crossover_chance=0.7)
    result=ga.run()
    print(result)

if __name__=="__main__":
    main()
