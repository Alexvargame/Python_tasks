from itertools import permutations, product,combinations

def f(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n

def combi_sum(candidates,target):
    
    alst=[f([sorted(list(item)) for item in combinations([c for c in candidates if c<=target],i) if sum(item)==target ]) for i in range(target+1)
          if len([item for item in combinations([c for c in candidates if c<=target],i) if sum(item)==target])>0]
    return [item for sublist in alst for item in sublist]
    
    
def combiSum(nums,target):
    def dfs(i,path,cur_tar):
        if (cur_tar==0):
            ans.append(path[:])
        else:
            for j in range(i,len(nums)):
                print('AAA',j,i,nums[j-1],nums[j],cur_tar)
                input()
                if(j!=i and nums[j-1]==nums[j]):
                    print('C')
                    continue
                if (cur_tar<nums[j]):
                    break
                print('CCC',j+1,i,path+[nums[j]],cur_tar-nums[j])
                input()
                
                dfs(j+1,path+[nums[j]],cur_tar-nums[j])
    ans=[]
    nums.sort()
    print('N',nums)
    dfs(0,[],target)
    return ans

    
def main():

    print(combi_sum([10,1,2,7,6,1,5],8))
    print(combiSum([10,1,2,7,6,1,5],8))

if __name__ == "__main__":
    main()

#
