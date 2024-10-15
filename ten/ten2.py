
class Team():
    def __init__(self, player1, player2, player3):
        self.player1=player1
        self.player2=player2
        self.player3=player3
        self.wins=1
    def __repr__(self):
        return "{player1:%s, player2:%s, player3:%s, wins:%s}" %(self.player1, self.player2, self.player3, self.wins)
    def __str__(self):
        return "%s %s %s %s" %(self.player1, self.player2, self.player3, self.wins)
    def compire(self,t1):
        l1=[t1.player1,t1.player2,t1.player3]
        l2=[self.player1,self.player2,self.player3]
        if len(list(set(l1)&set(l2)))==len(l1):
               t1.wins=t1.wins+1
               self.wins=self.wins+1
        

def max_w():
    l2=[]
    N=0
    list_=[]
    Team_l=[]
    with open('1.txt', 'r') as f:
        t=f.readlines()
        for l in t:
            list_.append(l.replace('\n','').split(","))
    N=len(t)
    for i in range(N):
        Team_l.append(Team(list_[i][0], list_[i][1], list_[i][2]))

    for i in range(N):
        for j in range(i+1, N):
            Team_l[i].compire(Team_l[j])
    for i in range(N):
        l2.append(Team_l[i].wins)
    return max(l2)
 
print(max_w())
