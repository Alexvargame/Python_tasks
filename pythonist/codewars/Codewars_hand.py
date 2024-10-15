from itertools import combinations

def compare_list(a,b):
    print(a,b)
    NOMINAL_F=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for i in range(len(a)):
        if NOMINAL_F.index(a[i])<NOMINAL_F.index(b[i]):
            return False
    return True

class Hand(object):

    NOMINAL_F=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    NOMINAL_S=["♣","♥","♦","♠"]
    COMBINATIONS=["straight-flash","for-of-a-kind","full house","flush","straight","three-of-a-kind","two pair","pair","nothing"]

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
    
    def sort_hand_nom(self,card):
        return -self.NOMINAL_F.index(card)
    def sort_hand(self,card):
        return -self.NOMINAL_F.index(card[:-1])
##    def sort_dict(self,card):
##        return dictt[a[:-1]]
    def is_combination(self,lst=NOMINAL_F):
        alst=sorted([a[:-1] for a in self.hand],key=self.sort_hand_nom)
##        print('a',alst,alst[0])
##        print(sorted(self.hand,key=self.sort_hand))
##        print(lst.index(alst[0]),lst.index(alst[-1]))
        if len(set([a[-1] for a in self.hand]))==1 and lst.index(alst[0])-lst.index(alst[-1])==4:
            res_comb=sorted(self.hand,key=self.sort_hand)
            return "straight-flush", res_comb#,[c[:-1] for c in res_comb]
        elif len(set([a[-1] for a in self.hand]))==1:
            res_comb=sorted(self.hand,key=self.sort_hand)
            return "flush", res_comb#,[c[:-1] for c in res_comb]
        
        elif  len(set([a[:-1] for a in self.hand]))==5 and lst.index(alst[0])-lst.index(alst[-1])==4:
            res_comb=sorted(self.hand,key=self.sort_hand) 
            return "straight",res_comb#,[c[:-1] for c in res_comb]
        else:
            if len(set([a[:-1] for a in self.hand]))==5:
                res_comb=[c for c in self.hand if c[:-1]==alst[0]]
                return "nothing", res_comb
            else:
                hand=self.hand.copy()
                a_dict={}
                
                for a in self.hand:
                        key,value=a[:-1],alst.count(a[:-1])
                        a_dict[key]=value
                nom=sorted([key for key in a_dict.keys() if a_dict[key]==max(a_dict.values())],key=self.sort_hand_nom)
                if len(set(alst))==2 and max(a_dict.values())==4:
                    #nom=[key for key in a_dict.keys() if a_dict[key]==max(a_dict.values())]
                    res_comb=[a for a in self.hand if a[:-1]==nom[0]]                   
                    return "four-of-a-kind",res_comb#,[res_comb[0][:-1]]+[c[:-1] for c in hand if c not in res_comb]
                elif len(set(alst))==2 and max(a_dict.values())==3:
                    res_comb=[c for c in self.hand if a_dict[c[:-1]]==3]+[c for c in self.hand if a_dict[c[:-1]]==2]#sorted(self.hand,key=self.sort_hand)
                    
                    return "full house", res_comb#,[key for key in a_dict.keys() if a_dict[key]==3][:1]+[key for key in a_dict.keys() if a_dict[key]==2][:1]
                elif len(set(alst))==3 and max(a_dict.values())==3:
                    #nom=[key for key in a_dict.keys() if a_dict[key]==max(a_dict.values())]
                    res_comb=sorted([a for a in self.hand if a[:-1]==nom[0]],key=self.sort_hand)        
                    return "three-of-a-kind", res_comb#,nom+sorted([c[:-1] for c in hand if c not in res_comb],key=self.sort_hand_nom)
                elif len(set([a[:-1] for a in self.hand]))==3 and max(a_dict.values())==2:
                    #nom=sorted([key for key in a_dict.keys() if a_dict[key]==max(a_dict.values())],key=self.sort_hand_nom)
                    res_comb=sorted([a for a in self.hand if a[:-1] in nom],key=self.sort_hand)
                    return "two pair", res_comb#,nom+[c[:-1] for c in hand if c not in res_comb]
                else:
                    #nom=[key for key in a_dict.keys() if a_dict[key]==max(a_dict.values())]
                    res_comb=sorted([a for a in self.hand if a[:-1] == nom[0]],key=self.sort_hand)
                    return "pair",res_comb#,nom+sorted([c[:-1] for c in hand if c not in res_comb],key=self.sort_hand_nom)
                

def hand(hole_cards, community_cards):
     
     CARDS=hole_cards+community_cards
     print(CARDS)
     COMBINATIONS=["straight-flush","four-of-a-kind","full house","flush","straight","three-of-a-kind","two pair","pair","nothing"]
     NOMINAL_F=['2','3','4','5','6','7','8','9','10','J','Q','K','A']
     #print('RRRR',[Hand(list(item)).is_combination()[0] for item in combinations(hole_cards+community_cards,5)])
     res=['nothing',['2♣','2♣','2♣','2♣','2♣'],[]]
##     print([item for item in combinations(CARDS,5)])
##     input()
     for item in combinations(CARDS,5):
         comb=Hand(list(item)).is_combination()
         print('i',item,comb,res)
         if set(list(item))==set(['5♣', '7♣', '3♣', 'K♣', '6♣']):
             input()
         #print(sorted([c[:-1] for c in CARDS if c not in comb[1]],key=Hand(list(item)).sort_hand_nom))
         if COMBINATIONS.index(comb[0])<COMBINATIONS.index(res[0]):# and sort_list([c[:-1] for c in comb[1]],[c[:-1] for c in res[1]]):
             print('c',COMBINATIONS.index(comb[0]),COMBINATIONS.index(res[0]))
             print('l',[c[:-1] for c in comb[1]],[c[:-1] for c in res[1]])
             print('DDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
             res[0]=comb[0]
             res[1]=comb[1]
             res[2]=[]
             for c in comb[1]:
                 if c[:-1] not in res[2]:
                     res[2].append(c[:-1])
                     
             res[2]+=sorted([c[:-1] for c in CARDS if c not in comb[1]],key=Hand(list(item)).sort_hand_nom)[:5-len(res[1])]
         elif COMBINATIONS.index(comb[0])==COMBINATIONS.index(res[0]) and compare_list([c[:-1] for c in comb[1]],[c[:-1] for c in res[1]]):
             print('c',COMBINATIONS.index(comb[0]),COMBINATIONS.index(res[0]))
             print('l',[c[:-1] for c in comb[1]],[c[:-1] for c in res[1]],compare_list([c[:-1] for c in comb[1]],[c[:-1] for c in res[1]]))
             print('111111111111DDDDDD')
             res[0]=comb[0]
             res[1]=comb[1]
             res[2]=[]
             for c in comb[1]:
                 if c[:-1] not in res[2]:
                     res[2].append(c[:-1])
                     
             res[2]+=sorted([c[:-1] for c in CARDS if c not in comb[1]],key=Hand(list(item)).sort_hand_nom)[:5-len(res[1])]
             print('RES',res)
     return res[0],res[2]
##     H=Hand(community_cards)
##     print('ffffffffffffff',H.is_combination())
     
        
def main():

    #print( hand(["K♠", "A♦"], ["10♣", "4♥", "9♥", "2♥", "3♦"]))
    #print( hand(["5♠", "6♠"], ["7♠", "8♠", "9♠", "J♠", "10♠"]))
    #print( hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]))
    #print( hand(["3♠", "2♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]))
    #print( hand(["3♠", "3♦"], ["2♣", "3♥", "2♠", "3♥", "2♦"]))
    #print( hand(["3♠", "3♦"], ["2♣", "2♥", "2♠", "3♥", "2♦"]))
    #print( hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]))
    #print( hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]))
    #print( hand(["Q♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "3♦"]))
    #print( hand(["3♠", "2♦"], ["J♣", "10♥", "9♥", "K♥", "Q♦"]))
    print( hand(['3♣', '5♣'], ['7♣', '2♣', 'K♣', 'K♥', '6♣']))
    #print( hand(['A♠', 'K♦'], ['J♥', '5♥', '10♥', 'Q♥', '3♥']))
    #print( hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]))

    
if __name__ == "__main__":
    main()




#
