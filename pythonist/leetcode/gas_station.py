def canCompleteCircuit(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    total = 0
    current = 0
    ans = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]
        current += gas[i] - cost[i]
        print(total, current, ans, i)
        if current < 0:
            current = 0
            ans = i + 1
    return ans if total >= 0 else -1

def main():
    print('res', canCompleteCircuit([1, 2, 3, 4, 5],[3, 4, 5, 1, 2]))



if __name__ == "__main__":
    main()
