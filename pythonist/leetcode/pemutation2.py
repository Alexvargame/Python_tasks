def permuteUnique(nums):

    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    n=4
    # from itertools import permutations, combinations_with_replacement, combinations, product
    # from functools import reduce
    # lst = [list(set([reduce(lambda x,y: x*y, item) for item in combinations_with_replacement(nums, i)])) for i in range(1,4)]
    # print(lst)
    # print(*lst)
    # for l in lst:
    #     for d in l:
    #         if n/d==1:
    #             return True
    while n>1:
        for d in [2,3,5]:
            print(d,n/d, (n/d).is_integer())
            if n/d==1.0:
                return True
            elif (n/d).is_integer():
                n=int(n/d)
                print('f',n)
                continue
            print(n)
    return False

    print([item for item in combinations_with_replacement(nums, len(nums))])
    print([item for item in combinations(nums, len(nums))])
    print([item for item in product(nums)])

def main():
    print('res', permuteUnique([2, 3, 5]))



if __name__ == "__main__":
    main()
