
class Answer:
   def __init__(self,alst):
      self.alst=alst

      
   def FindMedian(self):
      if len(self.alst)%2!=0:
         s=0
      else: s=0.5
      for a in set(sorted(self.alst)):
         print([i for i in self.alst if i<a+s],[i for i in self.alst if i+s>a+s],a+s)
         if len([i for i in self.alst if i<a+s])==len([i for i in self.alst if i+s>a+s]):
            
            print("ddd")
            return a+s
                  
                     
   

      return None
 
   
  



def main():
    
     A=Answer([1,5,2,3,6])
     B=Answer([1,5,3,3,2,6])
     print(A.FindMedian())
     print(B.FindMedian())
  
         
    

if __name__ == "__main__":
    main()


