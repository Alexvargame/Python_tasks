def search(nums, target):

    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return True

        while l < mid and nums[l] == mid_val:
            l += 1
        while r > mid and nums[r] == mid_val:
            r -= 1
        l_val = nums[l]
        r_val = nums[r]

        if mid_val >= l_val:
            if l_val <= target < mid_val:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if mid_val < target <= r_val:
                l = mid + 1
            else:
                r = mid - 1

    return False

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', search(nums=[2,5,6,0,0,1,2], target=8))



if __name__ == "__main__":
    main()
