from itertools import product,combinations_with_replacement, permutations, combinations
from functools import reduce



##def if_palindrom(n):
##    n_dict={}
##    adstr=''
##    for l in str(n):
##        if str(n).count(l)>1:
##            if l not in adstr:
##                adstr=adstr+l*(str(n).count(l)//2)
##            if str(n).count(l)%2!=0:
##                key, value=l, str(n).count(l)
##                n_dict[key]=value%2
##        else:
##            key, value=l, str(n).count(l)
##            n_dict[key]=value
##    print(adstr)
##    print(n_dict)
##    print(''.join(reversed(sorted(adstr))),''.join(sorted(adstr)), n_dict,len(n_dict.keys()),max(n_dict.keys()))
##    if set(list(reversed(sorted(adstr))))==set('0'):
##        if len(n_dict.keys())>0:
##            return str(max(n_dict.keys()))
##        return n
##    else:
##        if len(n_dict.keys())>0:
##            return ''.join(reversed(sorted(adstr)))+max(n_dict.keys())+''.join(sorted(adstr))
##        return ''.join(reversed(sorted(adstr)))+''.join(sorted(adstr))
##        
def if_palindrom(n):
    print(n)
    print('repeat',set([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0 or str(n).count(nn)>1]))
    print('str',''.join(set([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0 or str(n).count(nn)>1])))
    str1=''.join(set([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0]))
    #print('max',max([nn for nn in str(n) if str(n).count(nn)%2!=0]))

    if set([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0 or str(n).count(nn)>1])==set('0'):
        if [nn for nn in str(n) if str(n).count(nn)%2!=0]:
            return max([nn for nn in str(n) if str(n).count(nn)%2!=0])
        return n 
        
    else:
        if [nn for nn in str(n) if str(n).count(nn)%2!=0]:
            print('max',max([nn for nn in str(n) if str(n).count(nn)%2!=0]))
            return ''.join(reversed(sorted(set([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0 or str(n).count(nn)>1]))))+max([nn
                    for nn in str(n) if str(n).count(nn)%2!=0])+''.join(sorted(set
                                    ([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0 or str(n).count(nn)>1])))
        return ''.join(reversed(sorted(set([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0 or str(n).count(nn)>1]))))+''.join(sorted(set
                                    ([nn*(str(n).count(nn)//2) for nn in str(n) if str(n).count(nn)%2==0 or str(n).count(nn)>1])))
 
                         
def numeric_palindrome(*args):
    if 0 in args:
        args=[a for a in args if a!=0]
        if len(args)<2:
            return 0
        if 1 in args:
            args=[a for a in args if a!=1]
            args.append(1)
    print(args)
    if len(args)>1:
        print([items for sublist in
                    [[reduce(lambda x,y: x*y, list(item)) if len(item)>1 else item[0]
                      for item in combinations(args,rep)] for rep in range(2,len(args)+1)] for items in sublist])
        print([int(if_palindrom(n)) for n in sorted([items for sublist in
                    [[reduce(lambda x,y: x*y, list(item)) if len(item)>1 else item[0]
                      for item in combinations(args,rep)] for rep in range(2,len(args)+1)] for items in sublist])])
        return max([int(if_palindrom(n)) for n in sorted([items for sublist in
                    [[reduce(lambda x,y: x*y, list(item)) if len(item)>1 else item[0]
                      for item in combinations(args,rep)] for rep in range(2,len(args)+1)] for items in sublist])])
    elif args:
        return args[0]
    return 0
    
            
def main():


    print(numeric_palindrome(0, 1))
    
    
if __name__ == "__main__":
    main()


##def if_palindrom(n):
##    n_dict={}
##    adstr=''
##    for l in str(n):
##        key, value=l, str(n).count(l)
##        n_dict[key]=value
##    for key, value in n_dict.items():
##        if value>1:
##            adstr=adstr+key*(value//2)
##            n_dict[key]=value%2
##            
##    [n_dict.pop(key,None) for key in [key for key in n_dict.keys() if n_dict[key]==0]]
##           
##    print('dict',n_dict)
##    let=max(n_dict.keys())
##    print('max',let)
##    print('str',adstr, ''.join(sorted(adstr)), ''.join(reversed(sorted(adstr))))
##    pal=''.join(reversed(sorted(adstr)))+str(let)+''.join(sorted(adstr))
##    print(pal)
##    return n_dict, adstr
##for l in str(n):
##        key, value=l, str(n).count(l)
##        n_dict[key]=value
##    for key, value in n_dict.items():
##        if value>1:
##            adstr=adstr+key*(value//2)
##            n_dict[key]=value%2
  #  [n_dict.pop(key,None) for key in [key for key in n_dict.keys() if n_dict[key]==0]]
