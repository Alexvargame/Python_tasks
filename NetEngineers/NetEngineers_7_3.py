import re
from rich import inspect
def sort_list(r):
    return int(r[0])

def task7_3():
    temp="""{:<2}  {:>3}  {} """
    res=[]
    with open('CAM_table.txt') as f:
        for line in f.readlines():
            regex=r'[0-9]{2,3}\s+\w{4}\.\w{4}\.\w{4}\s+DYNAMIC\s+\w{3}\/[0-9]'
            #print('Re',re.findall(regex,line))
            if re.findall(regex,line):
                line.replace('DYNAMIC','')
                res.append(line.replace('DYNAMIC','').rstrip().split())
    res=sorted(res,key=sort_list)
    for r in res:
        s=' '*(len(res[-1][0])-len(r[0]))
        astr='{:>1}'+s+'{:>18}'+'{:>8}'
        print(astr.format(*r))
    vlan=input('Enter vlan:')
    for r in res:
        if r[0]==vlan:
            s = ' ' * (len(res[-1][0]) - len(r[0]))
            astr = '{:>1}' + s + '{:>18}' + '{:>8}'
            print(astr.format(*r))
    inspect(res)
def main():
    task7_3()


if __name__ == "__main__":
    main()

#
