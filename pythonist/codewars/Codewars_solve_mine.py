from collections import namedtuple
from collections import deque


import random

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
class Pixel():
    def __init__(self,state,char,mines=0,mark='N'):
        self.state=state
        self.char=char
        self.mines=mines
        self.mark=mark



def pixel_mines_null(initial,open,boom,around_pixels):
    print('BFS', initial.state,initial.char)
    if boom(initial):
        return True
    initial.char=str(initial.mines)
    frontier = Queue()
    frontier.push(Pixel(initial.state,initial.char))
    explored = {initial}
    while not frontier.empty:
        current_pixel = frontier.pop()
        current_state = current_pixel.state
        for child in around_pixels(current_state):
            if child in explored:
                continue
            explored.add(child)
            if child.mines==0:
                open(child)
                frontier.push(Pixel(child.state,child.char))
    return False

def mark_pixels(M):
    c_m = M.count_mines - len(M.mark_pixels_list())
    while c_m > 0:
        print('Mark pixel?')
        m = input()
        if m == 'N':
            break
        else:
            print('Enter mark pixel:')
            a = int(input())
            b = int(input())
            M._grid[a][b].mark = 'M'
        c_m -= 1
        print(M.print_after_round())
class Miner:
    def __init__(self,t):
        self._rows=len(t)
        self._columns=len(t[0])
        self._grid=t
        self.count_mines = 6
        self.randomly_fill()

    def __str__(self):
        output=''
        for row in self._grid:
            output+=''.join([c.char  for c in row])+'\n'
        return output

    def print_after_round(self):
        output=''
        for row in self._grid:
            output += ''.join([c.mark if c.mark == 'M' else '?' if c.char=='x' else c.char for c in row]) + '\n'
            #output += ''.join([c.char if c.char!='x' else '?' for c in row])+'\n'
        return output
    def print_mark(self):
        output=''
        for row in self._grid:
            output+=''.join([c.mark if c.mark!='N' else '?' for c in row])+'\n'
        return output
    def randomly_fill(self):
        count=self.count_mines
        while count>0:
            rand_x = random.randint(0, self._rows - 1)
            rand_y = random.randint(0, self._columns - 1)
            if self._grid[rand_x][rand_y].char != 'x':
                self._grid[rand_x][rand_y].char = 'x'
                count -= 1
        return map

    def count_mines_for_pixel(self,ml):
        mines=0
        if ml.x+1<self._rows and self._grid[ml.x+1][ml.y].char=='x':
            mines+=1
        if ml.x-1>=0 and self._grid[ml.x-1][ml.y].char=='x':
            mines+=1
        if ml.y+1<self._columns and self._grid[ml.x][ml.y+1].char=='x':
            mines+=1
        if ml.y-1>=0 and self._grid[ml.x][ml.y-1].char=='x':
            mines+=1
        if ml.x+1<self._rows and ml.y+1<self._columns and self._grid[ml.x+1][ml.y+1].char=='x':
            mines+=1
        if ml.x-1>=0 and ml.y+1<self._columns and self._grid[ml.x-1][ml.y+1].char=='x':
            mines+=1
        if ml.x+1<self._rows and ml.y-1>=0 and self._grid[ml.x+1][ml.y-1].char=='x':
            mines+=1
        if ml.x-1>=0 and ml.y-1>=0 and self._grid[ml.x-1][ml.y-1].char=='x':
            mines+=1
        return mines

    def around_pixels(self,ml):
        locations=[]
        if ml.x+1<self._rows:
            locations.append(self._grid[ml.x+1][ml.y])
        if ml.x-1>=0:
            locations.append(self._grid[ml.x-1][ml.y])
        if ml.y+1<self._columns:
            locations.append(self._grid[ml.x][ml.y+1])
        if ml.y-1>=0:
            locations.append(self._grid[ml.x][ml.y-1])
        if ml.x+1<self._rows and ml.y+1<self._columns :
            locations.append(self._grid[ml.x+1][ml.y+1])
        if ml.x-1>=0 and ml.y+1<self._columns:
            locations.append(self._grid[ml.x-1][ml.y+1])
        if ml.x+1<self._rows and ml.y-1>=0:
            locations.append(self._grid[ml.x+1][ml.y-1])
        if ml.x-1>=0 and ml.y-1>=0:
            locations.append(self._grid[ml.x-1][ml.y-1])
        return locations

    def show_count_mines(self):
        output=''
        for row in self._grid:
            output+=''.join([str(c.mines) if c.char!='x' else c.char for c in row])+'\n'
        return output

    def open(self,pixel):
        #pixel.char=pixel.mines
        for p in self.around_pixels(pixel.state):
            pixel.char=str(pixel.mines)
            if p.char!='x':
                p.char=str(p.mines)
                if p.mines==0:
                    for pp in self.around_pixels(p.state):
                        pp.char=str(pp.mines)

    def boom(self,pixel):
        if pixel.char=='x':
            print('BOOM!!!')
            return True

    def mark_pixels_list(self):
        mark_pixels = []
        for p in self._grid:
            for pp in p:
                if pp.mark == 'M':
                    mark_pixels.append(pp)
        return mark_pixels
    def unnown_pixels_list(self):
        unnown_pixels = []
        for p in self._grid:
            for pp in p:
                if pp.char == '?':
                    unnown_pixels.append(pp)
        return unnown_pixels

    def check_solve(self):
        for p in self.mark_pixels_list():
            print(p.state,p.char)
            if p.char!='x':
                return False
        # for p in self.unnown_pixels_list():
        #     print(p.state)
        #     if p.char!='x':
        #         return False
        #     p.mark='M'
        return True


def make_grid(map):
    map=map.strip()
    map = map.replace(' ', '')
    width=len(map.split('\n'))
    height=len(map.split('\n')[0])
    map = map.replace('\n','')
    grid = []
    for x in range(0, height):
        grid.append([])
        for y in range(0, width):
            char = map[x * width +y]
            pixel=Pixel(state=State(x,y),char=char)
            grid[x].append(pixel)
    return grid



def solve_mine(map):
    map_array = make_grid(map)
    M=Miner(map_array)
    print(M)
    for row in range(M._rows):
        for column in range(M._columns):
            mines=M.count_mines_for_pixel(M._grid[row][column].state)
            M._grid[row][column].mines=mines
    # print(M.show_count_mines())
    #mark_pixels(M)
    print('Enter pixel:')
    c=len(M._grid)*len(M._grid[0])
    while c>0:
        a=int(input())
        b=int(input())
        if pixel_mines_null(M._grid[a][b],M.open,M.boom,M.around_pixels):
            return f'BOOM!!!'
        print(M.print_after_round())
        c-=1
        print(len(M.mark_pixels_list()),len(M.unnown_pixels_list()),len(M.mark_pixels_list())+len(M.unnown_pixels_list()),M.count_mines)
        mark_pixels(M)
        if len(M.mark_pixels_list())==M.count_mines:# or \
                # (len(M.mark_pixels_list()) + len(M.unnown_pixels_list()))==M.count_mines or\
                # len(M.unnown_pixels_list())==0:
            print("Check?")
            ans=input()
            if ans=="Y":
                print('Miner')
                print(M.print_after_round())
                if M.check_solve():
                    print(M.print_mark())
                    return f'WIN'
                else:

                    return f'BOOM!!!'
        print(M.print_after_round())
        print('Enter pixel:')

def main():


    map="""
    ? ? ? ? ? ?
    ? ? ? ? ? ?
    ? ? ? ? ? ?
    ? ? ? ? ? ?
    ? ? ? ? ? ?
    ? ? ? ? ? ?
    """
    print(solve_mine(map))



if __name__ == "__main__":
    main()

