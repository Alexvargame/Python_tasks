from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Edge:
    u:int
    v:int

    def reversed(self):
        return Edge(self.v, self.u)
    def __str__(self):
        return f"{self.u}->{self.v}"



if __name__=="__main__":
    pass
