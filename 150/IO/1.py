with open ("1.txt", 'r') as f:
    #print(f.read())
    for s in f.readlines():
        print(s)
txt="55"
with open ("1.txt", 'a') as f:
    f.write(txt)
l=[]
with open ("1.txt", 'r') as f:
    for s in f.readlines():
       l.append(s)
print(l,len(l))
with open ("1.txt", 'r') as f:
    
    l1=f.read().split(" ")
print(max(l1))

with open ("1.txt", 'r') as f:
    
    a=f.read()
    with open ("2.txt", 'a') as f1:
        f1.write(a)
        
    


