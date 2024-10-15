import re


def convert_congic_to_dict(config_file_name):
    result_dict={}
    res=[]

    with open(config_file_name) as cf:
        cf_alst=[r.rstrip('\n').strip() for r in cf.read().split('!')[3:] if r.strip('\n').strip()!='' and not r.strip('\n').strip().startswith('alias')]
        print(cf_alst)
        for c in cf_alst:
            if not c.startswith('interface') and not c.startswith('line'):
                for cc in c.split('\n'):
                    result_dict[cc]=[]
            elif c.startswith('interface'):
                result_dict[c.split('\n')[0]]=c.split('\n')[1:]
            elif c.startswith('line'):
                print(c.split('line'))
                l=[('line'+i).strip().split('\n') for i in c.strip().split('line')[1:]]
                print(l)
                for ll in l:
                    result_dict[ll[0]]=[j.strip() for j in ll[1:]]


    for key,value in result_dict.items():
        print(key,':', value)




def main():
   convert_congic_to_dict('config_sw9_1.txt')



if __name__ == "__main__":
    main()

#
