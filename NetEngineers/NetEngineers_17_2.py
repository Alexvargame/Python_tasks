import csv
import re

from tabulate import tabulate
def  parse_sh_version(file):
    data = []
    headers = ["hostname", "ios", "image", "uptime"]
    data.append(headers)

    with open(file,'r') as f:
        for line in f.readlines():
            if re.findall(r'IOS[\w\s]+',line):
                print(line)
                for l in line.split(','):
                    if 'Version' in l:
                        ios=l.split()[1]
                        print(ios)
            elif re.findall(r'\d{,3}\sdays\,\s\d{,2}\shours\,\s\d{,2}\sminutes',line):
                uptime=', '.join(re.findall(r'\d{,3}\sdays',line)+re.findall(r'\d{,2}\shours',line)+re.findall(r'\d{,2}\sminutes',line))
                print(uptime)
            elif re.findall(r'image[\w\s]+',line):
                image=line.split()[-1].strip('"')
                print(image)
    data.append([file.split('.')[0].split('_')[-1],ios,image,uptime])
    return data

def write_inventory_to_csv(data_filenames,csv_filename):

    for file in data_filenames:
        with open(csv_filename, 'a') as f:
            writer = csv.writer(f)
            for row in parse_sh_version(file):
                writer.writerow(row)



def main():
    file_lst=['sh_version_r1.txt','sh_version_r3.txt','sh_version_r3.txt']
    write_inventory_to_csv(file_lst,'routers_inventory.csv')

if __name__ == "__main__":
    main()

#
