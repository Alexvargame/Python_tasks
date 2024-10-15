import csv
from tabulate import tabulate
def  write_dhcp_snooping_to_csv(file):
    data=[]
    headers=['switch','mac','ip','vlan','interface']
    astr=file.split('_')[0]

    with open(file,'r') as f:
        reader=csv.reader(f)
        h=next(reader)
        h=next(reader)
        print(','.join(headers))
        data.append(headers)
        for row in list(reader)[:-1]:
            row_l=[r.strip() for r in row[0].split()]
            row_l.pop(2)
            row_l.pop(2)
            row_l.insert(0,astr)
            data.append(row_l)
            print(','.join(row_l))
    return data



def main():
    file_lst=['sw1_dhcp_snooping.txt','sw3_dhcp_snooping.txt','sw3_dhcp_snooping.txt']
    for file in file_lst:
        with open('new_data_file.csv','a') as f:
            writer=csv.writer(f)
            for row in write_dhcp_snooping_to_csv(file):
                writer.writerow(row)


    print(write_dhcp_snooping_to_csv('sw1_dhcp_snooping.txt'))
    print(write_dhcp_snooping_to_csv('sw2_dhcp_snooping.txt'))
    print(write_dhcp_snooping_to_csv('sw3_dhcp_snooping.txt'))



if __name__ == "__main__":
    main()

#
