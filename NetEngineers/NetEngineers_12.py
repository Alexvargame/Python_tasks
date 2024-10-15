import ipaddress
import os
from tabulate import tabulate
def convert_range_ip_list(lst):
    res_lst=[]
    for ls in lst:
        if '-' in ls:
            first,last=ls.split('-')[0],ls.split('-')[1]
            res_lst.append(first)
            for i in range(1,int(last.split('.')[-1])-int(first.split('.')[-1])+1):
                res_lst.append(str(ipaddress.ip_address(first)+i))
        else:
            res_lst.append(ls)
    return res_lst


def ping_ipaddress(ip_lst):
    reachable=[]
    unreachale=[]
    for ip in ip_lst:
        ping = os.system("ping " + str(ip))
        if ping==0:
            reachable.append(ip)
        else:
            unreachale.append(ip)
    return (reachable,unreachale)

def print_ip_table(tup):
    columns=['Reachable','Unreachable']
    ip_s=dict.fromkeys(columns)
    ip_s["Reachable"]=tup[0]
    ip_s['Unreachable']=tup[1]

    print(tabulate(ip_s,headers='keys'))



def main():
    print_ip_table(ping_ipaddress(convert_range_ip_list(['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132'])))



if __name__ == "__main__":
    main()

#
