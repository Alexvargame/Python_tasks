import re

def valid_braces(string):

    symbols=[('[',']'),('(',')'),('{','}')]
    symbols1=['[','(','{']
    symbols2=[']',')','}']
    for sym in symbols:
        if string.find(sym[0])>string.find(sym[1]):
            return False
    count=0
    sym_dict={}
    for sym in symbols:
        key,value=sym,0
        sym_dict[key]=0
    print(sym_dict)
    for s in string:
        print(s)
        for key in sym_dict.keys():
            if s==key[0]:
                print('+')
                sym_dict[key]+=1
                print(sym_dict)
            elif s==key[1]:
                print('-')
                sym_dict[key]-=1
            if sym_dict[key]<0:
                return False
    return True

def main():

    
   
    print(valid_braces('(((({{'))
   
   


if __name__ == "__main__":
    main()

