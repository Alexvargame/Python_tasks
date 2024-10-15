##from precursion import precurse
##import sys
##def triangle(row):
##    #limit=sys.setrecursionlimit(20000)
##    colors={'RR':'R','BB':'B','GG':'G','RB':'G','GB':'R','RG':'B'}
##    if len(row)==1:
##        return row    
##    else :
##        return triangle(''.join([colors.get(row[i:i+2],colors.get(row[i:i+2][::-1])) for i in range(len(row))][:-1]))
def triangle(row):
    reduce=[3**i+1 for i in range(10) if 3**i<=100000][::-1]
    print(reduce)
    for length in reduce:
        while len(row)>=length:
            row=[row[i] if row[i]==row[i+length-1] else ({"R","G","B"}-{row[i],row[i+length-1]}).pop() for i in range(len(row)-length+1)]
    return row[0]
##@precurse
##def triangle(row):
##   
##    colors={'RR':'R','BB':'B','GG':'G','RB':'G','GB':'R','RG':'B'}
##    if row==0:
##        print('e')
##        yield 0
##        
##    
##    
##    #r=yield triangle.r(''.join([colors.get(row[i:i+2],colors.get(row[i:i+2][::-1])) for i in range(len(row))][:-1]))
##    else:
##        r=yield triangle(row-1)
##        print('r',r)
##        raise StopIteration(row+r)


##def f)
##def triangle(row):
##   
##    colors={'RR':'R','BB':'B','GG':'G','RB':'G','GB':'R','RG':'B'}
##    f=
##            
##            
##            
##def gen(row):
##    for i in s:
##        yield i
        
def main():
    #gen('RGB')
      

    print(triangle('RBRGBRBGGRRRBGBBBGG'))

    
    
  
    
if __name__ == "__main__":
    main()
