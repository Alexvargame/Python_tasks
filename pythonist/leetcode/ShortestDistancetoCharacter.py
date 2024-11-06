def shortestToChar(s,c):
    res = []
    c_idx = []
    l_idx = []
    for idx, l in enumerate(s):
        print(idx, l)
        if l != c:
            l_idx.append(idx)
        else:
            print('else', l_idx)
            for i in l_idx:
                if c_idx:
                    print(idx-i, c_idx[-1], idx,i)
                    res.append(min(idx-i, i - c_idx[-1]))
                else:
                    res.append(idx-i)
            c_idx.append(idx)
            res.append(0)
            l_idx = list()
    for i in l_idx:
        res.append(i - c_idx[-1])
    return res




def main():

    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', shortestToChar(s="loveleetcode", c="e"))



if __name__ == "__main__":
    main()
