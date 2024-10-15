from itertools import zip_longest
from functools import reduce
def summa(a):
    return int(a[0])+int(a[1])
def sum_strings(x, y):
    
    #print(x)
    #print(y)

    if x!='' or y!='':
        print(reduce(lambda x,y:x+y,list(sum(list(zip_longest(reversed(x),reversed(y),fillvalue='0'))[i])*pow(10,i)
                   for i in range(max(len(x),len(y))))))
                       #len(list(zip_longest(reversed(x),reversed(y),fillvalue='0')))))))
        return sum(summa(list(zip_longest(reversed(x),reversed(y),fillvalue='0'))[i])*pow(10,i)
                   for i in range(len(list(zip_longest(reversed(x),reversed(y),fillvalue='0')))))
    return 0

def main():
    
    print((sum_strings('42571245701324751324057913847591348579134857132948571349', '44573948579347563845485148651408154852064581207451244512454125688')))
    
if __name__ == "__main__":
    main()

