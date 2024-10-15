def climbStairs(n):
    """
    :type nums: List[int]
    :rtype: int
    """
    # from itertools import  product
    #
    # print(sum([len([item for item in product([1,2],repeat=i) if sum(item)==n]) for i in range(1, n+1)]))

    print(n//2)
    print(n)
    print(n//2)
def main():
    print('res', climbStairs(5))



if __name__ == "__main__":
    main()
