from __future__ import annotations
from heapq import heappop,heappush
from collections import namedtuple
from math import sqrt


State = namedtuple('State','y x')

class PriorityQueue():
    def __init__(self):
        self._container=[]
    @property
    def empty(self):
        return not self._container

    def push(self, item):
        heappush(self._container, item)
    def pop(self):
        return heappop(self._container)
    def __repr__(self):
        return repr(self._container)
class Node():
    def __init__(self, state, passable, parent=None, cost=0, heuristic=0.0):
        self.state = state
        self.passable = passable
        self.parent = parent
        self.heuristic = heuristic
        self.cost = cost

    def __lt__(self, other):
        return (self.cost + self.heuristic.cost) < (other.cost + other.heuristic.cost)


def astar(initial, goal_test, successors, heuristic):
    frontier = PriorityQueue()
    frontier.push(Node(initial.state, True,None, initial.cost, heuristic(initial.state)))
    explored = {initial.state: initial.cost}
    print('EXPL', explored)
    while not frontier.empty:

        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print('END', explored[current_node.state])
            return current_node
        print(current_state, current_node.cost,' RRRRRRRRRRRRR', successors(current_state))
        # input()
        for child in successors(current_state):

            new_cost = current_node.cost + heuristic(child).cost
            print("HEURCHILD", child, heuristic(child).cost, new_cost)
            if child not in explored or explored[child] < new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, True, current_node, new_cost, heuristic(child)))
                print(explored)

    return None


def set_points(M):
    def point(ml):
        return M._grid[ml[0]][ml[1]]
    return point


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

    def goal_test(self, ml):
        return ml == self.goal.state

    def successors(self, ml):
        locations = []
        if ml.y+1 < self._rows and self._grid[ml.y+1][ml.x].passable:
            locations.append(State(ml.y+1, ml.x))
        if ml.y-1 >= 0 and self._grid[ml.y-1][ml.x].passable:
            locations.append(State(ml.y-1, ml.x))
        if ml.x+1<self._columns and self._grid[ml.y][ml.x+1].passable:
            locations.append(State(ml.y, ml.x+1))
        if ml.x-1>=0 and self._grid[ml.y][ml.x-1].passable:
            locations.append(State(ml.y, ml.x-1))
        # if ml.y+1<self._rows and ml.x+1<self._columns and self._grid[ml.y+1][ml.x+1].passable:
        #     locations.append(State(ml.y+1,ml.x+1))
        # if ml.y-1>=0 and ml.x+1<self._columns and self._grid[ml.y-1][ml.x+1].passable:
        #     locations.append(State(ml.y-1,ml.x+1))
        # if ml.y+1<self._rows and ml.x-1>=0 and self._grid[ml.y+1][ml.x-1].passable:
        #     locations.append(State(ml.y+1,ml.x-1))
        # if ml.y-1>=0 and ml.x-1>=0 and self._grid[ml.y-1][ml.x-1].passable:
        #     locations.append(State(ml.y-1, ml.x-1))
        return locations

    def mark(self,path):
        for maze_location in path:

            self._grid[maze_location.y][maze_location.x]='P'
        self._grid[self.start.state.y][self.start.state.x]='S'
        self._grid[self.goal.state.y][self.goal.state.x]='G'
        for ml in self._grid:
            for mll in ml:
                if mll not in ['P','S','G','X','.']:
                    if self._grid[mll.state.y][mll.state.x].passable:
                        self._grid[mll.state.y][mll.state.x] = '.'
                    else:
                        self._grid[mll.state.y][mll.state.x] = 'X'


    # def clear(self,path):
    #     for maze_location in path:
    #         self._grid[maze_location.x][maze_location.y] = '.'
    #     self._grid[self.start.state.x][self.start.state.y] = 'S'
    #     self._grid[self.goal.state.x][self.goal.state.y] = 'G'


def minPathSum(grid):
    #print('NA',grid_blueprint)
    grid, start_node, end_node = make_grid(grid)
    print(start_node, end_node, grid)
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         print(grid[i][j].cost)
    # for g in grid:
    #     print([gg.cost for gg in g])
    # input()
    M = Maze(grid, start_node, end_node)
    solution = astar(M.start, M.goal_test, M.successors, set_points(M))
    print('solution', solution)
    if solution is None:
       return f'Oh for crying out loud...'
    else:
        print('Solution', solution)
        path = node_to_path(solution)
        # for p in path:
        #     print(p)
        M.mark(path)
        print('Mark_path\n', M)
        # M.clear(path)

def make_grid(grid_):
    print(grid_)
    """Convert a list of lists of 0's and 1's to a graph of Node objects"""
    width = len(grid_)
    height = len(grid_[0])
    grid = []
    start_node, end_node = Node(state=State(0, 0), passable=True, cost=grid_[0][0]), Node(state=State(width-1, height-1), passable=True, cost=grid_[width-1][height-1])
    for x in range(width):
        grid.append([])
        for y in range(height):
            cost = grid_[x][y]
            node = Node(state=State(x, y), passable=True, cost=cost)
            grid[x].append(node)
    return grid, start_node, end_node

def main():
    grid_ = [[1,4,8,6,2,2,1,7],[4,7,3,1,4,5,5,1],[8,8,2,1,1,8,0,1],[8,9,2,9,8,0,8,9],[5,7,5,7,1,8,5,5],[7,0,9,4,5,6,5,6],[4,9,9,7,9,1,9,0]]

    print(minPathSum(grid_))


    
    
  
    
if __name__ == "__main__":
    main()
