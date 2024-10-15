

def task6():
    mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
    print([m.replace(':','.') for m in mac])

    ip=input("Enter ip:")

    if len([d for d in ip.split('.') if d.isdigit() and 0<int(d)<256])==4 :
        if ip=='255.255.255.255':
            print('local broadcast')
        elif ip=='0.0.0.0':
            print('unassigned')
        elif 0<int(ip.split('.')[0])<224:
            print('unicast')
        elif 223<int(ip.split('.')[0])<240:
            print('multicast')
        else:
            print('unused')
    else:
        print('Wrong')
        ip = input("Enter ip at once:")
        if len([d for d in ip.split('.') if d.isdigit() and 0 < int(d) < 256]) == 4:
            if ip == '255.255.255.255':
                print('local broadcast')
            elif ip == '0.0.0.0':
                print('unassigned')
            elif 0 < int(ip.split('.')[0]) < 224:
                print('unicast')
            elif 223 < int(ip.split('.')[0]) < 240:
                print('multicast')
            else:
                print('unused')
        else:
            print('Wrong')



def main():
    task6()


if __name__ == "__main__":
    main()

#
