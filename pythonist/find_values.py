from functools import  reduce
   
def find_values(*args):
        res=reduce(lambda x,y:set(x)&set(y), args)
        return list(res)
   
def main():
 
    print(find_values([11,10,3],[10,3,5,11],[11,10]))
    print(find_values([1,10,3],[6,2,5,11],[4,'hhi']))
    print(find_values([8,7,5,'hi'],[8,'hi'],[4,'hi']))


if __name__ == "__main__":
    main()


