
class PokerHand(object):

    RESULT=['Loss','Tie','Win']
    NOMINAL_F=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    NOMINAL_S=['S','H','D','C']
    

    def __init__(self, hand):
        self.hand=hand

    def compare_with(self, other):
        COMBINATIONS=["Straight_Flash","For_of_a_Kind","Full_House","Flush","Straight","Three_of_a_Kind","Two_Pairs","Pair","High_Card"]
        if COMBINATIONS.index(self.is_combination()[0])<COMBINATIONS.index(other.is_combination()[0]):
            return 'Win'
        elif COMBINATIONS.index(self.is_combination()[0])>COMBINATIONS.index(other.is_combination()[0]):
            return 'Loss'
        else:
            if self.is_combination()[1]<other.is_combination()[1]:
                return 'Loss'
            elif self.is_combination()[1]>other.is_combination()[1]:
                return 'Win'
            else:                  
                for i in range(len(self.is_combination()[2])-1,-1,-1):
                    print(self.is_combination()[2][i],other.is_combination()[2][i])
                    if self.is_combination()[2][i]<other.is_combination()[2][i]:
                        return 'Loss'
                    if self.is_combination()[2][i]>other.is_combination()[2][i]:
                        return 'Win'
                return 'Tie'
        
                    
        
        

    def __str__(self):
        return self.hand
    

    def is_combination(self,lst=NOMINAL_F):
        alst=[a[0] for a in self.hand.split()]
        if len(set([a[1] for a in self.hand.split()]))==1 and max([lst.index(a[0]) for a in
                                self.hand.split()])-min([lst.index(a[0]) for a in self.hand.split()])==4:
            return "Straight_Flash", max([lst.index(a[0]) for a in self.hand.split()]), []
        elif len(set([a[1] for a in self.hand.split()]))==1:
            return "Flush", max([lst.index(a[0]) for a in self.hand.split()]),sorted([lst.index(a) for a in alst if a!=max(alst)])
        
        elif  len(set([a[0] for a in self.hand.split()]))==5 and max([lst.index(a[0]) for a in
                        self.hand.split()])-min([lst.index(a[0]) for a in self.hand.split()])==4:
            return "Straight",max([lst.index(a[0]) for a in self.hand.split()]),[]
        else:
            if len(set([a[0] for a in self.hand.split()]))==5:
                return "High_Card", lst.index(max(alst)),sorted([lst.index(a) for a in alst if a!=max(alst)])
            else:
                a_dict={}
                for a in self.hand.split():
                        key,value=a[0],[a[0] for a in self.hand.split()].count(a[0])
                        a_dict[key]=value
                if len(set([a[0] for a in self.hand.split()]))==2 and max(a_dict.values())==4:
                    return "For_of_a_Kind", lst.index([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())][0]
                                                      ),sorted([lst.index(k) for k in a_dict.keys() if a_dict[k]!=max(a_dict.values())])
                elif len(set([a[0] for a in self.hand.split()]))==2 and max(a_dict.values())==3:
                    return "Full_House", lst.index([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())][0]
                                                   ),sorted([lst.index(k) for k in a_dict.keys() if a_dict[k]!=max(a_dict.values())])
                elif len(set([a[0] for a in self.hand.split()]))==3 and max(a_dict.values())==3:
                    return "Three_of_a_Kind", lst.index([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())][0]
                                                        ),sorted([lst.index(k) for k in a_dict.keys() if a_dict[k]!=max(a_dict.values())])
                elif len(set([a[0] for a in self.hand.split()]))==3 and max(a_dict.values())==2:
                    return "Two_Pairs", lst.index([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())][0]
                                                  ),sorted([lst.index(k) for k in a_dict.keys() if a_dict[k]!=max(a_dict.values())])
                else:
                    return "Pair", lst.index(max([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())]
                                                 )),sorted([lst.index(k) for k in a_dict.keys() if a_dict[k]!=max(a_dict.values())])
                
                
                    
                
    


def main():

    P=PokerHand("2H 3H 4H 5H 6H")
    P1=PokerHand("KS AS TS QS JS")
   
    print("P",P.is_combination())
    print("P1",P1.is_combination())
    

    print(P.compare_with(P1))
   


if __name__ == "__main__":
    main()

##
##def is_straight_flash(self,lst=NOMINAL_F):
##        if len(set([a[1] for a in self.hand.split()]))==1 and max([lst.index(a[0]) for a in
##                                self.hand.split()])-min([lst.index(a[0]) for a in self.hand.split()])==4:
##            return True,max([lst.index(a[0]) for a in self.hand.split()])
##        return False, None 
##        
##        
##    
##    def is_for_of_a_kind(self,lst=NOMINAL_F):
##        alst=[a[0] for a in self.hand.split()]
##        
##        a_dict={}
##        if len(set([a[0] for a in self.hand.split()]))==2: 
##            for a in self.hand.split():
##                key,value=a[0],[a[0] for a in self.hand.split()].count(a[0])
##                a_dict[key]=value
##            if max(a_dict.values())==4:
##                return True, lst.index([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())][0])
##            
##        return False, None
##    def is_full_house(self,lst=NOMINAL_F):
##        alst=[a[0] for a in self.hand.split()]
##        print(alst)
##        a_dict={}
##        if len(set([a[0] for a in self.hand.split()]))==2:
##            
##            print(max([[a[0] for a in self.hand.split()].count(a[0]) for a in self.hand.split()]))
##            
##            for a in self.hand.split():
##                key,value=a[0],[a[0] for a in self.hand.split()].count(a[0])
##                a_dict[key]=value
##            if max(a_dict.values())==3:
##                return True, lst.index([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())][0])
##        return False, None
##
##    def is_straight(self,lst=NOMINAL_F):
##        if max([lst.index(a[0]) for a in self.hand.split()])-min([lst.index(a[0]) for a in self.hand.split()])==4:
##            return True,max([lst.index(a[0]) for a in self.hand.split()])
##        return False, None 
##
##    def is_tree_of_a_kind(self,lst=NOMINAL_F):
##        alst=[a[0] for a in self.hand.split()]
##        
##        a_dict={}
##        if len(set([a[0] for a in self.hand.split()]))==3: 
##            for a in self.hand.split():
##                key,value=a[0],[a[0] for a in self.hand.split()].count(a[0])
##                a_dict[key]=value
##            if max(a_dict.values())==3:
##                return True, lst.index([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())][0])
##        return False, None
##
##    def is_two_pairs(self,lst=NOMINAL_F):
##        alst=[a[0] for a in self.hand.split()]
##        
##        a_dict={}
##        if len(set([a[0] for a in self.hand.split()]))==3: 
##            for a in self.hand.split():
##                key,value=a[0],[a[0] for a in self.hand.split()].count(a[0])
##                a_dict[key]=value
##            if max(a_dict.values())==2:
##                return True, lst.index(max([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())]))
##        return False, None 
##    def is_pair(self,lst=NOMINAL_F):
##        alst=[a[0] for a in self.hand.split()]
##        
##        a_dict={}
##        if len(set([a[0] for a in self.hand.split()]))==4: 
##            for a in self.hand.split():
##                key,value=a[0],[a[0] for a in self.hand.split()].count(a[0])
##                a_dict[key]=value
##            if max(a_dict.values())==2:
##                return True, lst.index(max([k for k in a_dict.keys() if a_dict[k]==max(a_dict.values())]))
##        return False, None 
##    def is_high_card(self,lst=NOMINAL_F):
##        alst=[a[0] for a in self.hand.split()]
##        
##        a_dict={}
##        if len(set([a[0] for a in self.hand.split()]))==5: 
##            for a in self.hand.split():
##                key,value=a[0],[a[0] for a in self.hand.split()].count(a[0])
##                a_dict[key]=value
##            return True, lst.index(max([k for k in a_dict.keys()]))
##        return False, None 


