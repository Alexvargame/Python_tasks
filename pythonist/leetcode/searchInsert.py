def searchInsert(nums, target):
    """
    :type nums: List[int]
    :rtype: int
    """
    if target in nums:
        return nums.index(target)
    else:
        if target>nums[-1]:
            return len(nums)
        elif target<nums[0]:
            return 0
        else:
            l = len(nums)
            low = nums[:l//2]
            high = nums[l//2:]
            index = 0
            while index==0:
                print('1')
                if target>low[-1] and target<high[0]:
                    index =  nums.index(low[-1])+1
                if target > low[-1]:
                    l = len(high)
                    low = high[:l//2]
                    high = high[l//2:]
                else:
                    l = len(low)
                    high = low[l//2:]
                    low = low[:l//2]
            return index

def main():
    print('res', searchInsert([1, 3, 5], 2))



if __name__ == "__main__":
    main()
