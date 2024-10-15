def search(nums, target):
    l = 0
    r = len(nums)-1
    while l <= r:
        mid = (r + l) // 2
        mid_val = nums[mid]
        if target == mid_val:
            return mid
        if nums[l] <= mid_val:
            if target > mid_val or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < mid_val or target > nums[r]:
                 r = mid - 1
            else:
                l = mid + 1


    return -1



def main():
    #print('res', maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print('res', search([4,5,6,7,0,1,2], 0 ))


if __name__ == "__main__":
    main()
