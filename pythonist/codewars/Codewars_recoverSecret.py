from itertools import permutations

def recoverSecret(triplets):

    for item in permutations(triplets, len(triplets)):
        print(item)
    

    return list(set([''.join(item) for item in permutations(triplets, len(triplets))]))

    
   
##    if not [''.join(item) for item in permutations(list(str(n)),len(str(n))) if ''.join(item)<str(n) and item[0]!='0']:
##        return -1
##    return int(max([''.join(item) for item in permutations(list(str(n)),len(str(n))) if ''.join(item)<str(n) ]))
            
def main():
    

    print(recoverSecret([['t','u','p'],
          ['w','h','i'],
          ['t','s','u'],
          ['a','t','s'],
          ['h','a','p'],
          ['t','i','s'],
          ['w','h','s']]))
 # secret = "whatisup"

 
if __name__ == "__main__":
    main()


###
