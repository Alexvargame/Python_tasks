import math


def find_reverse_number(n):

    print(n,10**(len(str(n))-1),math.log10(10**(len(str(n))-1)))
    print()
    i=0
    res=0
    r=[]
    while n > 0:
        if str(i)==str(i)[::-1]:
            n-=1
            res=i
            #r.append(i)
        i+=1
    return res



    #return str(int(str(n)[0])-1)+str(n)[-1]*(len(str(n))-1)+str(int(str(n)[0])-1)
                  
        

def main():
    print(find_reverse_number(200))
        

    
  
    
if __name__ == "__main__":
    main()



