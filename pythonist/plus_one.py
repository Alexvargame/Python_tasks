from functools import  reduce
   
def plus_one(alst):
        
        return alst[1:]==[i+1 for i in alst[:-1]]
   
def main():
 
    print(plus_one([-1,0,1,2,3]))
    print(plus_one([-1,0,1,3,4]))
    print(plus_one([0,1]))
    print(plus_one([1,0]))
   
if __name__ == "__main__":
    main()


