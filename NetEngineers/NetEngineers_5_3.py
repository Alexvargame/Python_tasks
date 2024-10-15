def task5_3():
    adict={}
    access_template = [
        "switchport mode access",
        "switchport access vlan {}",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable"
    ]

    trunk_template = [
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk allowed vlan {}"
    ]
    adict['access']=access_template
    adict['trunk']=trunk_template

    mode = input('Enter the mode(access/trunk): ')
    interface = input('Enter interface: ')
    if mode=='access':
        vlans = input('Enter the vlan: ')
    else:
        vlans = input('Enter the vlans: ')
    print('interface'.format(interface))
    print('\n'.join(adict[mode]).format(vlans))


def main():
    task5_3()


if __name__ == "__main__":
    main()

#
