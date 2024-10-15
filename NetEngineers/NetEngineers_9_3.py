

def get_int_vlan_map(config_file_name):
    port_access={}
    port_trunk={}

    with open(config_file_name) as cf:
        cf_alst=[r.strip('\n'" ") for r in cf.read().split('!') if r.strip('\n'" ").startswith('interface')]
        for line in cf_alst:
            temp=[l.strip() for l in line.split('\n')]
            for t in temp:
                if 'access vlan' in t:
                    vlans=t.split()[-1]
                    port_access[temp[0]]=vlans

                elif 'trunk allowed vlan' in t:
                    vlans=t.split()[-1].split(',')
                    port_trunk[temp[0]]=vlans
                elif 'mode access' in t:
                    port_access[temp[0]]=1



    return (port_access,port_trunk)





def main():
   print(get_int_vlan_map('config_sw9_1.txt'))
   print()
   print(get_int_vlan_map('config_sw2.txt'))


if __name__ == "__main__":
    main()

#
