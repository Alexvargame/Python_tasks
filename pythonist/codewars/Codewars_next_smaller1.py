

def next_smaller(n):
    print(n)
    if len(str(n))<2 or len(set(list(str(n))))<2:
        return -1
    for i in range(len(str(n))-2,-1,-1):
        print(int(str(n)[i]),int(str(n)[i+1]))
        if int(str(n)[i])>int(str(n)[i+1]):
            #if str(n)[i+1]!='0'zzzzzz
            
            lst=list(str(n))
            tmplst=sorted(str(n)[i:],reverse=True)          
            lst.insert(i,max(list(j for j in tmplst if j<str(n)[i])))
            tmplst.remove(max(list(j for j in tmplst if j<str(n)[i])))
            print(''.join(lst[:i+1]+tmplst))
            if ''.join(lst[:i+1]+tmplst)[0]=='0':
                return -1
            return int(''.join(lst[:i+1]+tmplst))
    return -1
    

        


def main():

    
    print(next_smaller(907))
##    print(next_bigger(9))
##    print(next_bigger(111))
##    print(next_bigger(144))
##    print(next_bigger(414))
##    print(next_bigger(9091420762))
##    print(next_bigger(598848484))
    
   
    
if __name__ == "__main__":
    main()




#
