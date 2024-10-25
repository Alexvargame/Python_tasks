from __future__ import annotations
from typing import Tuple, List, Any
from chromosome import Chromosome
from genetic_algorithm import GeneticAlgorithm
from random import shuffle, sample
from copy import deepcopy
from zlib import compress
from sys import getsizeof
from pickle import dumps
# сжатые данные объемом 165 байт
PEOPLE: List[str] = ["Michael", "Sarah", "Joshua", "Narine", "David",
"Sajid", "Melanie", "Daniel", "Wei", "Dean", "Brian", "Murat", "Lisa"]
class ListCompression(Chromosome):
    def __init__(self, lst: List[Any]) -> None:
        self .lst: List[Any] = lst
    @property
    def bytes_compressed(self) -> int:
       return getsizeof(compress(dumps(self.lst)))
    def fitness(self) -> float:
        return 1 / self.bytes_compressed
    @classmethod
    def random_instance(cls) -> ListCompression:
        mylst: List[str] = deepcopy(PEOPLE)
        shuffle(mylst)
        return ListCompression(mylst)
    def crossover(self, other: ListCompression) -> Tuple[ListCompression,
    ListCompression]:
        childl: ListCompression = deepcopy(self)
        child2: ListCompression = deepcopy(other)
        idxl, idx2 = sample(range(len(self.lst)), k=2)
        l1, l2 = childl.lst[idxl], child2.lst[idx2]
        childl.lst[childl.lst.index(l2)], childl.lst[idx2]
        childl.lst[idx2], l2
        child2.lst[child2.lst.index(l1)], child2.lst[idxl]
        child2.lst[idxl], l1
        return childl, child2
    def mutate(self) -> None: # поменять дба элемента местами
        idxl, idx2 = sample(range(len(self.lst)), k=2)
        self.lst[idxl], self.lst[idx2] = self.lst[idx2], self.lst[idxl]
    def __str__(self) -> str:
        return f"Order: {self.lst} Bytes: {self.bytes_compressed}"

if __name__=="__main__":
    initial_population: List[ListCompression] = [ListCompression.random_instance() for _ in range(1000)]
    ga: GeneticAlgorithm[ListCompression] = GeneticAlgorithm(initial_population=initial_population, threshold=1.0,
    max_generations = 1000, mutation_chance = 0.2,
    crossover_chance = 0.7, selection_type=GeneticAlgorithm.SelectionType.TOURNAMENT)
    result: ListCompression = ga.run()
    print(result) 
