from collections import deque

graph={}
graph['start']={}
graph['start']['a']=2
graph['start']['b']=2
graph['a']={}
graph['a']['c']=2
graph['a']['fin']=2
#graph['a']['d']=
graph['b']={}
graph['b']['a']=2
#graph['b']['d']=7
graph['c']={}
graph['c']['b']=-1
graph['c']['fin']=2
##graph['d']={}
##graph['d']['a']=1
graph['fin']={}
print(graph)

infinity=float('inf')
costs={}
costs['a']=2
costs['b']=2
costs['c']=infinity
#costs['d']=infinity
costs['fin']=infinity

parents={}
parents['a']='start'
parents['b']='start'
parents['fin']=None

processed=[]
def find_lowest_cost_node ( costs ):
    lowest_cost = float ( " inf" )
    lowest_cost_node = None
    for node in costs:
        cost = costs [ node ]
        if cost < lowest_cost and node not in processed :
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node 
node=find_lowest_cost_node(costs)

while node is not None:
    print(costs,parents)
    cost=costs[node]
    neighbors=graph[node]
    print(node,cost,neighbors)
    input()
    for n in neighbors.keys():
        new_cost=cost+neighbors[n]
        print('new_cost',new_cost,'n',n,'cost[n]',costs[n],'neighbors[n]',neighbors[n])
        input()
        if costs[n]>new_cost:
            costs[n]=new_cost
            parents[n]=node
    print('af',costs,parents)
    processed.append(node)
    node=find_lowest_cost_node(costs)

print(costs['fin'])
    
def main():
    pass



if __name__ == "__main__":
    main()




#
