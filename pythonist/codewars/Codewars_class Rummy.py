from itertools import permutations
class Hand(object):

    
    NOMINAL_F=['A','2','3','4','5','6','7','8','9','T','J','Q','K']
    NOMINAL_F1=['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    NOMINAL_S=['♠','♣','♦','♥']
    SCORE_P=dict(zip(NOMINAL_F,range(1,14)))
    SCORE=dict(zip(NOMINAL_F,range(2,15)))
    
    

    def __init__(self, card_lst):
        self.card_lst=card_lst

    def get_hand(self):
        return self.card_lst

    def add_card(self,c):
        remove_card=''
        count=1000
        self.card_lst.append(c)
        print(self.get_hand())
        for c in self.card_lst:
            print(c)
            self.card_lst.remove(c)
            print(self.get_hand())
            print(self.get_score())
            if self.get_score()==0:
                return c
            if self.get_score()<count:
                count=self.get_score()
                remove_card=c
            self.card_lst.insert(0,c)
            print(self.get_hand())
        print(count,remove_card)
        self.card_lst.remove(remove_card)
        return remove_card

    def max_card(self,c):
        return self.SCORE[c[0]]
        
    def get_score1(self):
        result=0
        alst=self.get_hand()
        astr=' '.join(self.get_hand())
        check_set=[f for f in self.NOMINAL_F if astr.count(f)>2]
        print('CS',check_set)
        alst=[c for c in alst if c[0] not in check_set]
        #print('A',alst)
        astr=' '.join(alst)
        check_series=[f for f in self.NOMINAL_S if astr.count(f)>2]
        #print('CSER',check_series)
        for cs in check_series:
            temp=sorted([t for t in alst if t[1]==cs])
            if self.SCORE[temp[-1][0]]-self.SCORE[temp[0][0]]==len(temp)-1:
                alst=[c for c in alst if c[1]!=cs]
            else:
                for j in range(len(alst),2,-1):
                    for item in permutations(temp,j):
                        item=sorted(item,key=self.max_card)
                        if self.SCORE[item[-1][0]]-self.SCORE[item[0][0]]==j-1:
                             alst=[c for c in alst if c not in item]
                             break 
       # print('A',alst)
        result=sum(self.SCORE_P[c[0]] for c in alst)
        print(result)
        alst=self.get_hand()
        astr=' '.join(self.get_hand())
        check_series=[f for f in self.NOMINAL_S if astr.count(f)>2]
        #print('2-CSER',check_series)
        for cs in check_series:
            temp=sorted([t for t in alst if t[1]==cs])
            if self.SCORE[temp[-1][0]]-self.SCORE[temp[0][0]]==len(temp)-1:
                alst=[c for c in alst if c[1]!=cs]
            else:
                for j in range(len(alst),2,-1):
                    for item in permutations(temp,j):
                        item=sorted(item,key=self.max_card)
                        if self.SCORE[item[-1][0]]-self.SCORE[item[0][0]]==j-1:
                             alst=[c for c in alst if c not in item]
                             break 
        #print('2-A',alst)
        astr=' '.join(alst)
        #print(astr)
        check_set=[f for f in self.NOMINAL_F if astr.count(f)>2]
        #print('2-CS',check_set)
        alst=[c for c in alst if c[0] not in check_set]
        #print('2A-A',alst)
        result=min(result,sum(self.SCORE_P[c[0]] for c in alst))
        return result
              
        
    def __str__(self):
        return self.card_lst
    
  
                
                    
    def get_score(self):
        result=0
        alst=self.get_hand()
        astr=' '.join(self.get_hand())
        check_set=[f for f in self.NOMINAL_F if astr.count(f)>2]
        print('CS',check_set)
        alst=[c for c in alst if c[0] not in check_set]
        #print('A',alst)
        astr=' '.join(alst)
        check_series=[f for f in self.NOMINAL_S if astr.count(f)>2]
        #print('CSER',check_series)
        for cs in check_series:
            temp=sorted([t for t in alst if t[1]==cs])
            if self.SCORE[temp[-1][0]]-self.SCORE[temp[0][0]]==len(temp)-1:
                alst=[c for c in alst if c[1]!=cs]
            else:
                for j in range(len(alst),2,-1):
                    for item in permutations(temp,j):
                        item=sorted(item,key=self.max_card)
                        if self.SCORE[item[-1][0]]-self.SCORE[item[0][0]]==j-1:
                             alst=[c for c in alst if c not in item]
                             break 
       # print('A',alst)
        result=sum(self.SCORE_P[c[0]] for c in alst)
        print(result)
        alst=self.get_hand()
        astr=' '.join(self.get_hand())
        check_series=[f for f in self.NOMINAL_S if astr.count(f)>2]
        #print('2-CSER',check_series)
        for cs in check_series:
            temp=sorted([t for t in alst if t[1]==cs])
            if self.SCORE[temp[-1][0]]-self.SCORE[temp[0][0]]==len(temp)-1:
                alst=[c for c in alst if c[1]!=cs]
            else:
                for j in range(len(alst),2,-1):
                    for item in permutations(temp,j):
                        item=sorted(item,key=self.max_card)
                        if self.SCORE[item[-1][0]]-self.SCORE[item[0][0]]==j-1:
                             alst=[c for c in alst if c not in item]
                             break 
        #print('2-A',alst)
        astr=' '.join(alst)
        #print(astr)
        check_set=[f for f in self.NOMINAL_F if astr.count(f)>2]
        #print('2-CS',check_set)
        alst=[c for c in alst if c[0] not in check_set]
        #print('2A-A',alst)
        result=min(result,sum(self.SCORE_P[c[0]] for c in alst))
        return result
                           
    


def main():

    P=Hand(['5♠', '4♠', '3♣', '8♠', '5♦', '6♠', '3♦'])
   
    #P.add_card('7H')
    
    print(P.add_card('A♥'))
    print(P.get_score())
  

if __name__ == "__main__":
    main()

#
