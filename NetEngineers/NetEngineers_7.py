

def task7():
    temp_lst = ['Prefix','AD/Metric','Next-Hop','Last update','Outbound Interface']
    res_dict={}
    i=1

    with open('ospf.txt') as f:
        for line in f.readlines():
            temp_dict=dict(zip(temp_lst,line.strip().split()[1:3]+line.strip().split()[4:]))
            res_dict[i]=temp_dict
            i+=1
    for value in res_dict.values():
        print_lst = []
        for k,v in value.items():
            print_lst.append(k)
            print_lst.append(str(v).strip(','))
        print(template.format(*print_lst))








def main():
    task7()


if __name__ == "__main__":
    main()

#
