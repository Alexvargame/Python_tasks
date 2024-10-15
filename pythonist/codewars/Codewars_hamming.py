from math import log2,sqrt
from itertools import product
import sympy
#mem={1:1,2:2,3:3,4:4,5:5,6:6,7:8,8:9,9:10,10:12,11:15,12:16,13:18,14:20,15:24,16:25,17:27,18:30,19:32}
mem={1:1,2:2,3:3,4:4,5:5}#,2:[1,0,0],3:[0,1,0],4:[2,0,0],5:[0,0,1],6:[1,1,0],7:[3,0,0],8:[0,2,0],9:[1,0,1],10:[2,1,0],11:[0,1,1],12:[4,0,0],13:[1,2,0]}
ukaz=[1,1,1]


    
def divisions(m):
    div=[]
    for d in range(2,int(m/2)+1):
        if m%d==0:
            if d not in [2,3,5] and (d%2!=0 and d%3!=0 and d%5!=0):
                return []
            else:
                div.append(d)                
    return div
            
def hamming(n):
    if n not in mem:
        count=6
        while count<n+1:
            variants=[2*ukaz[0],3*ukaz[1],5*ukaz[2]]
            print(variants,min(variants))
            if min(variants) not in mem.values():
                if set(divisions(min(variants))).intersection({2,3,5}):
                    print('PV',sympy.factorint(min(variants)))
                    mem[count]=min(variants)
                    count+=1
                print(mem)
                ind=variants.index(min(variants))
                ukaz[ind]+=1

                
            else:
                ind=variants.index(min(variants))
                ukaz[ind]+=1
        return mem[n]
    else:
        return mem[n]

def main():

   print(hamming(8))

if __name__ == "__main__":
    main()



##if n not in mem:
##        count=0
##        d=pow(2,mem[max(mem)][0])*pow(3,mem[max(mem)][1])*pow(5,mem[max(mem)][2])
##        while count<n+1-len(mem):           
##            print(d)
##            lli=list(item for item in product(range(int(log2(d))),repeat=3) if pow(2,item[0])*pow(3,item[1])*pow(5,item[2])==d+1)
##            print('d',d,'lli',lli,len(mem),len(lli))
##            if len(lli)>0:
##                print('ll',list(lli[0]))
##                
##                mem[max(mem)+1]=list(lli[0])
##                d=pow(2,mem[max(mem)][0])*pow(3,mem[max(mem)][1])*pow(5,mem[max(mem)][2])
##                count=+1
##            else:
##              
##                if pow(2,int(log2(d))+1)==d+1:
##                    mem[max(mem)+1]=[int(log2(d))+1,0,0]
##                    d=pow(2,mem[max(mem)][0])*pow(3,mem[max(mem)][1])*pow(5,mem[max(mem)][2])
##                    count=+1
##                else:
##                    d=d+1
##                
##    
##        print(mem)
##        return pow(2,mem[n][0])*pow(3,mem[n][1])*pow(5,mem[n][2])
##    else:
##        return pow(2,mem[n][0])*pow(3,mem[n][1])*pow(5,mem[n][2])
##
##
