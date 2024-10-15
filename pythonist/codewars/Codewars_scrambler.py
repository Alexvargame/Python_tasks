from itertools import permutations

def scramble(s1,s2):
    #if any([True for item in permutations(s1,len(s2)) if ''.join(item)==s2]):
    print([l for l in s2 if s1.count(l)>=s2.count(l)])
    if len([True for l in s2 if s1.count(l)>=s2.count(l)])==len(s2):
            return True

    return False

##    while True:
##        for l in s2:
##            yield s1.count(l)>=s2.count(l)
##            
##    return False
    


def main():

    g1=scramble('katas', 'steak')
    print(g1)

    print(scramble('katas', 'steak'))
    print(scramble('cedewaraaossoqqyt', 'codewars'))
    print(scramble('rkqodlw', 'world'))


 
if __name__ == "__main__":
    main()


###
##def scramble(s1,s2):
##    for c in set(s2):
##        if s1.count(c) < s2.count(c):
##            return False
##    return True
##
##def scramble(s1,s2):
##    return all( s1.count(x) >= s2.count(x) for x in set(s2))
