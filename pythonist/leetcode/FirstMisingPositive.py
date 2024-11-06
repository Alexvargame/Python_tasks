def firstMissingPositive(nums):
    total = len(nums)
    max_val = total + 1
    default = -max_val

    for idx, num in enumerate(nums):
        if num < 0:
            nums[idx] = 0
    print(nums)
    for num in nums:
        idx = abs(num) - 1
        if idx >= total or idx < 0:
            continue
        val = abs(nums[idx])
        nums[idx] = -val if val else default
    print(nums)
    for i in range(total):
        if nums[i] >= 0:
            return i+1

    print(nums)
    return max_val

def main():
    print('res', firstMissingPositive([3,4,-1,1]))



if __name__ == "__main__":
    main()
