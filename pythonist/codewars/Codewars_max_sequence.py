


def filter_func(n):
    if n < 0:
        return True
    return False


def max_sequence(arr):
    n = len(arr)
    if len(arr)<1:
        return 0
    max_ = -1e8
    cur_sum = 0

    for i in range(len(arr)):
        cur_sum = cur_sum + arr[i]
        if cur_sum > max_:
            max_ = cur_sum
        if cur_sum< 0:
            cur_sum = 0
    if max_ > 0:
        return max_
    return 0

# def max_sequence(arr):
#
#     max_=[]
#     for i in range(len(arr)+1):
#         for j in range(i+1,len(arr)+1):
#             if sum(arr[i:j])>0 and sum(arr[i:j])>sum(max_):
#                 max_=arr[i:j]
#     print('MAX',max_)
#     for i in range(len(arr)+1):
#         j=i+1
#         while j<len(arr)+1:
#             if j==len(arr):
#                 print(sum(arr[i:j]))
#                 return sum(arr[i:j])
#             if sum(arr[i:j])<0:
#                 break
#             else:
#                 print('arr',arr[i:j])
#                 j+=1
#
#

#     print([[sum(arr[i:j]) for j in range(i+1,len(arr)+1) ] for i in range(len(arr)+1)
#                 if len([sum(arr[i:j]) for j in range(i+1,len(arr)+1)])>0])
#     return 0
    

# if max([max([sum(arr[i:j]) for j in range(i+1,len(arr)+1) ]) for i in range(len(arr)+1)
#              if len([sum(arr[i:j]) for j in range(i+1,len(arr)+1)])>0])>0:
#     return max([max([sum(arr[i:j]) for j in range(i+1,len(arr)+1) ]) for i in range(len(arr)+1)
#             if len([sum(arr[i:j]) for j in range(i+1,len(arr)+1)])>0])
#   return 0
# sum(max_)
            
                
           




def main():

    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()   
    
##  
##    from itertools import dropwhile
##
##def filter_func(n):
##    if n<0:
##        return True
##    return False
##
##def max_sequence(arr):
##    new_arr=list(dropwhile(filter_func,arr))
##    max=[]
##    for i in range(len(new_arr)+1):
##        for j in range(i+1,len(new_arr)+1):
##            if sum(new_arr[i:j])>0 and sum(new_arr[i:j])>sum(max):
##                max=new_arr[i:j]
##    return sum(max)
##            
##
from itertools import dropwhile


def filter_func(n):
    if n < 0:
        return True
    return False


def max_sequence(arr):
    print(arr)

    if arr == []:
        return 0
    mm = max([max([sum(arr[i:j]) for j in range(i + 1, len(arr) + 1)]) for i in range(len(arr) + 1)
              if len([sum(arr[i:j]) for j in range(i + 1, len(arr) + 1)]) > 0])
    if mm > 0:
        return mm
    return 0
# # sum(max)
#
#


