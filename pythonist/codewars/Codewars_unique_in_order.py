import re
def unique_in_order(sequence):
    result=[]
    if type(sequence)==str:
        for i in range(len(sequence)):
            exp=r''+sequence[i]+r'+'
            for item in re.finditer(exp,sequence):
                print(item,'i',item[0],'len',len(result))
                if len(result)>0:
                    if item[0][0]!=result[-1]:
                        print('last',result[-1])
                        result.append(item[0][0])
                else:
                    result.append(item[0][0])
    else:
        result=[sequence[0]]
        print(result[-1])
        r=[sequence[0]]
        for i in range(len(sequence)):
            if sequence[i]!=sequence[i-1]:
                r.append(sequence[i])
        print(r)
        result=[sequence[i] for i in range(1,len(sequence)) if sequence[i]!=sequence[i-1]]
        result.insert(0,sequence[0])
        
          
                   
    return result

def main():

   print(unique_in_order(['a', 'b', 'b', 'a']))

if __name__ == "__main__":
    main()




#
