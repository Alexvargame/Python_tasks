def candy(ratings):
    n = len(ratings)
    res = [1]*n
    for idx in range(1, n):
        if ratings[idx] > ratings[idx - 1]:
            res[idx] = res[idx - 1] + 1
    print(res)
    for idx in range(n - 2, -1, -1):
        print(idx, ratings[idx], ratings[idx+1])
        if ratings[idx] > ratings[idx + 1]:
            res[idx] = max(res[idx + 1] + 1, res[idx])

    return sum(res)

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', candy([1,0,2]))



if __name__ == "__main__":
    main()
