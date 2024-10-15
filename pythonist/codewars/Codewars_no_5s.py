from math import *

def pwr(a,b):
    pw=[]
    for d in range(1,floor(max(abs(a+1),abs(b+1))**(1/5))+1):
        pw.append(d**5)
        pw.append((-d)**5)
    return pw

def no_5s(a, b):
    res=[]
    pw=pwr(a,b)
    print(abs(a+1),abs(b+1),min(abs(a+1),abs(b+1)),max(abs(a+1),abs(b+1)))
    print(pw)
    if a>b:
        return 0
    return len([d for d in range(a,b+1) if '5' not in str(d) and d%5!=0 and len(str(d).strip('-'))!=5 and d not in pw])
    
def main():
    print(no_5s(-11111, 11110))


       
if __name__ == "__main__":
    main()
        
##    for d in range(a,b+1):
##        if '5' not in str(d) and d%5!=0 and len(str(d).strip('-'))!=5 and d not in pw:
##            res.append(d)
##    return res
