

def Devide_number(n):
   alst=[i for i in range(1,n+1)]
   res=[]
   if n%3==0:
      alst=[i for i in range(1,n+1)]   
   else:
      alst=[i for i in range(1,n+1)]
      alst.insert(0,0)
      
   res=[[alst[0],alst[4],alst[8]],[alst[1],alst[5],alst[6]],[alst[2],alst[3],alst[7]]]
   for i in range(len(res)):
      j=
      while sum(res[i])!=n%3:
         res[i].append(j*5)
##         
##def Devide_number(n):
##   alst=[i for i in range(1,n+1)]
##
##   adict
##   res=[]
##   if sum([i for i in range(1,n+1)])%3==0:
##      devide_sum=int(sum([i for i in range(1,n+1)])/3)
##   else:
##      return 0
##   i=0
##   while len(alst)>1:
##      res.append([])
##      print("rrr",res, alst, max(alst),i)
##      
##      if max(alst)==devide_sum:
##         res[i].append(alst.pop(alst.index(max(alst))))
##         print("1",res, alst, len(alst),i)
##         input()
##      else:
##         print([a for a in alst if a+max(alst)==devide_sum])
##         
##         res[i].extend([alst.pop(alst.index(a)) for a in alst if a+max(alst)==devide_sum])
##         res[i].append(alst.pop(alst.index(max(alst))))
##         print("2",res, len(alst))
##         input()
##      i=i+1
         
   
   
   
  

   return res, alst


def main():
    
     print(Devide_number(8))
     print(Devide_number(14))
         
    

if __name__ == "__main__":
    main()


