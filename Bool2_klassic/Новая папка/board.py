from __future__ import annotations
from typing import NewType,List
from abc import ABC,abstractmethod

Move=NewType('Move',int)

class Piece:
    @property
    def opposite(self):
        raise NotImplementedError("Should be implemented by subclasses")

class Board:
    @property
    @abstractmethod
    def turn(self):
        ...
    @abstractmethod
    def move(self,location):
        ...
    @property
    @abstractmethod
    def legal_moves(self):
        ...
    @property
    @abstractmethod
    def is_win(self):
        ...
    @property
    def is_draw(self):
        return (not self.is_win) and (len(self.legal_moves)==0)

    @abstractmethod
    def evaluate(self,player):
        ...

def main():
    pass



if __name__=="__main__":
    main()
