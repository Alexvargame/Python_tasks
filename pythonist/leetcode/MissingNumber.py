def missingNumber(nums):

    nums.sort()
    deff = nums[0]
    for idx, value in enumerate(nums):
        if idx != value-deff:
            return idx+deff




def main():
    print('res',missingNumber([5,6,7, 9, 10]))


if __name__ == "__main__":
    main()
