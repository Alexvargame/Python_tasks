def get_middle_vals(idx, nums):
    max_val = 10 ** 6 - 1
    min_val = -max_val
    max_l = nums[idx] if idx >= 0 else min_val
    next_idx = idx + 1
    min_r = nums[next_idx] if next_idx < len(nums) else max_val
    return max_l, min_r

def findMedianSortedArrays(nums1, nums2):

    s1 = len(nums1)
    s2 = len(nums2)
    if s1 > s2:
        return findMedianSortedArrays(nums2, nums1)
    total = s1 + s2
    half, is_odd = divmod(total, 2)

    l = 0
    r = s1 - 1
    while True:
        idx1 = (r + l) // 2
        idx2 = half - idx1 - 2

        max_l_1, min_r_1 = get_middle_vals(idx1, nums1)
        max_l_2, min_r_2 = get_middle_vals(idx2, nums2)
        if max_l_1 <= min_r_2 and max_l_2 <= min_r_1:
            if is_odd:
                return min(min_r_1, min_r_2)
            return (min(min_r_1, min_r_2) + max(max_l_2, max_l_1)) / 2
        if max_l_1 > min_r_2:
            r = idx1 - 1
        else:
            l = idx1 + 1


def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', findMedianSortedArrays(nums1=[1, 3], nums2=[2]))



if __name__ == "__main__":
    main()
