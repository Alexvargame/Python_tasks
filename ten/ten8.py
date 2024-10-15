n=3
m=3
domens=["ASSRTS", "RRARTT", "AARS"]
buyers=[("A","S"), ("AA", "S"),("R","T")]
count=0
l_count=dict.fromkeys(buyers)

for i in range(len(buyers)):
    count=0
    for j in range(len(domens)):

        if domens[j].find(buyers[i][0])==0 and domens[j].find(buyers[i][1], -1)==(len(domens[j])-len(buyers[i][1])):
            count=count+1
    l_count[buyers[i]]=count
print(l_count) 
                 
