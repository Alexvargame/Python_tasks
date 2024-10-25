from __future__ import annotations
from dataclasses import dataclass
from edge import Edge

@dataclass
class WeightedEdge(Edge):
    weight:float

    def reversed(self):
        return WeightedEdge(self.v,self.u,self.weight)
    def __lt__(self, other):
        return self.weight<other.weight

    def __str__(self):
        return f'{self.u} {self.weight} -> {self.v}'

def main():
    e=WeightedEdge(1,1,100)
    print(e)

if __name__=="__main__":
    main()
