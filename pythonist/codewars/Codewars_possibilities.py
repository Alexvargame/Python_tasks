
from itertools import product
def possibilities(param):
    combi=[item for item in product(['0','1'],repeat=param.count('?'))]
    print(combi)
    result=[]
    for item in combi:
        print(item)
        temp=param
        k=0
        for i in range(len(param)):
            if temp[i]=='?':
                print('i',i,'a',temp[:i],'b',item[k],'c',temp[i+1:])
                temp=temp[:i]+item[k]+temp[i+1:]
                k+=1
                print(temp)
        result.append(temp)
    return result
def main():

    print(possibilities('10??'))

if __name__ == "__main__":
    main()

#
