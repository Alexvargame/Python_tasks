def getLastMoment(n, left, right ):
    res = 0
    for pos in right:
        res = max(res, n-pos)
    for pos in left:
        res = max(res, pos)
    return res

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', getLastMoment(4, left=[4, 3], right=[0, 1]))



if __name__ == "__main__":
    main()
