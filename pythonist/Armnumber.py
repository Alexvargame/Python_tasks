

def Armnumber(n):

    
   
    
  
    return sum([int(i)**len(str(n)) for i in str(n)])==n








def main():
    
     print(Armnumber(153))
     print(Armnumber(1652))


if __name__ == "__main__":
    main()


