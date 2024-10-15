dep1=[(6,6),(8,8)]
dep2=[(1,8),(4,9)]

def square(l1,l2):
    l=[]
    max_=0
    for k in range(2):
        for i in l1:
            for j in l2:
                if max_<i[0]-j[0]:
                    max_=i[0]-j[0]
        l.append(max_)
    return max(l)**2
print(square(dep1,dep2))
            
        
