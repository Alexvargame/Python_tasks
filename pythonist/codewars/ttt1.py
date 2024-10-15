from itertools import groupby
    
def sum_pairs(ints,s):

    res=[]
    def checksum(a,b):
       # print(a,b)
        #input()
        if a+b==s:
            
            return [a,b]

    def sort(l):
        return l[2]

    for i in range(len(ints)):
        #print(i)
        res.extend(map(lambda x,y:checksum(x,y) ,ints,ints[i+1:]))
       #print(res)
       # input()
    
    res=list(filter(None, res))
    if len(res)>0:
        return [el for el , _ in groupby(res)][0]
     
##    res=[item for sublist in [[[ints[i],ints[j],j] for j in range(i+1,len(ints))
##             if sum([ints[i],ints[j]])==s] for i in range(len(ints)-1)] for item in sublist]
##    if len(res)>0:
##        res=sorted(res, key=sort)
##        return res[0][:-1]
##    else:
##       return None 

    
    
    
           
   

    



    
    
def main():
    print(sum_pairs([10, 5, 2],7))
    print(sum_pairs([10, 5, 2, 3, 7, 5],10))
    print(sum_pairs([11,3,7,5],10))
    print(sum_pairs([4,3,2,3,4],6))
##    
          
             
  
    
if __name__ == "__main__":
    main()    
