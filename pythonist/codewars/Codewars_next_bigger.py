

def next_bigger(n):
    if len(str(n))<2 or len(set(list(str(n))))<2:
        return -1
    for i in range(len(str(n))-2,-1,-1):
        if int(str(n)[i])<int(str(n)[i+1]):         
            lst=list(str(n))
            tmplst=sorted(str(n)[i:])          
            lst.insert(i,min(list(j for j in tmplst if j>str(n)[i])))
            tmplst.remove(min(list(j for j in tmplst if j>str(n)[i])))
            return int(''.join(lst[:i+1]+tmplst))
    return -1
    

        


def main():

    
    print(next_bigger(2071))
##    print(next_bigger(9))
##    print(next_bigger(111))
##    print(next_bigger(144))
##    print(next_bigger(414))
##    print(next_bigger(9091420762))
##    print(next_bigger(598848484))
    
   
    
if __name__ == "__main__":
    main()




#
