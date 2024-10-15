import csv
import re
from pprint import pprint

import yaml
from tabulate import tabulate
def  parse_sh_cdp_neighbors(file):
    file_dict = {}
    headers=['Device ID','Local Intrfce', 'Holdtme', 'Capability', 'Platform', 'Port ID']
    with open(file,'r') as f:
        reader=csv.reader(f)
        h=next(reader)
        file_dict[h[0].split('>')[0]]={}
        for row in reader:
            if re.findall(r'\bR\d+', ' '.join(row)) or re.findall(r'\bSW\d+', ' '.join(row)):
                row_lst=[r.strip() for r in ' '.join(row).split('  ') if r!='']
                file_dict[h[0].split('>')[0]][row_lst[headers.index('Local Intrfce')]]={}
                file_dict[h[0].split('>')[0]][row_lst[headers.index('Local Intrfce')]][row_lst[headers.index('Device ID')]]=row_lst[headers.index('Port ID')]
        print(file_dict)
    return file_dict

def generate_topology_from_cdp(file_lst,save_to_file):
    res_dict={}
    for file in file_lst:
        res_dict.update(parse_sh_cdp_neighbors(file))
    with open(save_to_file,'w') as f:
        yaml.dump(res_dict,f)
def transform_topology(file):
    top_dict={}
    with open (file) as f:
        temp=yaml.safe_load(f)
    for key, value in temp.items():
        for k,v in value.items():
            for kk,vv in v.items():
                if (kk,vv) not in top_dict.keys():
                    top_dict[(key,k)]=(kk,vv)
    print(top_dict)
def main():
    file_lst=['sh_cdp_n_sw1.txt','sh_cdp_n_r1.txt','sh_cdp_n_r2.txt',
              'sh_cdp_n_r3.txt','sh_cdp_n_r4.txt','sh_cdp_n_r5.txt','sh_cdp_n_r6.txt']
    #parse_sh_cdp_neighbors('sh_cdp_n_r3.txt')
    generate_topology_from_cdp(file_lst,'topology.yaml')
    transform_topology('topology.yaml')

if __name__ == "__main__":
    main()

#
