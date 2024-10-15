import ipaddress


            
if __name__ == '__main__':
   
    net = ipaddress.ip_interface('123.45.67.64/27')
    print(net.network)
    for n in net:
        print(n)
        
    net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
    print(net)
    for n in net6:
        print(n)
