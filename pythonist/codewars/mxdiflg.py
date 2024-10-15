from itertools import zip_longest

def mxdiflg(l1,l2):
    print(l1,l2)
    l=zip_longest(l1,l2)
    print(list(l))
        
def main():

    print(mxdiflg(['wetrwet','wt','t','qwetwet'],['erwer','t','eqrew']))

    
if __name__ == "__main__":
    main()





