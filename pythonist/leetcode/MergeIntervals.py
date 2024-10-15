def merge(intervals):
    intervals.sort()
    res = [intervals[0]]

    for idx in range(1, len(intervals)):
        start, end = intervals[idx]
        last_interval = res[-1]
        last_end = last_interval[1]
        if start > last_end:
            res.append(intervals[idx])
        else:
            last_interval[1] = max(last_end, end)

    return res

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', merge([[1,3],[2,6],[8,10],[15,18]]))



if __name__ == "__main__":
    main()
