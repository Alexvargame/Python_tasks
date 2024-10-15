from __future__ import annotations
from collections import namedtuple
from collections import deque

Position=namedtuple('Position','x y')

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

class Peak():
    def __init__(self,position,peak,char):
        self.position=position
        self.peak=peak
        self.char=char



def peak(plato):
    frontier=Queue()
    initial=P._grid[1][1]
    frontier.push(Peak(initial.position,initial.peak,initial.char))
    explored={initial}
    
    while not frontier.empty:
        # print('EX',explored)
        current_peak=frontier.pop()
        current_state=current_peak.position
        # if goal_test(current_state):
        #     return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,True,current_node))
    return None

def node_to_path(node):
    path=[node.position]
    while node.parent is not None:
        node=node.parent
        path.append(node.position)
    path.reverse()
    return path

class Plato:
    def __init__(self,t):
        self._rows=len(t)
        self._columns=len(t[0])
        self._grid=t

    def __str__(self):
        output=''
        for row in self._grid:
            output+=''.join([str(c) for c in row])+'\n'
        return output

    def successors(self,ml):
        locations=[]
        if ml.x+1<self._rows:
            locations.append(Position(ml.x+1,ml.y))
        if ml.x-1>=0:
            locations.append(Position(ml.x-1,ml.y))
        if ml.y+1<self._columns:
            locations.append(Position(ml.x,ml.y+1))
        if ml.y-1>=0:
            locations.append(Position(ml.x,ml.y-1))
        return locations

    def mark(self,path):
        for i in range(self._rows):
            for j in range(self._columns):
                if self._grid[i][j].position in path:
                    self._grid[i][j]='#'
                else:
                    if self._grid[i][j].passable:
                        self._grid[i][j]='0'
                    else:
                        self._grid[i][j]='1'

        # for maze_location in path:
        #     self._grid[maze_location.x][maze_location.y]='#'
        # if maze_location not in path:
        #     self._grid[maze_location.x][maze_location.y]='1'
        self._grid[self.start.position.x][self.start.position.y]='S'
        self._grid[self.goal.position.x][self.goal.position.y]='E'

    def clear(self,path):
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY

        self._grid[self.start.row][self.start.column] = 'S'
        self._grid[self.goal.row][self.goal.column] = 'E'



def print_peak_height(grid):
    output = ''
    for row in grid:
        output += ''.join([str(c.peak) for c in row]) + '\n'
    return output
def peak_height(grid):
    print(print_peak_height(grid))
    P = Plato(grid)
    for p in range(int(min(len(grid),len(grid[0]))/2)):
        for i in range(1,P._rows-1):
            for j in range(1,P._columns-1):
                if P._grid[i][j].peak>p:
                    min_peak=min([P._grid[i+1][j].peak,P._grid[i-1][j].peak,P._grid[i][j+1].peak,P._grid[i][j-1].peak])
                    P._grid[i][j].peak=min_peak+1
                    #print(P.successors(P._grid[i][j].position))
        print(p,print_peak_height(grid))

    print(print_peak_height(grid))


def make_grid(mountain):
    #mountain = mountain[0].strip().replace('\n', '')
    grid = []
    width=len(mountain[0])
    height=len(mountain)
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = mountain[x][y]
            node = Peak(position=Position(x, y), peak=1 if char == '^' else 0,char=char)
            grid[x].append(node)
    return grid

def main():
    mountain = [ "  ^^^^^^             ",
            "^^^^^^^^       ^^^   ",
            "^^^^^^^  ^^^         ",
            "^^^^^^^  ^^^         ",
            "^^^^^^^  ^^^         ",
            "---------------------",
            "^^^^^                ",
            "   ^^^^^^^^  ^^^^^^^ ",
            "^^^^^^^^     ^     ^ ",
            "^^^^^        ^^^^^^^ ",]
    grid=make_grid(mountain)
    print('eEE',make_grid(mountain))
    print(peak_height(grid))

    
    
  
    
if __name__ == "__main__":
    main()
