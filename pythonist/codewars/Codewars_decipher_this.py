def decipher_this(s):
    ss='ert'
    print(ss.replace(ss[0],ss[-1]).replace(ss[-1],ss[0]))
    print(ss[0])
    result=[]
    alst=s.split()
    for l in alst:
        fl=chr(int(''.join([w1 for w1 in l if w1.isdigit()])))
        print(fl)
        if len(l)<=len([w1 for w1 in l if w1.isdigit()]):
            result.append(fl)
        elif len(l)-1<=len([w1 for w1 in l if w1.isdigit()]):
            result.append(fl+l[len([w1 for w1 in l if w1.isdigit()])])
        else:
            result.append(fl+l[-1]+l[len([w1 for w1 in l if w1.isdigit()])+1:-1]+l[len([w1 for w1 in l if w1.isdigit()])])
            
               
        
    return ' '.join(result)  

    
##    return ' '.join([chr(int(''.join([w1 for w1 in w if w1.isdigit()])))+w[-1]+
##                w[len([w1 for w1 in w if w1.isdigit()])+1:-1]+w[len([w1 for w1 in w if w1.isdigit()])] if len([w1 for w1 in w if w1.isdigit()])<len(w)
##                     else chr(int(''.join([w1 for w1 in w if w1.isdigit()]))) for w in s.split()])
    

def main():
    print(decipher_this('87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri'))




if __name__ == "__main__":
    main()




#
