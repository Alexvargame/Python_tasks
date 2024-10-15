from collections import deque

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

def successors(curr):

    success=[]
    success.append(2*curr+1)
    success.append(3*curr+1)
    print('CURR',curr,'s_lst',success)
    return success

def dbl_linear(n):
    print('BFS',1)
    res=1
    frontier=[]#Queue()
    frontier.append(1)#push(1)
    explored=[1]

    while len(frontier)>0:#not frontier.empty:
        print('EX',explored)
        print("FRONIWER", frontier)
        print('MIN',min(frontier))
        current_num=frontier.pop(-1)
        if len(explored)>n:
            res=sorted(explored)[n]
            if res<current_num:
                return res
           # print('f',max(frontier._container))
            #return sorted(explored)[n]
        for child in successors(current_num):
            print('C',child)
            if child in explored:
                continue
            if len(explored)==n and child>sorted(explored)[n-1]:
                continue
            frontier.append(child)#push(child)
            explored.append(child)
        frontier=sorted(frontier,reverse=True)
        print('f',frontier)
    return 0

def main():
    print(dbl_linear(1000))
    
    
  
    
if __name__ == "__main__":
    main()
