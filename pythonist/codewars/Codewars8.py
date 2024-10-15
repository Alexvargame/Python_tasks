
class Task:
    def __init__(self,name,rank=-8):
        
        self.name=name
        self.rank=rank
       

    def __str__(self):
        return f'Имя- {self.name} Ранг- {self.rank}'

class User:

    def __init__(self,name,rank=-8, progress=0):
        
        self.name=name
        self.rank=rank
        self.progress=progress

    def __str__(self):
        return f'Имя- {self.name} Ранг- {self.rank}  Прогресс- {self.progress}'

    def inc_progress(self, task):
        if (self.rank <0 and task.rank<0)or(self.rank >0 and task.rank>0):
            if self.rank>task.rank and abs(abs(self.rank)-abs(task.rank))>1:
                
                return self
            
            elif self.rank>task.rank and abs(abs(self.rank)-abs(task.rank))==1:
                self.progress=self.progress+1
                if self.progress>100:
                    self.progress=self.progress-100
                    if self.rank!=-1:
                        if self.rank!=8:
                            self.rank=self.rank+1
                    else:
                        self.rank=self.rank+2
                return self
                        
            elif self.rank==task.rank:
                self.progress=self.progress+3
                if self.progress>100:
                    self.progress=self.progress-100
                    if self.rank!=-1:
                        if self.rank!=8:
                            self.rank=self.rank+1
                    else:
                        self.rank=self.rank+2
                return self
            
            elif self.rank<task.rank:
                self.progress=self.progress+10*(abs(self.rank-task.rank))**2
                if self.progress>100:
                    self.progress=self.progress-100
                    if self.rank!=-1:
                        if self.rank!=8:
                            self.rank=self.rank+1
                    else:
                        self.rank=self.rank+2
                return self
        elif self.rank >0 and task.rank<0:
            if self.rank>task.rank and abs(abs(self.rank)-abs(task.rank))>1:
                
                return self
            
            elif self.rank>task.rank and abs(abs(self.rank)-abs(task.rank))==0:
                self.progress=self.progress+1
                if self.progress>100:
                    self.progress=self.progress-100
                    if self.rank!=-1:
                        if self.rank!=8:
                            self.rank=self.rank+1
                    else:
                        self.rank=self.rank+2
                return self
        elif self.rank <0 and task.rank>0:
            print('w',10*(abs(self.rank-task.rank))**2)
            self.progress=self.progress+10*(abs(self.rank-task.rank))**2
            if self.progress>100:
                temp=self.progress//100
                self.progress=self.progress-100*temp
                if self.rank!=-1:    
                    self.rank=self.rank+temp
                    if self.rank!=8:
                        self.rank=8
                        
                else:
                    self.rank=self.rank+2
            return self
                


def main():

    A=User('Alex',-5,99)
    B=User('Bob',-1,100)
    t1=Task('1')
    t2=Task('2',-6)
    t3=Task('2',-5)
    t4=Task('2',7)
    print(A)
    print(B)
    print(t1)
    A.inc_progress(t1)
    print(A)
    input()
    A.inc_progress(t2)
    print(A)
    input()
    A.inc_progress(t3)
    print(A)
    input()
    A.inc_progress(t4)
    print(A)
    input()
        
    
if __name__ == "__main__":
    main()




#
