import re
from operator import getitem
infiles = [
    "sh_cdp_n_sw1.txt",
    "sh_cdp_n_r1.txt",
    "sh_cdp_n_r2.txt",
    "sh_cdp_n_r3.txt",
]
def parse_cdp_neighbors(command_output):
    adict={}
    res_dict={}
    device=command_output[:command_output.find('>')].strip('\n')
    reg=tuple(re.findall(r'\b[A-Z]{,}\d\s',command_output))
    alst=[st.strip() for st in command_output.split('\n') if st.startswith(reg) and len(st)>0]
    ind=command_output.split('\n').index(alst[0])
    names=[n.strip() for n in command_output.split('\n')[ind-1].split('  ') if len(n)>0]
    for pos,a in enumerate(alst,1):
        adict[pos]=dict(zip(names,[aa.strip() for aa in a.split('  ') if len(aa)>0]))
    for value in adict.values():
        k=(str(device),value['Local Intrfce'])
        res_dict[k]=(str(value['Device ID']),str(value['Port ID']))
    return res_dict



def main():
    topology_dict={}
    for file in infiles:
        print(file)
        with open(file) as f:
            temp=parse_cdp_neighbors(f.read())
            print(temp)
            for key,value in temp.items():
                print(key,value)
                if value not in topology_dict.keys():
                    topology_dict[key]=value
    print(topology_dict)



if __name__ == "__main__":
    main()

#
