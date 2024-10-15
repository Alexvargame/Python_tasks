
class User:

    def __init__(self,rank=-8, progress=0):
    
        self.rank=rank
        self.progress=progress

    def __str__(self):
        return f'Ранг: {self.rank}  Прогресс: {self.progress}'

    def inc_progress(self, rank):
        if rank<-8 or rank>8 or rank==0:
            raise ValueError 
        if self.rank==8:
            self.progress=0
            return self
        if (self.rank <0 and rank<0)or(self.rank >0 and rank>0):
            if self.rank>rank and abs(abs(self.rank)-abs(rank))>1:
                print('R',rank,self)
                return self
            
            elif self.rank>rank and abs(abs(self.rank)-abs(rank))==1:
                print('RR',rank,self)
##                if self.progress==0:
##                    self.rank=self.rank+1
##                    self.progress=self.progress+1
##                    return self
                    
                self.progress=self.progress+1
                if self.progress>99:
                    self.progress=self.progress-100
                    if self.rank!=-1:
                        if self.rank!=8:
                            self.rank=self.rank+1
                    else:
                        self.rank=self.rank+2
                return self
                        
            elif self.rank==rank:
                print('RRR',rank,self)
                self.progress=self.progress+3
                if self.progress>99:
                    self.progress=self.progress-100
                    if self.rank!=-1:
                        if self.rank!=8:
                            self.rank=self.rank+1
                    else:
                        self.rank=self.rank+2
                return self
            
            elif self.rank<rank:
                print('RRRR',rank,self)
                self.progress=self.progress+10*(abs(self.rank-rank))**2
                if self.progress>99:
                    temp=self.progress//100
                    print(temp)
                    print(self.progress)
                    self.progress=self.progress-100*temp
                    print(self.progress)
                    if self.rank!=-1:    
                        self.rank=self.rank+temp
                        if self.rank>=8:
                            self.rank=8
                            self.progress=0
                    else:
                        self.rank=self.rank+2
                return self
        elif self.rank >0 and rank<0:
            print('RRRRR',rank,self)
            if self.rank>rank and abs(abs(self.rank)-abs(rank))>1:
                
                return self
            
            elif self.rank>rank and abs(abs(self.rank)-abs(rank))==0:
                self.progress=self.progress+1
                if self.progress>99:
                    self.progress=self.progress-100
                    if self.rank!=-1:
                        if self.rank!=8:
                            self.rank=self.rank+1
                    else:
                        self.rank=self.rank+2
                return self
        elif self.rank <0 and rank>0:
            print('RRRRRR',rank,self)
            self.progress=self.progress+10*(abs(self.rank-rank)-1)**2
            print(self.progress)
            if self.progress>99:
                temp=self.progress//100
                self.progress=self.progress-100*temp
                if self.rank!=-1:
                    if temp>abs(self.rank):
                        self.rank=self.rank+temp+1
                    else:
                        self.rank=self.rank+temp
                    if self.rank>=8:
                        self.rank=8
                        self.progress=0
                    if self.rank==0:
                        self.rank=1
                        
                else:
                    self.rank=self.rank+2
            return self
                


def main():

    A=User(7,0)
    B=User(7,40)
   
##    print(A)
##    print(B)
##
##    A.inc_progress(-7)
##    print(A)
##    input()
##    A.inc_progress(-5)
##    print(A)
##    input()
##    A.inc_progress(-5)
##    print(A)
##    input()
    A.inc_progress(-7)
    print(A)

if __name__ == "__main__":
    main()




#
