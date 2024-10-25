test_list=[29,23,58,31,56,77,43,12,65,19]
x=65
def ser(l,n):
         
    for i in test_list:
        if i==x:
            return (True, i)
print(ser(test_list,x))
def bin_ser(l,n):
    c=0
    l1=sorted(l).copy()
    if c==0:
        
        if n==l[int(len(l1)//2)]:
            c=1
        elif n>l1[int(len(l1)//2)]:
            bin_ser(l1[int(len(l1)//2)::],n)
        elif n<l1[int(len(l1)//2)]:
            bin_ser(l1[::int(len(l1)//2)],n)
   
print(bin_ser(test_list, x))
def sort1(l):
    l1=[]
    for i in range(len(l)-1):
        for j in range(i+1,len(l)-1):
            if l[i]>l[j]:
                l[i],l[j]=l[j],l[i]
        l1.append(l[i])
    return l1
print(test_list, sort1(test_list))

def pancake_sort(nums):
    arr_len = len(nums)
    while arr_len > 1:
        mi = nums.index(max(nums[0:arr_len]))
        nums = nums[mi::-1] + nums[mi+1:len(nums)]
        print(nums[mi::-1], nums[mi+1:len(nums)], nums)
        nums = nums[arr_len-1::-1] + nums[arr_len:len(nums)]
        print(nums[arr_len-1::-1], nums[arr_len:len(nums)], nums)
        arr_len -= 1
        input()
    return nums
user_input = input("Input numbers separated by a comma:\n").strip()
nums = [int(item) for item in user_input.split(',')]
print(pancake_sort(nums))

