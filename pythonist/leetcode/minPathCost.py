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
    def __init__(self, state, parent=None, cost=0, ind=0, heuristic=0.0):
        self.state = state
        self.parent = parent
        self.heuristic = heuristic
        self.cost = cost
        self.ind = ind

    def __lt__(self, other):
        return (self.cost + self.heuristic.cost) < (other.cost + other.heuristic.cost)


def astar(initial, goal_test, successors, heuristic, moveCost):
    frontier = PriorityQueue()
    frontier.push(Node(initial.state, None, initial.cost, initial.ind, heuristic(initial.state)))
    explored = {initial.state: initial.cost}
    print('EXPL', explored)
    while not frontier.empty:

        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print('END', explored[current_node.state])
            return explored[current_node.state]#current_node
        print(current_state, current_node.cost, current_node.ind, 'RRRRRRRRRRRRR', successors(current_state))
        #input()
        cost_move = moveCost[current_node.ind]
        print(cost_move)
        for child in successors(current_state):
            new_cost = current_node.cost + heuristic(child).cost + cost_move[child.x]
            print("HEURCHILD", child, heuristic(child).cost, new_cost)
            if child not in explored or explored[child] < new_cost:
                explored[child] = new_cost
                frontier.push(Node(child, current_node, new_cost, heuristic(child).ind, heuristic(child)))
                print(explored)

    return None


def set_points(M):
    def point(ml):
        return M._grid[ml[0]][ml[1]]
    return point


# def node_to_path(node):
#     path=[node.state]
#     while node.parent is not None:
#         node=node.parent
#         path.append(node.state)
#     path.reverse()
#     return path

class Maze:
    def __init__(self, t, start, finish):
        self._rows = len(t)
        self._columns = len(t[0])
        self.start = start
        self.goal = finish
        self._grid = t

    def __str__(self):
        output = ''
        for row in list(zip(*self._grid)):
            output += ''.join([str(c) for c in row])+'\n'
        return output

    def goal_test(self, ml):
        return ml == self.goal.state

    def successors(self, ml):
        locations = []
        print(ml)
        if ml.y + 1 < self._rows:
            for i in range(self._columns):
                locations.append(State(ml.y + 1, i))
        #print('locations', ml, locations)

        return locations

    # def mark(self, path):
    #     for maze_location in path:
    #
    #         self._grid[maze_location.y][maze_location.x]='P'
    #     self._grid[self.start.state.y][self.start.state.x]='S'
    #     self._grid[self.goal.state.y][self.goal.state.x]='G'
    #     for ml in self._grid:
    #         for mll in ml:
    #             if mll not in ['P','S','G','X','.']:
    #                 if self._grid[mll.state.y][mll.state.x].passable:
    #                     self._grid[mll.state.y][mll.state.x] = '.'
    #                 else:
    #                     self._grid[mll.state.y][mll.state.x] = 'X'


    # def clear(self,path):
    #     for maze_location in path:
    #         self._grid[maze_location.x][maze_location.y] = '.'
    #     self._grid[self.start.state.x][self.start.state.y] = 'S'
    #     self._grid[self.goal.state.x][self.goal.state.y] = 'G'


def minPathCost(grid, moveCost):
    sols = []
    grid, start_node, end_node = make_grid(grid)
    print(start_node.ind, end_node.state, grid)
    width = len(grid)
    height = len(grid[0])
    print(width, height)
    for i in range(height):
        for j in range(height):
            start_node = Node(state=State(0, i), cost=grid[0][i].cost, ind=grid[0][i].ind)
            end_node = Node(state=State(width-1, j), cost=grid[width-1][j].cost, ind=grid[width-1][j].ind)
            print('STARTEND', start_node.state, end_node.state, start_node.ind, start_node.cost)

            M = Maze(grid, start_node, end_node)
            solution = astar(M.start, M.goal_test, M.successors, set_points(M), moveCost)
            print('solution', solution)
            if solution is None:
               return f'Oh for crying out loud...'
            else:
                sols.append(solution)
                print('Solution', solution)
                #path = node_to_path(solution)
                # for p in path:
                #     print(p)
                #M.mark(path)
                print('Mark_path\n', M)
                # M.clear(path)
    print(sols)
    print(min(sols))

def make_grid(grid_):
    print(grid_)
    """Convert a list of lists of 0's and 1's to a graph of Node objects"""
    width = len(grid_)
    height = len(grid_[0])
    grid = []
    start_node, end_node = Node(state=State(0, 0), cost=grid_[0][0], ind=grid_[0][0]), Node(state=State(width-1, height-1), cost=grid_[width-1][height-1], ind=grid_[width-1][height-1])
    for x in range(width):
        grid.append([])
        for y in range(height):
            cost = grid_[x][y]
            ind = grid_[x][y]
            node = Node(state=State(x, y), cost=cost, ind=ind)
            grid[x].append(node)
    return grid, start_node, end_node

def main():
    # grid_ = [[5, 3], [4, 0], [2, 1]]
    # moveCost = [[9, 8], [1, 5], [10, 12], [18, 6], [2, 4], [14, 3]]
    grid_ = [[28,35,29,5,13,17,18,23,14],[30,15,12,27,2,26,25,19,7],[1,16,34,21,9,3,20,24,8],[4,33,22,11,31,0,6,10,32]]
    moveCost = [[87,46,11,33,55,26,26,56,23],[77,56,72,49,35,18,37,66,37],[54,40,62,1,64,49,95,81,77],[80,7,76,71,91,67,75,84,52],[65,11,13,15,9,34,10,98,20],[1,95,100,61,33,47,28,100,44],[39,56,94,7,64,91,66,34,70],[37,99,62,7,23,78,74,89,97],[84,41,63,42,84,15,46,31,11],[60,36,27,25,37,18,4,90,43],[35,83,90,37,91,27,61,99,53],[85,2,98,99,67,70,38,91,68],[66,46,7,99,26,81,95,51,51],[41,96,66,84,61,73,78,28,63],[38,34,49,55,35,29,93,5,28],[3,30,80,20,23,10,93,40,33],[8,86,47,15,45,84,47,19,58],[72,5,76,82,60,50,13,74,38],[4,8,25,38,29,4,60,81,21],[65,50,74,32,9,47,71,55,14],[90,30,92,51,45,51,4,85,22],[30,56,1,45,63,72,91,73,60],[51,61,53,49,44,99,11,5,3],[24,54,91,11,5,30,50,89,44],[87,97,46,92,93,41,64,73,15],[94,76,90,80,30,9,88,8,33],[50,34,4,63,49,90,46,55,16],[10,46,80,21,97,69,70,85,31],[10,66,74,43,65,45,85,34,91],[82,26,77,10,2,5,89,39,4],[80,70,89,73,54,61,100,89,23],[30,66,80,51,3,34,92,100,63],[74,15,4,33,37,3,87,76,92],[44,43,77,99,27,1,23,10,8],[8,74,17,35,31,84,97,98,34],[99,9,28,43,55,39,93,64,93]]
    print(minPathCost(grid_, moveCost))


    
    
  
    
if __name__ == "__main__":
    main()
