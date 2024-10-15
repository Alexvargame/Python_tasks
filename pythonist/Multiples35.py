

def Multiples(n, *args):

   return sum([i for i in range(1,n) if any([i%j==0 for j in args])])







def main():
    
     print(Multiples(10,3,5))
     print(Multiples(20,3,5))
     print(Multiples(10,3,4))
     print(Multiples(20,2,5))
    
   


if __name__ == "__main__":
    main()


