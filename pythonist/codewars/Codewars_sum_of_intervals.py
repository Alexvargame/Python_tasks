def sum_of_intervals(intervals):
    idict={}     
    for el in sorted(intervals):
        key,value=el[0],el
        l=idict.get(key,[])
        l.append(value)
        idict[key]=l
    print(idict)
    li=[max(idict[key]) for key in idict.keys()]
    print(li)
    summa=li[0][1]-li[0][0]
    max_=li[0][1]
    print(summa,max_)
    for i in range(1,len(li)):
        print('LI', li[i])
        if li[i][0]>max_:
            summa+=(li[i][1]-li[i][0])
            max_=li[i][1]
            print('1www',summa,max_)
        elif li[i][1]>max_:
            summa+=li[i][1]-max_
            max_=li[i][1]
            print('2www',summa,max_)
    return summa
            
            
##
##    for key, value in idict.items():
##        if key> 
##        summa+=max(idict[key])[1]-max(idict[key])[0]
##        print(summa)
##        
    
def main():


    print(sum_of_intervals( [
     [0, 20],
   [-100000000, 10],
   [30, 40]
]))
    #print(find_all(10,3))
    #print(find_all(35,6))
    
  
  
 
if __name__ == "__main__":
    main()


###
