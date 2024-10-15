


class Direction(object):
   def __init__(self, name, description):
        self.name = name
        self.description = description
       
    

class Dir_iOS(Direction):
   def __init__(self, name,description,theory_practic,hours=0,tasks={},professor=[], interns=[]):
        super().__init__(name,description)
        self.theory_practic = theory_practic
        self.professor=[]
        self.interns=[]
        self.hours=hours
        self.tasks={}
        
   def add_prof(self,prof):
    
      if prof and prof.name not in self.professor:
        
         
         self.professor.append(prof.name)
         
         if self not in prof.courses.values():
            print('self',self)
            prof.add_course(self)
         else:
            print("Курс уже добавлен")
   
      return self.professor

   def add_intern(self,intern):
      if intern and intern.name not in self.interns:
         self.interns.append(intern.name)
         
         if self not in intern.courses:
            intern.add_course(self)
         else:
            print("Курс уже добавлен")    
      return self.interns

   def add_task(self, task):

      if task not in self.tasks.keys():
         self.tasks[task]='0'
      else:
         print("Такое задание есть")

      
      

   def to_dict(self):
      fields={
         'name':self.name,
         'description':self.description,
         'theory_practic':self.theory_practic,
         'professor':self.professor,
         'interns':self.interns,
         'hours':self.hours,
         'tasks':self.tasks,
         }
      return fields

   
        
       
        
   def __repr__(self):
       return "<name:%s description:%s theory_practic:%s professor:%s>" % (self.name,self.description,self.theory_practic,self.professor)
   def __str__(self):
        return "Название-%s Описание-%s Теория/практика - %s Преподаватель %s"  % (self.name,self.description,self.theory_practic,self.professor)
   def __iter__(self):
        return self    
          
