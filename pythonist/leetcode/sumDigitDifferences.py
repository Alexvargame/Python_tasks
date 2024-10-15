def sum_dif(a, b):
    astr = str(a)
    bstr = str(b)
    dif = 0
    for i in range(len(astr)):
        if astr[i] != bstr[i]:
            dif += 1  # abs(int(bstr[i])-int(astr[i]))
    return dif


def sumDigitDifferences(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] != nums[j]:
                res += sum_dif(nums[i], nums[j])
    return res


def main():
    print('res', sumDigitDifferences( [13,23,12]))



if __name__ == "__main__":
    main()
