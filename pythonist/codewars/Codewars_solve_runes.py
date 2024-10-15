from operator import add,sub,mul


def func(op):
    return {'+': add, '-': sub, '*': mul}.get(op, 'error')

def solve_runes(runes):
    n1,n2,n3=1,1,1
    start=0
    operand=['+','*','-']
    
    if '--' in runes:
        n2=-1
        if runes[0]=='-':
            n1=-1
    run_lst=runes.split('=')
##    if run_lst[1][0]=='-':
##        n3=-1
    for op in operand:
        if op in run_lst[0]:
            oper=op
            run_lst[0]=[rl for rl in run_lst[0].split(op) if rl]
    print(run_lst[0])
    if oper=='-' and runes[0]=='-':
        n1=-1
    for r in run_lst[0]:
        if (r[0]=='?' and len(r)>1) or (r[0]=='-' and r[1]=='?'):
            start=1
            break
    if (run_lst[1][0]=='?' and len(run_lst[1])>1) or (run_lst[1][0]=='-' and run_lst[1][1]=='?'):
        start=1
        
    for d in reversed(range(start,10)):
        d1=int(run_lst[0][0].replace('?',str(d)))*n1
        d2=int(run_lst[0][1].replace('?',str(d)))*n2
        res=int(run_lst[1].replace('?',str(d)))
        print(n1,n2,d1,d2,func(oper)(d1,d2),res)
        if func(oper)(d1,d2)==res:
##            if d==1:
##                if func(oper)(int(run_lst[0][0].replace('?',str(2)))*n1,int(run_lst[0][1].replace('?',str(2)))*n2)==int(run_lst[1].replace('?',str(2))):
##                    return 2
            return d
    if func(oper)(d1=int(run_lst[0][0].replace('?','0'))*n1,d2=int(run_lst[0][1].replace('?','0'))*n2)== int(run_lst[1].replace('?','0')):
        return 0
    return -1
       
        

   

def main():
    
    print(solve_runes("-113*-?012=?7935?"))


if __name__ == "__main__":
    main()

