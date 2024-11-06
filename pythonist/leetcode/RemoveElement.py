def removeElement(nums, val):
    k = 0
    l = len(nums)
    for idx, n in enumerate(nums[::-1]):
        print('IDX', idx, n)
        #print('1212 ', nums[:idx + l - 1], nums[idx + l - 1])
        if n == val:
            i = 0
            # while nums[idx:][i] == val:
            #     idx += i
            #     i += 1

            print('3r33', nums[:l - idx - 1], nums[:l - idx], nums[l - idx - 1])
            print('sdffd', nums[l - idx - 1:])
            nums[idx + l - 1] = nums[:idx + l - 1]
            #nums = nums[:idx + 1] + nums[idx + 1:]
            k += 1
            print('NUMS', nums)
    return k, nums

def main():
    #print('res', carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print('res', removeElement(nums=[0,1,2,2,3,0,4,2], val=2))



if __name__ == "__main__":
    main()
