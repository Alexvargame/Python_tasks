
import json


def read_json(file):
    with open (file) as f:
        templates=json.load(f)
    oper_systems=[t['smart_os'] for t in templates]
    print(oper_systems)
    res_dict={}
    for os in oper_systems:
        key,value=os,oper_systems.count(os)
        res_dict[key]=value
    print(res_dict)
    res_dict=dict(sorted(res_dict.items(),key=lambda x: x[1])[::-1])
    return res_dict
def main():
    print(read_json('smarts.json'))

if __name__ == "__main__":
    main()