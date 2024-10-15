def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    #
    # res = []
    # tmp = []
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         for k in range(len(nums)):
    #             if i != j and i != k and j != k and nums[i] + nums[j] + nums[k] == 0:
    #                 if set([nums[i], nums[j], nums[k]]) not in tmp:
    #                     tmp.append(set([nums[i], nums[j], nums[k]]))
    #                     res.append([nums[i], nums[j], nums[k]])
    # return res
    result = []
    nums.sort()

    for i, a in enumerate(nums):
        if i and a == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1

        while l < r:
            three_sum = a + nums[l] + nums[r]
            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return result













def main():
    print('res', threeSum([-1,0,1,2,-1,-4]))



if __name__ == "__main__":
    main()
