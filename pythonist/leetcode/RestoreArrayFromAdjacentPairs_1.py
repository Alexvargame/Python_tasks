from collections import defaultdict

def restoreArray(adjacentPairs):
    res = []
    graph = defaultdict(list)

    for a, b in adjacentPairs:
        graph[a].append(b)
        graph[b].append(a)

    for num, neigh in graph.items():
        if len(neigh) == 1:
            res.append(num)
            res.append(neigh[0])
            break
    while len(res) <= len(adjacentPairs):
        last = res[-1]
        prev = res[-2]
        neigh = graph[last]
        if neigh[0] == prev:
            res.append(neigh[1])
        else:
            res.append(neigh[0])


    return res

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', restoreArray([[2,1],[3,4],[3,2]]))



if __name__ == "__main__":
    main()
