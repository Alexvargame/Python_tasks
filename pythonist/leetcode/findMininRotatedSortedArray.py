def findMin(nums):
    l = 0
    r = len(nums)-1
    min_val = nums[0]
    while l <= r:
        min_val = min(min_val, nums[l])
        mid = (r + l) // 2
        min_val = min(min_val, nums[mid])
        if nums[l] > nums[mid]:
            r = mid - 1
        else:
            l = mid + 1


    return min_val



def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', findMin([4,5,6,7,0,1,2] ))


if __name__ == "__main__":
    main()
