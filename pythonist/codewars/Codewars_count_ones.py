import time
from math import log2

DICT_MEM={1:[1],2:[1,2,1]}
def get_koef(n):
    if n not in DICT_MEM:
        DICT_MEM[n]=[1]+[sum(get_koef(n-1)[i:i+2]) for i in range(0,len(get_koef(n-1))-1)]+[1]
    return DICT_MEM[n]

def sum_lst(alst):
    sum_=0
    for index,value in enumerate(alst):
        sum_+=(index+1)*value
    return sum_

def count_ones(left,right):
    #print(log2(200000000000000))
    print(left,right)
    print(f'{right:b}',bin(right))
    print(f'{int(right/10):b}')
    print((f'{int(right/100):b}'))
    ones = 0
        #print(bin(2),bin(4),bin(8),bin(16),bin(32),bin(64))
    # for i in range(left, right+1):
    #
    #     #print(i,f'{i:b}')
    #     ones+=f'{i:b}'.count('1')
    # print('ONES',ones)
    ones=0
    t=time.time()
    left_lg=int(log2(left))
    r_lg=int(log2(right))

    print(left_lg,' ',2**left_lg,r_lg)
    if 2**left_lg>left:
        ones_lst=[sum_lst(get_koef(i)) for i in range(left_lg,r_lg)]
    else:
        ones_lst = [sum_lst(get_koef(i)) for i in range(left_lg, r_lg + 1)]
    print(time.time() - t)
    ones=sum(ones_lst)
    print(ones_lst,'ones',ones,range(2**left_lg,left),range(right,2**(r_lg+1)-1))
    for i in range(2**left_lg,left):
        #print(i,f'{i:b}')
        ones-=f'{i:b}'.count('1')
    print('ttt',ones)
    for i in range(right,2**(r_lg+1)-1):
        #print(i,f'{i:b}')
        ones-=f'{i:b}'.count('1')
    return ones-1


def main():
    #print(get_koef(5))
    # print(count_ones(1,4))
    print(count_ones(12000000,2900000000))
    print(count_ones(193303, 289384))
    # print(count_ones(9,16))
    #print(count_ones(17,32))
   # print(count_ones(121321,2000000000000000000000000000000))
  
  
  
 
if __name__ == "__main__":
    main()


###
# def count_ones(left,right):
#     ones=0
#     #print(bin(2),bin(4),bin(8),bin(16),bin(32),bin(64))
#     for i in range(left, right+1):
#         print
#         #print(f'{i:b}')
#         ones+=f'{i:b}'.count('1')
#     return ones
