from itertools import combinations_with_replacement
import math
def remov_nb(n):

    #print(list(item for item in combinations_with_replacement(list(range(1,n)),2) if sum(list(range(1,n+1)))-sum(item)==item[0]*item[1]))
    res=[]
    res1=[]
    sum_=(n+1)*n/2
    t=sum_+1
    lst=[float(l) for l in range(1,n+1)]
    print(lst)
    for i in lst:
        print(i,t,t/(i+1)-1,math.modf(t/(i+1)-1))
        tm=t/(i+1)-1
        if tm.is_integer() and tm<n:
            res1.append((int(i),int(t/(i+1)-1)))

    print([(int(i),int(t/(i+1)-1)) for i in lst if math.modf(t/(i+1)-1)[0]==0.0 and math.modf(t/(i+1)-1)[1]<n])
    return res1
       
           




def main():

    print(remov_nb(26))


if __name__ == "__main__":
    main()   
    
