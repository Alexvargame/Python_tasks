from itertools import permutations
from functools import reduce

def permutation(s):
    print(s)
    for item in permutations(list(s), len(s)):
        print(item,reduce(lambda x,y:x+y,item))

    return list(set(reduce(lambda x,y:x+y,item) for item in permutations(list(s), len(s))))
        


def main():

    
    print(permutation('ab'))
##    print(next_bigger(9))
##    print(next_bigger(111))
##    print(next_bigger(144))
##    print(next_bigger(414))
##    print(next_bigger(9091420762))
##    print(next_bigger(598848484))
    
   
    
if __name__ == "__main__":
    main()




#
