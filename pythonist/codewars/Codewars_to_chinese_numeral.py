def to_chinese_numeral(n):
    print(n)
    numerals = {
        "-":"负",
        ".":"点",
        0:"零",
        1:"一",
        2:"二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
        10:"十",
        100:"百",
        1000:"千",
        10000:"万"
    }
    ch=[]
    if str(n)[0]=='-':
        astr=str(n)[1:]
        print('E@@#EE@E',astr)
        if abs(n) in numerals.keys() and len(astr)<3:
            return numerals['-']+numerals[abs(n)]
        ch.append(numerals['-'])
        print(ch)
    else:
        if n in numerals.keys() and len(str(n))<3:
            return numerals[n]
        astr=str(n)
    
    if '.' in astr:     
        nstr=astr.split('.')
        print('000',nstr[0],int(nstr[0]))
        print([int(nstr[0][i])*(10**(len(nstr[0])-i-1)) for i in range(len(nstr[0])) if (int(nstr[0][i-1])!=0 or int(nstr[0][i])!=0)])
        if int(nstr[0]) in numerals.keys() and len(nstr[0])<3:
            ch.append(numerals[int(nstr[0])])
            ch.append(numerals['.'])
            for d in nstr[1]:
                ch.append(numerals[int(d)])
            return ''.join(ch)
            
            
            
        if int(nstr[0])>10 and int(nstr[0])<20:
            ch.append(numerals[10])
            ch.append(numerals[abs(int(astr))%10])
            ch.append(numerals['.'])
            for d in nstr[1]:
                ch.append(numerals[int(d)])
            return ''.join(ch)
            
        
        for d in [int(nstr[0][i])*(10**(len(nstr[0])-i-1)) for i in range(len(nstr[0])) if (int(nstr[0][i-1])!=0 or int(nstr[0][i])!=0)]:
                ch.append(numerals[int(str(d)[0])])
                if len(str(d))>1:
                    ch.append(numerals[d/int(str(d)[0])])
        
        if int(nstr[0])%10==0 and ch:
            ch.pop(-1)
        print(ch)
        if len(ch)<1 or ch[-1]==numerals['-'] :
            ch.append(numerals[0])
        ch.append(numerals['.'])
        for d in nstr[1]:
            ch.append(numerals[int(d)])
        print(ch)
    else:
        print('e4tr24t',ch)
        if int(astr)>10 and int(astr)<20:
            return ''.join(ch)+numerals[10]+numerals[abs(n)%10]
        for d in [int(astr[i])*(10**(len(astr)-i-1)) for i in range(len(astr)) if (int(astr[i-1])!=0 or int(astr[i])!=0)]:
                ch.append(numerals[int(str(d)[0])])
                if len(str(d))>1:
                    ch.append(numerals[d/int(str(d)[0])])
        if int(astr)%10==0:
    
            ch.pop(-1)
        print(ch)
        
    return ''.join(ch)



def main():
    print(to_chinese_numeral(-10.000001))
##    print(to_chinese_numeral(-10306))
##    print(to_chinese_numeral(10306))
##    print(to_chinese_numeral(10006))
##    print(to_chinese_numeral(1000))
##    print(to_chinese_numeral(10))
##    print(to_chinese_numeral(10306.005))
##    
if __name__ == "__main__":
    main() 
  
