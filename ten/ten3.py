import random
n=6
subs=[]

for i in range(n):
    subs.append(random.randint(0,10))
def profit_(subs):
    profit=0
    for i in range(len(subs)):
        profit=profit+subs[i]*(-1)**(i-1)
    return profit
print(subs)
print(profit_(subs))
def maxi_profit(subs):
    list_prof=[]
    for j in range(2): 
        for i in range(j,(len(subs)-j)//2*2,2):
            subs[i], subs[i+1]=subs[i+1], subs[i]
            list_prof.append(profit_(subs))
            subs[i], subs[i+1]=subs[i+1], subs[i]
        
    return list_prof
print(max(maxi_profit(subs)))
print(maxi_profit(subs))

