from collections import Counter
##from functools import reduce

def solve(astr):
   
    adict={}

    for a in astr:
        key, value=a.isupper(),a.count(a)
        l=adict.get(key,[])
        l.append(value)
        adict[key]=l
      
    
    if len(adict[False])<len(adict[True]):
        return astr.upper()
    else:
        return astr.lower()

    print([a for a in astr if a.isupper()])

def solve1(astr):
    
    if len([a for a in astr if a.isupper()])>len(astr)//2:
        
        return astr.upper()
    else:
        return astr.lower()




def main():

     print(solve('coDe'))
     print(solve1('coDe'))
     print(solve('CODe'))
     print(solve1('COdee'))
     print(solve('CoDe'))
     print(solve1('CoDe'))


if __name__ == "__main__":
    main()


