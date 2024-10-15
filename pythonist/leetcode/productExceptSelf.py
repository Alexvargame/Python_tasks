from functools import reduce
def productExceptSelf(nums):
    # result = []
    #
    # for i in range(len(nums)):
    #     if not i:
    #         t1 = 1
    #     else:
    #         t1 = t1 * nums[i - 1]
    #     if i != len(nums) - 1:
    #         t2 = reduce(lambda x, y: x * y, nums[i + 1:])
    #     else:
    #         t2 = 1
    #     result.append(t1 * t2)
    # return result

    result = [1]*len(nums)
    prefix = 1

    for idx, num in enumerate(nums):
        result[idx] = prefix
        prefix *=num
    postfix = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *=postfix
        postfix *= nums[i]
    return result

def main():
    print('res', productExceptSelf([1,2,3,4]))



if __name__ == "__main__":
    main()
