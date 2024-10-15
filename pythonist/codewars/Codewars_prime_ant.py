def is_prime(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    return True
def smallest_div(a):
    for i in range(2,a//2+1):
        if a%i==0:
            return i
       
       

def prime_ant(n):
    pos=0
    A=[a for a in range(2,n+2)]
    print('A',A)
    index=0
    res_list=[2]
    while n>0:
        inds=(i for i in range(n))
        zip_list = list(zip(inds,A))
        print('1',zip_list)
        print('2',zip_list[n-1][1])
        print('23',res_list[-1])
        print('3',zip_list[res_list[-1]][1])
        if is_prime(zip_list[res_list[-1]][1]):
            res_list.append(p)
            index = + 1
            # print('PRIME','p-pos', p,ind,'n-ind',n,ind,'index',index)
        else:
            res_list[-1] = res_list[-1] + smallest_div(p)
            res_list(int(p / smallest_div(p)))
            index -= 1
        for ind, p in zip(inds,A):
            print('IND-P',p,ind)
            print('ZIP',list(zip(inds,A[1:])))

    #for ind, p in enumerate(a for a in range(2,n)):
            if is_prime(p):
                res_list.append(p)
                index=+1
                #print('PRIME','p-pos', p,ind,'n-ind',n,ind,'index',index)
            else:
                res_list[-1]=res_list[-1]+smallest_div(p)
                res_list(int(p/smallest_div(p)))
                index-=1
                #print('NOT_PRIME','p-pos', p,ind,'n-ind',n,ind,'index',index)
        n-=1
    print('RES_LIST',res_list)
    return index
        
    

def main():

   print(prime_ant(11))

if __name__ == "__main__":
    main()
#
# while n > 0:
#     inds = (i for i in range(index, n))
#     # print('INDS',inds,zip(inds,A))
#
#     for ind, p in zip(inds, A):
#         print('IND-P', p, ind)
#         print('ZIP', list(zip(inds, A[index + 1:])))
#         # for ind, p in enumerate(a for a in range(2,n)):
#         if is_prime(p):
#             pos = p + 1
#             index = 1
#             print('PRIME', 'p-pos', p, ind, 'n-ind', n, ind, 'index', index)
#         else:
#             p = int(p / smallest_div(p))
#             index -= 1
#             print('NOT_PRIME', 'p-pos', p, ind, 'n-ind', n, ind, 'index', index)
#     n -= 1
# return index
#



