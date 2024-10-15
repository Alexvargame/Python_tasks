import os
import sqlite3
import re
import yaml

from tabulate import tabulate
def create_db(name):

    print(f'Создаю базу {name}')
    con = sqlite3.connect(name)
    with open('dhcp_snooping_schema1.sql','r') as dh:
        readlines=[r.strip('\n').strip() for r in dh.readlines() if r.strip('\n')!='']
        commands=re.findall(r'\bcreate[\s\w]+\([\s\w\,\(\)]+\)\;',''.join(readlines))
        for command in commands:
            con.execute(str(command))


def add_data(name):
    if not os.path.isfile(name):
        print(f' База данных {name} не существует. Ее нужно создать' )
        create_db(name)
    else:
        print(f'Открываю базу {name}')
        con = sqlite3.connect(name)
        data=[]
        print(f' Добавляю данные в таблицу switches')
        with open('switches.yml') as sw:
            sw_dict=yaml.safe_load(sw)
            for key,value in sw_dict.items():
                for k,v in value.items():
                    data.append((k,v))
        query='INSERT into switches values (?,?)'
        try:
            con.executemany(query,data)
        except:
            pass
        con.commit()
        print(f' Добавляю данные в таблицу dhcp')
        con.execute('update dhcp set active=?',(0,))
        file_list=['sw1_dhcp_snooping1.txt','sw2_dhcp_snooping1.txt','sw3_dhcp_snooping1.txt']
        for file in file_list:
            with open(file,'r') as f:
                data=[]
                readline=f.readlines()
                headers=readline[0]
                not_in_table=['Lease(sec)','Type']
                data_dict=dict.fromkeys([h for h in headers.split() if h!='Lease(sec)' and h!='Type'])
                not_in_table_index=[headers.split().index(h) for h in headers.split() if h=='Lease(sec)' or h=="Type"]
                # for r in readline[2:-1]:
                #     data.append(dict(zip(data_dict,r.split()[:2]+r.split()[4:])))
                # print(data)


                for r in readline[2:-1]:
                    temp_r=[str(rr) for rr in r.split() if r.split().index(rr) not in not_in_table_index]
                    temp_r.append(file.split('_')[0])
                    temp_r.append(1)
                    data.append(tuple(temp_r))
            query = 'INSERT into dhcp values (?,?,?,?,?,?)'
            for d in data:
                try:
                    con.execute(query, d)
                except:
                    con.execute('update dhcp set ip=?,vlan=?,interface=? where mac=?',(d[1],d[2],d[3],d[0]))
            con.commit()
def get_data(*args):
    if len(args)==0:
        con=sqlite3.connect('dhcp_snooping.db')
        data=con.execute("select * from dhcp where active=0").fetchall()
        print("Неактивные записи")
        print(tabulate(data))
        data = con.execute("select * from dhcp where active=1").fetchall()
        print("Активные записи")
        print(tabulate(data))
        con.close()
    elif len(args)==2:
        print(*args)
        con = sqlite3.connect('dhcp_snooping.db')
        data = con.cursor().execute(f"select * from dhcp where {args[0]}=?",(args[1],)).fetchall()
        print(tabulate(data))
        con.close()
    else:
        print("Функция принимает 0 или 2 аргумента")


def main():
    add_data('dhcp_snooping.db')
    get_data()
    get_data('vlan',1)
    get_data('switch', 'sw1')

    #create_db('dhcp_snooping.db')

if __name__ == "__main__":
    main()

#
