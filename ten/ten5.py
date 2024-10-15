mans=5
ch=3
list_=['ad','a','abc','aboba','b', 'add']
ch_l=[(3,'a'),(2,'ab'),(1,'b'),(2,'ad'),(1,'r')]
s_list_=sorted(list_).copy()
print(s_list_)
for j in range(len(ch_l)):
    k=0
    t=''
    for i in range(len(list_)):
        if k!=ch_l[j][0]:
            if s_list_[i].find(ch_l[j][1])==0:
                k=k+1
                t=s_list_[i]
    if t:
        print(list_.index(t)+1)
    else:
        print("-1")
                          
