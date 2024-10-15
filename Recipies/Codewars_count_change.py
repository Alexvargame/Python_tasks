from itertools import product,combinations_with_replacement
import multiprocessing
def count_change(money, coins):
    if money==0:
        return 1

    res=[]
##    for rep in range(money//max(coins),money//min(coins)+1):
##        #r_coins=[i for i in coins if i*rep<=money]
##        print(money//max(coins),money//min(coins))
##        print('list',coins,'rep',rep)
##    
##        for item in product(coins,repeat=rep):
##            print(item)
##            if sum(item)==money:   
##                if sorted(item) not in res:
##                    res.append(sorted(item))
##    for rep in range(money//max(coins),money//min(coins)+1):      
##        for item in combinations_with_replacement(coins,rep):
##            print(item)
##            if sum(item)==money:   
##                if sorted(item) not in res:
##                    res.append(sorted(item))

##    print([items for sublist in [[item for item in combinations_with_replacement(coins,rep) if sum(item)==money]
##           for rep in range(money//max(coins),money//min(coins)+1) if len([item for item in combinations_with_replacement(coins,rep) if sum(item)==money])>0] for items in sublist])
    print(len([items for sublist in [[item for item in combinations_with_replacement(coins,rep) if sum(item)==money]
           for rep in range(money//max(coins),money//min(coins)+1) if len([item for item in
            combinations_with_replacement(coins,rep) if sum(item)==money])>0] for items in sublist]))
    return len([items for sublist in [[item for item in combinations_with_replacement(coins,rep) if sum(item)==money]
           for rep in range(money//max(coins),money//min(coins)+1) if len([item for item in
            combinations_with_replacement(coins,rep) if sum(item)==money])>0] for items in sublist])

def some_thread():
    while True:
        pool=multiprocessing.Pool()
        print(pool)
        r=pool.apply(count_change,(199,[3,5,9,15]))
        print(r)
def main():
    
     pool=multiprocessing.Pool()
     some_thread()

##    print(count_change(4,[2,1,3]))
##    print(count_change(10,[5,3,2]))
##    print(count_change(199999,[3,5,9,15]))
if __name__ == "__main__":
    main()


###
