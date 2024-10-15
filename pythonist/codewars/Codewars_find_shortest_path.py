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

class Node():
    def __init__(self,position,passable,parent=None):
        self.position=position
        self.passable=passable
        self.parent=parent


def bfs(initial,goal_test,successors):
    print('BFS',initial)
    frontier=Queue()
    frontier.push(Node(initial.position,True,None))
    explored={initial}
    
    while not frontier.empty:
        # print('EX',explored)
        current_node=frontier.pop()
        current_state=current_node.position
        if goal_test(current_state):
            return current_node
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

class Maze:
    def __init__(self,t,start,finish):
        self._rows=len(t)
        self._columns=len(t[0])
        self.start=start
        self.goal=finish
        self._grid=t

    def __str__(self):
        output=''
        for row in self._grid:
            output+=''.join([str(c) for c in row])+'\n'
        return output

    def goal_test(self,ml):
        return ml==self.goal.position

    def successors(self,ml):
        locations=[]
        if ml.x+1<self._rows and self._grid[ml.x+1][ml.y].passable:
            locations.append(Position(ml.x+1,ml.y))
        if ml.x-1>=0 and self._grid[ml.x-1][ml.y].passable:
            locations.append(Position(ml.x-1,ml.y))
        if ml.y+1<self._columns and self._grid[ml.x][ml.y+1].passable:
            locations.append(Position(ml.x,ml.y+1))
        if ml.y-1>=0 and self._grid[ml.x][ml.y-1].passable:
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



def find_shortest_path(grid, start_node, end_node):
    M=Maze(grid, start_node, end_node)
    solution = bfs(M.start, M.goal_test, M.successors)
    print('SOL',solution)
    if solution is None:
        print('No solutions found')
    else:
        path = node_to_path(solution)
        M.mark(path)
        print(M)

def make_grid(grid_blueprint, width, height):
    grid_blueprint = grid_blueprint.strip().replace('\n', '')
    grid = []
    start_node, end_node = None, None
    for x in range(0, width):
        grid.append([])
        for y in range(0, height):
            char = grid_blueprint[x * width + y]
            node = Node(position=Position(x, y), passable=False if char == '1' else True)
            if char == 'S':
                start_node = node
            elif char == 'E':
                end_node = node
            grid[x].append(node)

    return grid, start_node, end_node 
def main():
    mountain = """
S0110
01000
01010
00010
0001E
"""
    grid, start_node, end_node=make_grid(grid1_blueprint,5,5)
    print('eEE',make_grid(grid1_blueprint,5,5))
    print(find_shortest_path(grid, start_node, end_node))
    pass # print(cheapest_path([[1,9,1],[2,9,1],[2,1,1]], (0,0), (0,2)))

    
    
  
    
if __name__ == "__main__":
    main()
