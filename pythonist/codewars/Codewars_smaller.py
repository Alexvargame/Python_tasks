import numpy as np

        
def smaller(lst):
    res=[]
    srt=sorted(lst)
    # for i in range(len(lst)):
    #     res.append(srt.index(lst[i]))
    #     srt.remove(lst[i])
    # print(res)
    for i in range(len(lst)):
        print(srt[i:])
    print([sorted(lst[i:]) for i in range(len(lst))])
    return [sorted(lst[i:]).index(lst[i]) for i in range(len(lst))]


def main():
    print(smaller([5, 6, 7, 3, 1]))
    
    
  
    
if __name__ == "__main__":
    main()



##print([int(if_palindrom(n)) for n in sorted([items for sublist in
##                    [[reduce(lambda x,y: x*y, list(item)) if len(item)>1 else item[0]
##                      for item in combinations(args,rep)] for rep in range(2,len(args)+1)] for items in sublist])])
##def smaller(lst):
##    print(lst)
##    def f(a):
##        return list(len([a[j] for j in range(i+1,len(a)) if a[j]<a[i]]) for i in range(len(a)))
##    lst=np.array(lst)
##    return f(lst)
##    return list(len(list(lst[j] for j in range(i+1,len(lst)) if lst[j]<lst[i])) for i in range(len(lst)))
###list(len([lst[j] for j in range(i+1,len(lst)) if lst[j]<lst[i]]) for i in range(len(lst)))
##          
##   res=[]
##    print(lst)
####    for ind,l in enumerate(lst):
####        print(ind,l)
####        key,value=l,counter()
##    for i in range(len(lst)):    
##        temp=lst[i:]
##        #temp.append(lst[i])
##        print(sorted(temp))
##        print(sorted(temp).index(lst[i]))
##        print(len(temp)-sorted(temp).index(lst[i]))
##        res.append(sorted(temp).index(lst[i]))
##
##    print(res)
