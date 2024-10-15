from itertools import permutations, product,combinations

def f(l):
    if l==sorted(l):
        return True
    return False


def combi_sum(candidates):
    
    alst=[[list(item) for item in combinations(candidates,i) if f(list(item))] for i in range(1,len(candidates)+1)
          if len([item for item in combinations(candidates,i)])>0]
    return max([len(item) for sublist in alst for item in sublist])
    
    
def lengthoflis(nums):
    total_number=len(nums)
    dp=[0 for _ in range(total_number)]
    print('dp',dp)
    for i in range(1,total_number):
        for j in range(i):
            print('i',i,'j',j,'[j]',nums[j],'[i]',nums[i])
            if nums[j]<nums[i]:
                
                dp[i]=max(dp[i],dp[j]+1)
                print('1dp',dp)
    return max(dp)+1
       


    
def main():

    print(combi_sum([10,9,2,5,3,7,101,18]))
    print(lengthoflis([10,9,2,5,3,7,101,18]))

if __name__ == "__main__":
    main()

#
