
from collections import deque

def ConnectLetters(astr,t1,t2):

    variant=[]
    tup=[(c,v) for c, v in enumerate(astr)]
    for i  in range(len(tup)):
        for j in range(i,len(tup)):
            if tup[i][1]!=tup[j][1] and valid_1(tup[i][1],tup[j][1], t1,t2):#((tup[i][1] in t1 and tup[j][1] in t1) or (tup[i][1] in t2 and tup[j][1] in t2)):
                variant.append((tup[i],tup[j]))
    print(variant)
    input()
    
    vdict={}
    for vv in variant:
        key,value=vv,[v for v in variant if v[0]!=vv[0]]
        l=vdict.get(key,[])
        l.append(value)
        vdict[key]=l
    print(vdict)
    v=valid_2(variant)
    print(check(vdict, ((0, 'B'),(2, 'A')), t1,t2))
    return v

def valid(a,b):
    if valid_1(a,b):
        pass
    
def check(vdict, first, t1,t2):
    search_queue=deque()
    search_queue+=vdict[first]
    searched=[]
    while search_queue:
        v=search_queue.popleft()
        if not v in searched:
            pass
        else:
            search_+=vdict[v]
            searched.append(v)
    return False
    


    
def valid_1(a,b, t1, t2):
    if (a in t1 and b in t1) or(a in t2 and b in t2):
        return True
def valid_2(alst):
    
    for i in range(len(alst)):
        al=[]
        us=[]
        al.append(alst[i])
        us.append(alst[i][0])
        us.append(alst[i][1])
        for j in range(i+1, len(alst)):
            if alst[j][0] not in us and alst[j][1] not in us:
##                print(alst[i], alst[j])
##                input()
                #print(all([alst[i][0][0]<alst[j][0][0]<alst[j][1][0],alst[i][0][0]<alst[j][1][0]<alst[j][1][0]]))
                print(alst[i][0][0],alst[j][0][0],'*', alst[j][1][0],alst[i][1][0])
                if alst[i][0][0]<alst[j][0][0] and alst[j][1][0]<alst[i][1][0]:
                    al.append(alst[j])
                    us.append(alst[j][0])
                    us.append(alst[j][1])
                    
##                    print(al)
##                    input()
    return al
        

def main():
    
     print(ConnectLetters('BXABAYBA',('A','B'), ('X','Y')))
    

if __name__ == "__main__":
    main()


