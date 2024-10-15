from itertools import permutations

def permutation(s):

    return list(set([''.join(item) for item in permutations(list(s), len(s))]))

    
   
##    if not [''.join(item) for item in permutations(list(str(n)),len(str(n))) if ''.join(item)<str(n) and item[0]!='0']:
##        return -1
##    return int(max([''.join(item) for item in permutations(list(str(n)),len(str(n))) if ''.join(item)<str(n) ]))
            
def main():

    print(permutation('aabb'))
    print(permutation('aa'))
    print(permutation('ab'))
    print(permutation('abcd'))

 
if __name__ == "__main__":
    main()


###
