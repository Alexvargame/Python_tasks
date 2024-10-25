from __future__ import annotations
from abc import ABC,abstractmethod
from typing import TypeVar,Type,Tuple

T=TypeVar('T',bound='Chromosome')


class Chromosome(ABC):
    @abstractmethod
    def fitness(self):
        ...

    @classmethod
    @abstractmethod
    def random_instance(cls):
        ...
    @abstractmethod
    def crossover(self,other):
        ...
    @abstractmethod
    def mutate(self):
        ...


def main():
    pass

if __name__=="__main__":
    main()
