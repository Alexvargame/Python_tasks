
l_lift=[(2,6), (5,6), (2,5), (2,2), (6,8), (2,2), (0,2)]
#l_lift=[(2,4), (5,6), (2,2), (2,4), (6,8), (7,8), (0,2)]

n=len(l_lift)
lift_cl=[]
class lift():
    def __init__(self, first, last, pos=0):
        self.first=first
        self.last=last
        self.pos=pos
    def __repr__(self):
        return "<first: %s, last: %s, pos: %s>" %(self.first, self.last, self.pos)
    def __str__(self):
        return "%s %s %s" %(self.first, self.last, self.pos)
    def compire(self, lift):
        if self.first<lift.first:
            return True
        elif  self.first==lift.first:        
            if self.last<=lift.last:
                return True
            else: return False
        else: return False
      
for i in range(len(l_lift)):
    lift_cl.append(lift(l_lift[i][0], l_lift[i][1]))
for i in range(len(lift_cl)):
    for j in range(i,len(lift_cl)):
        if not lift_cl[i].compire(lift_cl[j]):
             lift_cl[i],lift_cl[j]=lift_cl[j], lift_cl[i]
i=0
count=0
def iter_(i, count):
    
    lift_cl.append(lift(lift_cl[-1].last, lift_cl[-1].last))
    for i in range(i, len(lift_cl)-1):
        if  lift_cl[i].first==lift_cl[-1].last:
            return count+1
        else:
            if lift_cl[i].last==lift_cl[i+1].first:
                count=count+1
            else :
                lift_cl.pop(i+1)
                iter_(i, count) 
    return count
print(iter_(i, count))
