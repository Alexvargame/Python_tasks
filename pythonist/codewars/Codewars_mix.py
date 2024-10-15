
def mix(s1,s2):
    res=[]
    s1_dict={}
    s2_dict={}
    print('s1',s1)
    print('s2',s2)
    for l in s1:
        if l.isalpha() and l.islower()and s1.count(l)>1:
            key,value=l, s1.count(l)
            s1_dict[key]=value
    print('s1',s1_dict)
    s1_dict_sort=dict(sorted(s1_dict.items(), key=lambda x:x[1],reverse=True))
    
    
    for l in s2:
        if l.isalpha() and l.islower()and s2.count(l)>1:
            key,value=l, s2.count(l)
            s2_dict[key]=value
    print('s2',s2_dict)
    s2_dict_sort=dict(sorted(s2_dict.items(), key=lambda x:x[1],reverse=True))
    s_dict_sort={}
   
    #s_dict_sort=dict(sorted(s_dict.items(), key=lambda x:x[1],reverse=True))
    for k in s2_dict.keys():
        if k in s1_dict.keys():
            if s2_dict[k]>s1_dict[k]:
                s_dict_sort[k]=s2_dict[k]
            else:
                s_dict_sort[k]=s1_dict[k]
        else:
            s_dict_sort[k]=s2_dict_sort[k]
    for k in s1_dict.keys():
        if k not in s2_dict.keys():
            s_dict_sort[k]=s1_dict_sort[k]
    print(s_dict_sort)
    for k,v in s_dict_sort.items():
        if k in s1_dict.keys() and k in s2_dict.keys():
            if s1_dict[k]>s2_dict[k]:
                res.append('1:'+k*s_dict_sort[k])
            elif s1_dict[k]<s2_dict[k]:
                res.append('2:'+k*s_dict_sort[k])
            else:
                res.append('=:'+k*s1_dict[k])
        elif k in s1_dict.keys() and k not in s2_dict.keys():
            res.append('1:'+k*s_dict_sort[k])
        else :
            res.append('2:'+k*s_dict_sort[k])

    res1=sorted(res, key=lambda r:(-len(r.split(':')[1]), r.split(':')[0], r.split(':')[1][0]))
    print(res,res1)


            
    return  ('/').join(sorted(res, key=lambda r:(-len(r.split(':')[1]), r.split(':')[0],r.split(':')[1][0])))


##    if k in s1_dict.keys() and k in s2_dict.keys():
##            if s1_dict[k]>s2_dict[k]:
##                res=res+'1:'+k*s_dict_sort[k]+'/'
##            elif s1_dict[k]<s2_dict[k]:
##                res=res+'2:'+k*s_dict_sort[k]+'/'
##            else:
##                res=res+'=:'+k*s1_dict[k]+'/'
##        elif k in s1_dict.keys() and k not in s2_dict.keys():
##            res=res+'1:'+k*s_dict_sort[k]+'/'
##        else :
##            res=res+'2:'+k*s_dict_sort[k]+'/'
##        
##

def main():

    #print(mix("my&friend&Paul has heavy hats! &","my friend John has many many friends &"))
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"))
        
    
if __name__ == "__main__":
    main()




#
