


class Employee(object):
   def __init__(self, name,courses={}):
        self.name = name
        self.courses = courses
   
         
      
      
   def list_courses(self):
      for key in self.courses.keys():
         print(key)
   
    

class Professor(Employee):
   def __init__(self, name,courses={}, projects='Full'):
        super().__init__(name,courses={})
        self.projects=projects

   def to_dict(self):
##      courses_l={}
##      for cur in self.courses.values():
##         key,value=cur.name, cur.hours
##         courses_l[key]=value
    
      fields={
         'name':self.name,
         'courses':self.courses,
         'projects':self.projects,
         }
      return fields

   def change_hours(self,cur,h):
      self.courses[cur.name]=h
      return self.courses
      
      
      

   def add_course(self,cur):
      
      if cur.name not in self.courses.keys():# and self.name not in cur.professor:
         self.courses[cur.name]=cur.hours
         cur.add_prof(self)
         
      else:
         print("курс прикрепоен к преподавателю")
      
      return self.courses
        
       
        
   def __repr__(self):
       return "<name:%s courses:%s>" % (self.name,self.courses)
   def __str__(self):
        return "Имя-%s Курсы-%s "  % (self.name,self.courses)
   def __iter__(self):
        return self    
          
class Intern(Employee):
   def __init__(self, name,courses={}, projects='Part'):
        super().__init__(name,courses={})
        self.projects=projects

   def add_course(self,cur):
      
      if cur.name not in self.courses.keys():# and self.name not in cur.interns:
         self.courses[cur.name]=cur.tasks
         cur.add_intern(self)
      else:
         print("интерн записан на курс")

      return self.courses

   def add_point(self,cur,task,point):
      self.courses[cur.name][task]=point
      return self.courses

   def result(self,cur):
      res=0
      #for value in self.courses.values():
      for v in self.courses[cur.name].values():
            res=res+int(v) 
      res=res/len(self.courses[cur.name].values())
      return f"Средний балл по курсу {cur.name} - {res}"
   
         
   def to_dict(self):
##      courses_l={}
##      for cur in self.courses.values():
##         key,value=cur.name, cur.tasks
##         courses_l[key]=value
    
      fields={
         'name':self.name,
         'courses':self.courses,
         'projects':self.projects,
         }
      return fields
        
       
        
   def __repr__(self):
       return "<name:%s courses:%s>" % (self.name,self.courses)
   def __str__(self):
        return "Имя-%s Курсы-%s "  % (self.name,self.courses)
   def __iter__(self):
        return self  
