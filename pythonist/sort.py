

def sort(alst):
   
   
   print([a for a in alst])
   def field(a):
      
      return a[0]
   
   return sorted(alst, key=field)





def main():
    
     print(sort([('Химия',88),('Физика',90),('Алгебра',97),('История',82)]))
         
   


if __name__ == "__main__":
    main()


