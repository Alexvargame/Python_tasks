from collections import Counter
   
def pin(astr):
        desk={'a':['.','.','.','.','.','.','.','.'],
              'b':['.','.','.','.','.','.','.','.'],
              'c':['.','.','.','.','.','.','.','.'],
              'd':['.','.','.','.','.','.','.','.'],
              'e':['.','.','.','.','.','.','.','.'],
              'f':['.','.','.','.','.','.','.','.'],
              'g':['.','.','.','.','.','.','.','.'],
              'h':['.','.','.','.','.','.','.','.'],
             }
        print(desk)
        for k,v in desk.items():
                desk[k][int(astr[1])-1]='*'
                if k==astr[0]:
                        
                        desk[k]=['*']*8
                        
        for k,v in desk.items():
                print (k,v)
        return(desk)
           
def main():
 
    print(pin('a4'))
   

      
if __name__ == "__main__":
    main()


