def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = []
    for n in nums:
        if n not in res:
            res.append(n)

    return len(res), res


def main():
    print('res', removeDuplicates([1, 1, 2]))



if __name__ == "__main__":
    main()
