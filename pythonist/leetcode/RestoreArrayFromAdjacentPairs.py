

def restoreArray(adjacentPairs):
    res = []
    start = None
    pair_dict = {}
    for pair in adjacentPairs:
        pair_dict[pair[0]] = pair_dict.get(pair[0], [])
        pair_dict[pair[0]].append(pair[1])
        pair_dict[pair[1]] = pair_dict.get(pair[1], [])
        pair_dict[pair[1]].append(pair[0])

    for key, value in pair_dict.items():
        if len(value) < 2:
            start = key
            break
    print('start', start)
    res.append(start)
    res.append(pair_dict[start][0])
    i = 0
    while i < len(pair_dict):
        print(res[-1])
        print(pair_dict[res[-1]])
        if pair_dict[res[-1]][0] != res[-2]:
            res.append(pair_dict[res[-1]][0])
        else:
            if len(pair_dict[res[-1]]) > 1:
                res.append(pair_dict[res[-1]][1])
        i += 1
    return res

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', restoreArray([[2,1],[3,4],[3,2]]))



if __name__ == "__main__":
    main()
