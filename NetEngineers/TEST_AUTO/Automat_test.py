import json
from tabulate import tabulate
def binary_contains(lst,key,value):
    low= 0
    high=len(lst) - 1
    while low <= high: # пока еще есть место для поиск
        mid=(low + high) // 2
        if int(lst[mid][key]) < int(value):
            low = mid + 1
        elif int(lst[mid][key]) > int(value):
            high = mid - 1
        else:
            return lst[mid]
    return False
def ss(item):
    return int(item['id'])

def automat_test(file1,file2):
    res_list={'params':[]}
    with open(file1) as f:
        temp_list=json.load(f)
    temp_list['params']=sorted(temp_list['params'],key=ss)
    with open(file2) as f:
        value_list=json.load(f)
    for item in value_list['values']:
        temp=binary_contains(temp_list['params'],'id',item['id'])
        if temp:
            temp['value']=item['value']
            if temp.get('values'):
                for it in temp['values']:
                    if it['id']==item['value']:
                        temp['value']=it['title']
                    if it.get('params'):
                        for item1 in value_list['values']:
                            temp1=binary_contains(sorted(it['params'],key=ss),'id',item1['id'])
                            if temp1:
                                for p in temp1['values']:
                                    if p['id']==item1['value']:
                                        temp['value']=p['title']
            res_list['params'].append(temp)
            temp_list['params'].remove(temp)
    with open('StructureWithValues.json','w') as f:
        f.write(json.dumps(res_list,indent=2))

def main():
    automat_test('TestcaseStructure.json','Values.json')



if __name__ == "__main__":
    main()

#
