from __future__ import annotations

import time
from collections import namedtuple
from collections import deque

State=namedtuple('State','x y')

class Queue():
    def __init__(self):
        self._container=deque()
    @property
    def empty(self):
        return not self._container

    def push(self,item):
        self._container.append(item)
    def pop(self):
        return self._container.popleft()
    def __repr__(self):
        return repr(self._container)

class Letter():
    def __init__(self,state,parent=None,char='',cost=''):
        self.state=state
        self.parent=parent
        self.char=char
        self.cost=cost



def astar(initial, goal_test, successors, grid,word):
    frontier = Queue()
    frontier.push(Letter(initial.state,None,initial.char,initial.char))
    explored = {initial:initial.char}
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            if current_node.cost==word:
                return current_node
        for child in successors(current_state,word):
            new_cost=current_node.cost+grid[child.x][child.y].char
            if child not in explored and new_cost in word:
                if new_cost not in explored.values():
                    explored[child]=new_cost
                frontier.push(Letter(child,current_node,grid[child.x][child.y].char,new_cost))


    return None




def node_to_path(node):
    path=[node.state]
    while node.parent is not None:
        node=node.parent
        path.append(node.state)
    path.reverse()
    return path


class Maze:
    def __init__(self,t,start,finish):
        self._rows=len(t)
        self._columns=len(t[0])
        self.start=start
        self.goal=finish
        self._grid=t

    def __str__(self):
        output=''
        for row in list(zip(*self._grid)):
            output+=''.join([str(c) for c in row])+'\n'
        return output

    def goal_test(self,ml):
        print('GTET',ml,self.goal.state,self._grid[ml.x][ml.y].char,'ct',self._grid[ml.x][ml.y].cost,'d')
        return ml==self.goal.state

    def successors(self,ml,word):
        locations=[]
        if ml.x+1<self._rows and self._grid[ml.x+1][ml.y].char in word:
            locations.append(State(ml.x+1,ml.y))
        if ml.x-1>=0 and self._grid[ml.x-1][ml.y].char in word:
            locations.append(State(ml.x-1,ml.y))
        if ml.y+1<self._columns and self._grid[ml.x][ml.y+1].char in word:
            locations.append(State(ml.x,ml.y+1))
        if ml.y-1>=0 and self._grid[ml.x][ml.y-1].char in word:
            locations.append(State(ml.x,ml.y-1))
        if ml.x+1<self._rows and ml.y+1<self._columns and self._grid[ml.x+1][ml.y+1].char in word:
            locations.append(State(ml.x+1,ml.y+1))
        if ml.x-1>=0 and ml.y+1<self._columns and self._grid[ml.x-1][ml.y+1].char in word:
            locations.append(State(ml.x-1,ml.y+1))
        if ml.x+1<self._rows and ml.y-1>=0 and self._grid[ml.x+1][ml.y-1].char in word:
            locations.append(State(ml.x+1,ml.y-1))
        if ml.x-1>=0 and ml.y-1>=0 and self._grid[ml.x-1][ml.y-1].char in word:
            locations.append(State(ml.x-1,ml.y-1))
        return locations

    def print_path(self,path):
        output = ''
        for p in path:
            output+=self._grid[p.x][p.y].char
        return output

def find_word(testBoard,word):

    grid,start_letters,end_letters = make_grid(testBoard,word)
    for start in start_letters:
        for end in end_letters:
            M=Maze(grid, start, end)
            solution = astar(M.start, M.goal_test, M.successors,M._grid,word)
            if solution:
                path = node_to_path(solution)
                print(path)
                return M.print_path(path)
    return f'Oh for crying out loud...'


def make_grid(testBoard,word):
    width=len(testBoard)
    height=len(testBoard[0])
    grid = []
    start_letters=[]
    end_letters=[]
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = testBoard[x][y]
            node = Letter(state=State(x, y), char=char)
            grid[x].append(node)
            if char==word[0]:
                start_letters.append(node)
            if char==word[-1]:
                end_letters.append(node)
    return grid,start_letters,end_letters

def main():

    testBoard=[['L', 'H', 'A', 'R', 'R', 'G', 'A'],
               ['H', 'O', 'E', 'A', 'Y', 'C', 'L'],
               ['C', 'A', 'B', 'D', 'T', 'E', 'U'],
               ['C', 'N', 'A', 'Y', 'O', 'D', 'A'],
               ['R', 'O', 'K', 'T', 'L', 'I', 'R'],
               ['P', 'N', 'I', 'A', 'P', 'T', 'V'],
               ['G', 'M', 'S', 'E', 'M', 'R', 'S']]

    word='KITLITVSRMPAESMNONAABDTOD'
        #  KITLITVSRMPAESMNONA
    # testBoard =  [
    #   ["E","A","R","A"],
    #   ["N","L","E","C"],
    #   ["I","A","I","S"],
    #   ["B","Y","O","R"]
    # ]
    # word='RSCAREIOYBAILNEA'

    print(find_word(testBoard,word))


    
    
  
    
if __name__ == "__main__":
    main()
