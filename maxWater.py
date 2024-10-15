


def maxWater(alst):

    #a*alst.index(a) for a in aslt 

##    return [[min(a,b)*(alst.index(b)-alst.index(a)) for b in alst]
##            for a in alst]

    return max([max([min(alst[i],alst[j])*(j-i) for j in range(len(alst)) if j>i]) 
            for i in range(len(alst[:-1]))])


def main():

    print(maxWater([1,8,6,2,5,4,8,3,7]))
    print(maxWater([5,1,3,4,6]))
    
   
   

    
 

if __name__ == "__main__":
    main()
