from itertools import combinations
def subsets(nums):
    res = []
    for lis in [[list(item) for item in combinations(nums, i)] for i in range(len(nums) + 1)]:
        res.extend(lis)
    return res

def main():
    print('res', subsets(nums = [1,2,3]))



if __name__ == "__main__":
    main()
