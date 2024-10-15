

def sumIntervals(alst):
   res=[]
   res1=[]
   
   def unpack(a):
      res.extend(a)
      return res
   [unpack(a) for a in alst]
   
   for i in range(len(alst)):
      for j in range(i+1, len(alst)):
         count=0
         print(i,j, count)
         if alst[i][1]>alst[j][0]:
            print([alst[i][0],alst[j][1]])
            input()
            res1.append([alst[i][0],alst[j][1]])
            count=1
            alst.pop(j)
            alst.pop(i)
            print(alst,res1)
            print(i,j, count)
            
         
            if count==0:
               res1.append(alst[i])
               
      print(res1)
   return sorted(res)


def main():
    
     #print(sumIntervals([[1,2],[6,10],[11,15]]))
     print(sumIntervals([[1,4],[7,10],[3,5]]))
 
         
    

if __name__ == "__main__":
    main()


