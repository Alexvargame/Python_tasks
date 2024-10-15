from math import sqrt

def is_prime(n):
    for i in range(2,int(round(sqrt(n),0)+1)):
        if n%i==0:
            return False
    return True
    
def gap(g,n,m):
    list_prime=[]
  
    for d in range(n,m+1):
        if is_prime(d):
            list_prime.append(d)
            if len(list_prime)>1:
     #           print(d,list_prime, list_prime[-2])
    ##            for p in list_prime:
    ##                print(d,p)
                if d-list_prime[-2]==g:
                    return [list_prime[-2],d]
    return None

    
        


def main():

    print(gap(2,3,50))
    print(gap(1000,30000,100000))
       
    
if __name__ == "__main__":
    main()




#
