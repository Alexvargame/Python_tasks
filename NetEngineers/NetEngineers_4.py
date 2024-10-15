def task1(nip):
    new_nip=nip.replace('FastEthernet0/1','GigabitEthernet0/1')
    return new_nip
def task2(mac):
    new_mac='.'.join(mac.split(':'))
    return new_mac
def task3(config):
    VLANs=config.split()[-1].split(',')
    return VLANs
def task4(vlans):
    new_vlans=sorted(list(set(vlans)))
    return new_vlans

def task5(command1,command2):
    result=sorted(list(set(task3(command1)).intersection(set(task3(command2)))))
    return result
def task6(ospf_route):
    osr=ospf_route.split()
    ip_template="""
{:<10}{:>25}
{:<10}{:>25}
{:<10}{:>25}
{:<10}{:>24}
{:<10}{:>17}
"""
    print(ip_template.format('Prefix', osr[0], 'AD/Metric', osr[1], 'Next-Hop',osr[3][:-1],'Last update',osr[4][:-1],'Outbound Interface',osr[5]))

def task7(mac):
    pass

def task8(ip):
    ip_template = '''
IP address:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
    ip_lst=[int(i) for i in ip.split('.')]
    print(ip_template.format(*ip_lst))

def main():
    mac = "AAAA:BBBB:CCCC"
    nip="ip nat inside source list ACL interface FastEthernet0/1 overload"
    config = "switchport trunk allowed vlan 1,3,10,20,30,100"
    vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
    command1 = "switchport trunk allowed vlan 1,2,3,5,8"
    command2 = "switchport trunk allowed vlan 1,3,8,9"
    ospf_route = "       10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"
    ip = "192.168.3.1"
    

    
    print(task1(nip))
    print(task2(mac))
    print(task3(config))
    print(task4(vlans))
    print(task5(command1,command2))
    print(task6(ospf_route))
    print(task7(mac))
    print(task8(ip))

if __name__ == "__main__":
    main()

#
