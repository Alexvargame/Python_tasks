
class Warrior:

    

    def __init__(self, level=1, experience=100):
        self.ranks=["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
           "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        
        self.experience=experience
        self.level=level
        self.rank=self.ranks[self.level//10]
        self.achievements=[]

    def __str__(self):

        return f'{self.rank}-{self.level}-{self.experience}'
        
    def get_experience(self,a):
        if self.experience+a>10000:
            return 10000
        return self.experience+a
    def fight(self,w):
        if w<1 or w>100:
            return f"Invalid level"
        elif self.level<w-4 and self.ranks.index(self.rank)<w//10:
            return f"You've been defeated"
        elif self.level-1>w:
            return f"Easy fight"
        elif self.level-1==w:
            self.experience=self.get_experience(5)
            self.level=self.experience//100
            self.rank=self.ranks[self.level//10]
            return f"A good fight"
        elif self.level==w:
            self.experience=self.get_experience(10)
            self.level=self.experience//100
            self.rank=self.ranks[self.level//10]
            return f"A good fight"
        elif self.level<w:
            self.experience=self.get_experience(20*(w-self.level)**2)#self.experience+20*(w-self.level)**2
            self.level=self.experience//100
            self.rank=self.ranks[self.level//10]
            return f"An intense fight"
        
    def training(self,achi_lst):
        if self.level>=achi_lst[2]:
            self.experience=self.get_experience(achi_lst[1])#self.experience+achi_lst[1]
            self.level=self.experience//100
            self.rank=self.ranks[self.level//10]
            self.achievements.append(achi_lst[0])
            return f'{achi_lst[0]}'
        else:
            return f"Not strong enough"
        

def main():
    ranks=["Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage",
           "Elite", "Conqueror", "Champion", "Master", "Greatest"]
        

    bruce=Warrior()
    print(bruce)
    chuck=Warrior()
    print('bruce-chuck',bruce.fight(1))
    swarz=Warrior(level=4)
    print('bruce-swarz',bruce.fight(4))
    print('bruce-swarz',bruce.fight(4))
    print('bruce-swarz',bruce.fight(4))
    print('bruce-swarz',bruce.fight(4))
    swarz.level=8
    print(bruce)
    print('bruce-swarz',bruce.fight(8))
    print('bruce-swarz',chuck.fight(11))
    print('chuck-swarz',chuck.fight(11))
    print(bruce.training(['first',1000,1]))
    print(bruce)
    print(bruce.training(['second',1000,30]))
    print(bruce)
    print('bruce-swarz',bruce.fight(15))
    
        
    
    
    
    
  
    
if __name__ == "__main__":
    main()



##def fight(self,w):
##        if w.level<1 or w.level>100:
##            return f"Invalid level"
##        elif self.level<w.level-4:
##            return f"You've been defeated"
##        elif self.level-2>w.level:
##            return f"Easy fight"
##        elif self.level-1==w.level:
##            self.experience=self.experience+5
##            self.level=self.experience//100
##            self.rank=self.ranks[self.level//10]
##            return f"A good fight"
##        elif self.level==w.level:
##            self.experience=self.experience+10
##            self.level=self.experience//100
##            self.rank=self.ranks[self.level//10]
##            return f"A good fight"
##        elif self.level<w.level:
##            self.experience=self.experience+20*(w.level-self.level)**2
##            self.level=self.experience//100
##            self.rank=self.ranks[self.level//10]
##            return f"An intense fight"
##        
##    def training(self,achi_lst):
##        if self.level>=achi_lst[2]:
##            self.experience=self.experience+achi_lst[1]
##            self.level=self.experience//100
##            self.rank=self.ranks[self.level//10]
##            self.achievements.append(achi_lst[0])
##            return f'{achi_lst[0]}'
##        else:
##            return f"Not strong enough"
class Warrior(object):
    
    MAX_LVL        = 100
    MAX_XPS        = 10000
    LVL_XP_RATIO   = 100
    RANKS          = ["", "Pushover", "Novice", "Fighter", "Warrior", "Veteran", "Sage", "Elite", "Conqueror", "Champion", "Master", "Greatest"]
    DEF_RET_ACHIEV = "Not strong enough"
    INVALID_BATTLE = "Invalid level"
    FAILED_BATTLE  = "You've been defeated"
    STR_BATTLE     = ["A good fight", "An intense fight", "Easy fight"]
    
    
    def __init__(self):      self.xps, self.achiev = self.LVL_XP_RATIO, []
    
    @property
    def level(self):         return self.xps // self.LVL_XP_RATIO
    @property
    def rank(self):          return self.RANKS[self.getRank(self.xps)]
    @property
    def experience(self):    return self.xps
    @property
    def achievements(self):  return self.achiev[:]
    
    def getRank(self,xps):   return xps//1000 + 1
    def updateXps(self,xp):  self.xps = min( self.xps+xp, self.MAX_XPS )
    
    def battle(self, oLvl):
        diff = oLvl - self.level
        if not (1 <= oLvl <= self.MAX_LVL):
            return self.INVALID_BATTLE
            
        if diff >= 5 and self.getRank(self.xps) < self.getRank(oLvl*self.LVL_XP_RATIO):
            return self.FAILED_BATTLE
        
        xpGain = 20 * diff**2 if diff > 0 else max(0, 10+5*diff)
        iRet   = (diff>0)-(diff<0) if diff != -1 else 0
        self.updateXps(xpGain)
        return self.STR_BATTLE[iRet]
    
    def training(self, event):
        ach, xpGain, minLvl = event
        if self.level < minLvl: return self.DEF_RET_ACHIEV
        
        self.updateXps(xpGain)
        self.achiev.append(ach)
        return ach
class Warrior():
    _ranks = "Pushover","Novice","Fighter","Warrior","Veteran","Sage","Elite","Conqueror","Champion","Master","Greatest"
    
    def __init__(self):
        self.experience = 0
        self.achievements = []
        self._set_props(100)
    
    def _set_props(self, new_exp):
        self.experience = min(10_000, self.experience + new_exp)
        self.level = self.experience // 100
        self.rank = self._ranks[self.level // 10]
    
    def training(self, arg):
        descr, exp, min_level = arg
        if self.level < min_level: return "Not strong enough"
        self._set_props(exp)
        self.achievements.append(descr)
        return descr
    
    def battle(self, lvl):
        diff = lvl - self.level
        if not 0 < lvl < 101:                                       return 'Invalid level'
        elif self._ranks.index(self.rank) < lvl // 10 and diff > 4: return "You've been defeated"
        elif diff >  0: exp, desc = 20 * diff * diff, 'An intense'
        elif diff < -1: exp, desc = 0               , 'Easy'
        else          : exp, desc = 5 * (2 + diff)  , 'A good'
        self._set_props(exp)
        return f'{desc} fight'
