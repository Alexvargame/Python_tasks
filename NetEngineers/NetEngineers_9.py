
access_mode_template = [
    "switchport mode access", "switchport access vlan",
    "switchport nonegotiate", "spanning-tree portfast",
    "spanning-tree bpduguard enable"
]
port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security"
]

access_config = {
    "FastEthernet0/12": 10,
    "FastEthernet0/14": 11,
    "FastEthernet0/16": 17
}

access_config_2 = {
    "FastEthernet0/03": 100,
    "FastEthernet0/07": 101,
    "FastEthernet0/09": 107,
}
trunk_mode_template = [
    "switchport mode trunk", "switchport trunk native vlan 999",
    "switchport trunk allowed vlan"
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17]
}

def generate_access_config(intf_vlan_mapping, access_template,port_security_template=None):
    for key, value in intf_vlan_mapping.items():
        print('interface {}'.format(key))
        for item in access_template:
            if item.endswith('vlan'):
                print(item, value)
            else:
                print(item)
        if port_security_template:
            for item in port_security_template:
                print(item)

def generate_trunk_config(intf_vlan_mapping, trunk_template,port_security_template=None):
    for key, value in intf_vlan_mapping.items():
        print('interface {}'.format(key))
        for item in trunk_template:
            if item.endswith('vlan'):
                print(item, *value)
            else:
                print(item)
        if port_security_template:
            for item in port_security_template:
                print(item)


def main():

    generate_access_config(access_config, access_mode_template)
    generate_access_config(access_config_2,access_mode_template,port_security_template)
    generate_trunk_config(trunk_config,trunk_mode_template)

if __name__ == "__main__":
    main()

#
