


def strr(str2, str1):
    l=list(str1)
    l1=list(str2)
    for i in l1:
        if i not in l:
            return False
        else:
            l.remove(i)
    return True

print(strr('naaffd','aanf'))
print(strr('naaffd','aanfk'))
print(strr('','aa'))
print(strr('aa',''))





        
