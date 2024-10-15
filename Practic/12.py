import re

def func(astr):



    return [astr[i-1] for i in range(1,len(astr)) if astr[i-1].isdigit() and not astr[i].isdigit() ]
    #return [int(''.join([i for i in a if i.isdigit()])) for a in astr.split() if len([i for i in a if i.isdigit()])>0] 
   
    
def func1(astr):
    #nums=re.findall('[0-9]+',astr)

    return [int(n) for n in re.findall('[0-9]+',astr)]









def main():
    
     #print(func('ff78 werwe93 we 7 rewr88'))
     print(func1('ff78 werwe93 we 7 rewr88'))
     #print(func('ff78 we94rwe93 we 7 rewr88'))
   
if __name__ == "__main__":
    main()


