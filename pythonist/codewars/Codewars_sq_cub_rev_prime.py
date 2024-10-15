from itertools import combinations


def is_prime(a,b):
    #print(a,b)
    for i in range(2, a // 2 + 1):
        #print('ee',a%i, b%i)
        if a % i == 0 or (b>i and b % i == 0):
            #print('Not prime')
            return False
    return True


def get_lst_primes(n):
    size = n//2
    lst = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if lst[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val
            lst[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(lst) if v and i>0]

def sq_cub_rev_prime(n):
    count = 0
    i = 1
    while count<n:
        i += 1
        if i%10==0:
            continue
        sq = i*i
        cub = i**3
        #print(sq, cub,int(str(sq)[::-1]),int(str(cub)[::-1]))
        # pr=is_prime(int(str(cub)[::-1]),int(str(sq)[::-1]))
        # print(int(str(cub)[::-1]),int(str(sq)[::-1]),pr)

        if is_prime(int(str(cub)[::-1]),int(str(sq)[::-1])):# and is_prime(int(str(cub)[::-1])):
            print(i)
            count += 1

    return i






#
# class Primes:
#     @staticmethod
#     def stream():
#
#     for i in range(2,a//2+1):
#         if a%i==0:
#             return False
#     return True
        


def main():

    print(sq_cub_rev_prime(5))

if __name__ == "__main__":
    main()


