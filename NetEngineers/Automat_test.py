import json
from tabulate import tabulate
def binary_contains(lst,key,value):
    print('B',key,value)
    low= 0
    high=len(lst) - 1
    while low <= high: # пока еще есть место для поиск
        mid=(low + high) // 2
        print('M',mid,lst[mid])
        if lst[mid][key] < value:
            low = mid + 1
        elif lst[mid][key] > value:
            high = mid - 1
        else:
            return lst[mid]
    return False
def automat_test(file1,file2):
    res_list=[]
    with open(file1) as f:
        temp_list=json.load(f)
    temp_list=sorted(temp_list,key=id)
    with open(file2) as f:
        value_list=json.load(f)
    for item in value_list:
        temp=binary_contains(temp_list,'id',item['id'])
        if temp:
            if type(item['value']) is str:
                temp['value']=item['value']
            else:
                temp['values']=item['value']
            res_list.append(temp)
            temp_list.remove(temp)
    print('res',res_list)
    with open('StructureWithValues.json','w') as f:
        #for r in res_list:
        f.write(json.dumps(res_list,indent=2))

def main():
    automat_test('TestcaseStructure.json','Values.json')



if __name__ == "__main__":
    main()

#
