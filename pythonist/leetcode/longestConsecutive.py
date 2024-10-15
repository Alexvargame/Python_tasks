def longestConsecutive(nums):

    setnums = set(nums)
    len_max = 0
    for n in nums:
        if n - 1 not in setnums:
            seq_len = 0
            while (n+seq_len) in setnums:
                seq_len += 1
            len_max = max(len_max, seq_len)
    return len_max










def main():
    print('res', longestConsecutive([0,3,7,2,5,8,4,6,0,1]))



if __name__ == "__main__":
    main()
