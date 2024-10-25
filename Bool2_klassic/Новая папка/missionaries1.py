from __future__ import annotations
from typing import List,Optional
from generic_search import Node,node_to_path,Queue

MAX_MIS=3
MAX_CAN=3

class MCState:
    def __init__(self,missionaries,cannibals,boat):
        self.wm=missionaries
        self.wc=cannibals
        self.em=MAX_MIS-self.wm
        self.ec=MAX_CAN-self.wc
        self.boat=boat

    def __str__(self):
        return ("On the west bank there are {} missionaries and {}cannibals.\n"
                "On the east bank there are {} missionaries and {} cannibals.\n"
                "The boat is оп the {} bank.").format(self.wm, self.wc, self.em, self.ec, ("west" if self.boat
                                                         else "east"))
    def __eq__(self):
        if MAX_MIS<MAX_CAN:
            print ('Cannibals eated missionaires')
            return False
        return True
    def goal_test(self):
        return self.is_legal and self.em==MAX_MIS and self.ec==MAX_CAN

    def is_legal(self):
        if self.wm<self.wc and self.wm>0:
            return False
        if self.em<self.ec and self.em>0:
            return False
        return True

    def successors(self) -> List[MCState]:
        sucs = []
        if self.boat:  # лодка на западном берегу
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else:  # лодка на восточном берегу
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.ec > 0) and (self.em > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]

def display_solutioп(path):
    if len(path)==0:
        return
    old_state=path[0]
    print('OS',old_state)
    for current_state in path[1:]:
        if current_state.boat:
            print("{} missionaries and {} cannibals moved form the est to the west bank.\n"
                  .format(old_state.em-current_state.em,old_state.ec-current_state.ec))
        else:
            print("{} missionaries and {} cannibals moved form the west to the est bank.\n"
                  .format(old_state.wm - current_state.wm, old_state.wc - current_state.wc))
        print('CS',current_state)
        old_state=current_state
def bfs(initial,goal_test,successors):
    frontier=Queue()
    frontier.push(Node(initial,None))
    print('I', initial)
    explored={initial}
    while not frontier.empty:
        current_node=frontier.pop()
        current_state=current_node.state
        if goal_test(current_state):
            return current_node
        for child in successors(current_state):
            if child in explored:
                continue
            explored.add(child)
            frontier.push(Node(child,current_node))
    return None
def main():
    print('a')
    start=MCState(MAX_MIS,MAX_CAN,True)
    if start.__eq__():
        solution=bfs(start,MCState.goal_test,MCState.successors)
        if solution is None:
            print("No solution found")
        else:
            path=node_to_path(solution)
            display_solutioп(path)





if __name__=="__main__":

    main()





