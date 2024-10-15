#dep1=[(6,6),(8,8)]

l=[]
l_v=[]
l_p=[]
with open("2.txt",'r') as f:
    ll=f.readlines()
    for i in ll:
        l=[]
        l.append(i.replace('\n','').split("="))
        print(l)
        
        l_v.append(l[0][0])
        if  len(l)==1:
            l_p.append(l[0][0])
        else:
            l_p.append(l[0][1])
print(l_v,l_p)
