import pickle
    

class Users():
   #default_name = "Undefined"
   def __init__ (self, id_user, name, nik, mail, password, time_last_vizit, accept='user',  text_info=None):#name2=None, family=None, country=None, city=None, text_info=None):
        self.id_user =id_user
        self.name = name
        #if name2:
        #self.name2 =name2
       # else: self.name = Users.default_name
       # if family:
        #self.family = family
     #   else: self.family = Users.default_name
        self.nik = nik
        self.mail = mail
        self.password = password
        self.time_last_vizit=time_last_vizit
        self.accept = accept
       # if text_info:
        self.text_info = text_info
        #self.country = country
        #self.city = city
        self.add_info={'name2': [None, None], 'family': [None, None],'country': [None, None],'city': [None, None],}
        self.print_info=[]
        
       # else: self.text_info = Users.default_name 
        
   def __repr__(self):
       
       return "<id_user:%s name:%s nik:%s mail:%s password:%s accet:%s time_last_vizit:%s text_info:%s print_info:%s>" % (self.id_user, self.name, self.nik,
                                                   self.mail, self.password, self.accept, self.time_last_vizit, self.text_info, self.print_info)
   def __str__(self):
        return "%s %s %s %s %s %s %s %s %s" %(self.id_user,self.name, self.nik,  self.mail, self.password, self.accept, self.time_last_vizit, self.text_info, self.print_info)
   def __iter__(self):
        return self    
   def pickle(self, file):
           with open(file, 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
           
   def pickle_search(self):
           with open('_Obj_temp.txt', 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
   def compare(self, b):
      if(self.name==b.name and self.nik==b.nik and self.mail==b.mail and self.nik==b.nik):
         return True
   def compare1(self, b):
      val1=0
      val2=0
      val3=0
      if(self.name==b.name):
         val1=1
      elif (self.nik==b.nik):
         val2=1
      elif (self.mail==b.mail):
         val3=1
         return val1, val2, val3
   def assign(self, b):
      b.id_user=self.id_user
      b.name=self.name
      #b.name2=self.name2
      #b.family=self.family
      b.nik=self.nik
      b.mail=self.mail
      b.password=self.password
      b.accept=self.accept
      b.text_info=self.text_info
      #b.country=self.country
      #b.city=self.city
      b.time_last_vizit=self.time_last_vizit
      b.add_info=self.add_info.copy()
      return b
  
   def print_info_(self):
      for key, value in self.add_info.items():
          if value[1]==1:
             self.print_info.append(value[0])
      return self.print_info
   def convert_to_tuple(self):
        t=(self_add_date, self.types, self.city)
        return t   
   @staticmethod
   def unpickle(self):
            with open('11.txt', 'rb') as f:
               return pickle.load(f)

