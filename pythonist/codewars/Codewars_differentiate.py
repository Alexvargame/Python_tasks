import re
def differentiate(equation, point):
    print(re.findall(r'[-+]',equation))
    signs=[-1 if i=='-' else 1 for i in re.findall(r'[-+]',equation)]
    members = re.split(r'[-+]', equation)
    if equation[0]!='-':
        signs.insert(0,1)
    else:
        members=members[1:]

    print('members',members)
    new_members=[]
    for m in members:
        mm=re.split(r'[x^]',m)
        # print('mm',mm)
        if len(mm)>2:
            if mm[0] != '':
                new_members.append((int(mm[0])*int(mm[-1]),int(mm[-1])-1))
            else:
                new_members.append((int(mm[-1]), int(mm[-1])-1))
        if len(mm)==2:
            if mm[0]!='':
                new_members.append((int(mm[0]),0))
            else:
                new_members.append((1, 0))
    print('signs',signs)
    print('new',new_members)
    if new_members[0][1]==0:
        return signs[0] * new_members[0][0]
    if new_members[0][1]>1:
        res=str(signs[0] * new_members[0][0]) + 'x^' + str(new_members[0][1])
    else:
        res = str(signs[0] * new_members[0][0]) + 'x'
    res1=signs[0] * new_members[0][0]*(point**new_members[0][1])
    print('res1',res1)
    for i in range(1,min(len(signs),len(new_members))):
        print('i1',new_members[i][1],new_members[i][0],'si',signs[i])
        if new_members[i][1]>1:
            if signs[i]*new_members[i][0]>0:
                res +='+'+str(signs[i] * new_members[i][0]) + 'x^' + str(new_members[i][1])
            else:
                res +=str(signs[i] * new_members[i][0]) + 'x^' + str(new_members[i][1])
            print('r',signs[i] * new_members[i][0]*(point**new_members[i][1]))
            res1+=signs[i] * new_members[i][0]*(point**new_members[i][1])
            print('1res111', res1)
        elif new_members[i][1]==1:
            if signs[i] * new_members[i][0] > 0:
                res +='+'+str(signs[i] * new_members[i][0]) + 'x'
            else:
                res+=str(signs[i]*new_members[i][0])+'x'
            res1 += signs[i] * new_members[i][0] * (point ** new_members[i][1])
            print('2res111', res1)
        else:
            if new_members[i][0]>0:
                res +='+'+str(new_members[i][0])
            else:
                res+=str(new_members[i][0])
            res1 += signs[i] * new_members[i][0] * (point ** new_members[i][1])
            print('3res111',res1)
    print('res',res)

    return res1



        
def main():
     print(differentiate('-7x^5+22x^4-55x^3-94x^2+87x-56', -3))
if __name__ == "__main__":
    main()




#
