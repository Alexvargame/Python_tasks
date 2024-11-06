from __future__ import annotations
from heapq import heappop, heappush
from collections import namedtuple, deque
from math import sqrt





State = namedtuple('State','y x')

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
    def __init__(self, state, parent=None, char='', cost=''):
        self.state = state
        self.cost = cost
        self.parent = parent
        self.char = char
    #
    # def __lt__(self, other):
    #     return (self.char + self.heuristic.char) == (other.char + other.heuristic.char)


def astar(initial, goal_test, successors, grid, word):
    frontier = Queue()
    frontier.push(Node(initial.state, None, initial.char, initial.char))
    explored = {initial.state: initial.char}
    print('EXPL', explored)
    while not frontier.empty:

        current_node = frontier.pop()
        current_state = current_node.state
        if goal_test(current_state):
            print('END', explored[current_node.state])
            print(node_to_path(current_node))
            if current_node.cost == word:
                return current_node
        print(current_state, current_node.char,' RRRRRRRRRRRRR', successors(current_state, word))

        for child in successors(current_state, word):

            new_cost = current_node.cost + grid[child.y][child.x].char
            print("HEURCHILD", child,  new_cost)
            if child not in explored or new_cost in word:
                print('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDd')
                if new_cost not in explored.values():
                    explored[child] = new_cost
                frontier.push(Node(child, current_node, grid[child.y][child.x].char, new_cost))

    return None


class Maze:
    def __init__(self, t, start, finish):
        self._rows = len(t)
        self._columns = len(t[0])
        self.start = start
        self.goal = finish
        self._grid = t
        #self.word = word

    def __str__(self):
        output = ''
        for row in list(zip(*self._grid)):
            output += ''.join([str(c.char) for c in row])+'\n'
        return output

    def goal_test(self, ml):
        return ml == self.goal.state

    def successors(self, ml, word):
        locations = []
        if ml.y+1 < self._rows and self._grid[ml.y+1][ml.x].char in word:
            locations.append(State(ml.y+1, ml.x))
        if ml.y-1 >= 0 and self._grid[ml.y-1][ml.x].char in word:
            locations.append(State(ml.y-1, ml.x))
        if ml.x+1<self._columns and self._grid[ml.y][ml.x+1].char in word:
            locations.append(State(ml.y, ml.x+1))
        if ml.x-1>=0 and self._grid[ml.y][ml.x-1].char in word:
            locations.append(State(ml.y, ml.x-1))
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

    def print_path(self, path):
        output = ''
        for p in path:
            output += self._grid[p.y][p.x].char
        return output
def node_to_path(node):
    path = [node.state]
    while node.parent is not None:
        node=node.parent
        path.append(node.state)
    path.reverse()
    return path
def exists(board, word):
    grid, start, end = make_grid(board, word)
    M = Maze(grid, start[0], end[0])
    print(M)
    solution = astar(M.start, M.goal_test, M.successors, M._grid, word)
    if solution:
        path = node_to_path(solution)
        return M.print_path(path)

def make_grid(board, word):
    print(board)
    """Convert a list of lists of 0's and 1's to a graph of Node objects"""
    width = len(board)
    height = len(board[0])
    grid = []
    start_node, end_node = [], []
    for x in range(width):
        grid.append([])
        for y in range(height):
            char = board[x][y]
            node = Node(state=State(x, y), char=char, cost='')
            grid[x].append(node)
            if char == word[0]:
                start_node.append(node)
            elif char == word[-1]:
                end_node.append(node)
    return grid, start_node, end_node
def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', exists(board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word="ABCCED"))



if __name__ == "__main__":
    main()
