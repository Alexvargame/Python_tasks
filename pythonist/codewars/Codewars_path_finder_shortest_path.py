from __future__ import annotations
from collections import namedtuple
from math import sqrt
from collections import deque


State=namedtuple('State','y x')

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
    def __init__(self,state,passable,parent=None):
        self.state=state
        self.passable=passable
        self.parent=parent

    #
    # def __lt__(self, other):
    #     return (self.cost + self.heuristic) > (other.cost + other.heuristic)


def bfs(initial, goal_test, successors):
    print('BFS', initial)
    frontier = Queue()
    frontier.push(Node(initial.state, True,None))
    explored = {initial}

    while not frontier.empty:
        print('EX', explored)
        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child, True,current_node))
    return None
def euclidean_distance(goal):
    def distance(ml):
        xdist = ml.x - goal.x
        ydist = ml.y - goal.y
        #print('DIS',sqrt((xdist * xdist) + (ydist * ydist)))
        return sqrt((xdist * xdist) + (ydist * ydist))
    return distance
def node_to_path(node):
    path=[node.state]
    while node.parent is not None:
        node=node.parent
        print('p_node',node.state)
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
        return ml==self.goal.state

    def successors(self,ml):
        locations=[]
        if ml.y+1<self._rows and self._grid[ml.y+1][ml.x].passable:#!='X':
            locations.append(State(ml.y+1,ml.x))
        if ml.y-1>=0 and self._grid[ml.y-1][ml.x].passable:#!='X':
            locations.append(State(ml.y-1,ml.x))
        if ml.x+1<self._columns and self._grid[ml.y][ml.x+1].passable:#!='X':
            locations.append(State(ml.y,ml.x+1))
        if ml.x-1>=0 and self._grid[ml.y][ml.x-1].passable:#!='X':
            locations.append(State(ml.y,ml.x-1))
        # if ml.y+1<self._rows and ml.x+1<self._columns and self._grid[ml.y+1][ml.x+1].passable:#!='X':
        #     locations.append(State(ml.y+1,ml.x+1))
        # if ml.y-1>=0 and ml.x+1<self._columns and self._grid[ml.y-1][ml.x+1].passable:#!='X':
        #     locations.append(State(ml.y-1,ml.x+1))
        # if ml.y+1<self._rows and ml.x-1>=0 and self._grid[ml.y+1][ml.x-1].passable:#!='X':
        #     locations.append(State(ml.y+1,ml.x-1))
        # if ml.y-1>=0 and ml.x-1>=0 and self._grid[ml.y-1][ml.x-1].passable:#!='X':
        #     locations.append(State(ml.y-1,ml.x-1))
        # if ml.x==41 and ml.y==17:
        #     print(self._grid[ml.y+1][ml.x+1]!='X')
        #     print(locations)
        #     input()
        return locations

    def mark(self,path):
        for maze_location in path:
            self._grid[maze_location.y][maze_location.x]='P'
        self._grid[self.start.state.y][self.start.state.x]='S'
        self._grid[self.goal.state.y][self.goal.state.x]='G'
        # for ml in self._grid:
        #     for mll in ml:
        #         if mll not in ['P','S','G','X','.']:
        #             if self._grid[mll.state.y][mll.state.x].passable:
        #                 self._grid[mll.state.y][mll.state.x] = '.'
        #             else:
        #                 self._grid[mll.state.y][mll.state.x] = 'X'


    def clear(self,path):
        for maze_location in path:
            self._grid[maze_location.x][maze_location.y] = '.'
        self._grid[self.start.x][self.start.y] = 'S'
        self._grid[self.goal.x][self.goal.y] = 'G'


def pathFinder(maze):
    #print('NA',grid_blueprint)
    grid,start_node,end_node = make_grid(maze)

    M=Maze(grid, start_node,end_node)

    solution = bfs(M.start, M.goal_test, M.successors)
    if solution is None:
       return f'Oh for crying out loud...'
    else:
        print('Solution',solution)
        path = node_to_path(solution)
        print('Len',len(path))
        # for p in path:
        #     print(p)
        M.mark(path)
        print('Mark_path\n',M)


def make_grid(maze):
    maze=maze.strip()
    print(maze)
    width=len(maze.split('\n'))
    height=len(maze.split('\n')[0])
    print(width,height)
    maze = maze.replace('\n', '')
    grid = []
    start_node, end_node = None, None
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = maze[y * height +x]
            node = Node(state=State(x, y), passable=False if char=='W' else True)
            grid[x].append(node)
    start_node=Node(State(0,0),passable=True)
    end_node=Node(State(len(grid)-1,len(grid)-1),passable=True)
    return grid,start_node,end_node

def main():
    maze = """
.W.
.W.
...
"""

    print(pathFinder(maze))


    
    
  
    
if __name__ == "__main__":
    main()
