def task5_1():
    london_co = {
        "r1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.1"
        },
        "r2": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "4451",
            "ios": "15.4",
            "ip": "10.255.0.2"
        },
        "sw1": {
            "location": "21 New Globe Walk",
            "vendor": "Cisco",
            "model": "3850",
            "ios": "3.6.XE",
            "ip": "10.255.0.101",
            "vlans": "10,20,30",
            "routing": True
        }
    }

    #print(param_list)
    dev = input('Enter the name of device: ')
    param_list=london_co[dev].keys()
    param_str=','.join(london_co[dev].keys())
    print(param_str)
    parametr = input('Enter the parametr of device ('+param_str+'):')
    if parametr.lower() in london_co[dev].keys():
        print("{}".format(london_co[dev][parametr.lower()]))
    else:
        print("Такого параметра нет")


def main():
    task5_1()


if __name__ == "__main__":
    main()

#
