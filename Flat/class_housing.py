import pickle



class Housing(object):
   def __init__(self, id_object, author_object, add_date, types, city, street, district, num_house, num_kor, price, text_info):
        self.types = types
        self.city = city
        self.street = street
        self.num_house = num_house
        self.num_kor = num_kor
        self.district = district
        self.price = price
        self.add_date = add_date
        self.text_info = text_info
        self.id_object = id_object
        self.author_object = author_object
    

class Flats(Housing):
   def __init__(self, id_object, author_object, add_date, types, city, street, district, num_house, num_kor, rooms, floor, floors, square, plan, price, text_info):
        super().__init__( id_object, author_object, add_date, types, city, street, district, num_house, num_kor, price, text_info) 
        self.rooms = rooms
        self.floor = floor
        self.floors = floors
        self.square = square
        self.plan = plan
        
   def __repr__(self):
       return "<id_object:%s author_object:%s, add_date:%s types:%s city:%s street:%s disctrict:%s num_house:%s num_kor:%s rooms:%s floor:%s floors:%s plan:%s price:%s square:%stext_info:%s>" % (id_object, author_object,self.add_date,
         self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
          self.rooms, self.floor, self.floors, self.plan, self.price, self.square, self.text_info)
   def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s  " % (self.id_object, self.author_object, self.add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
          self.rooms, self.floor, self.floors, self.plan, self.price, self.square, self.text_info)
   def __iter__(self):
        return self    
   def pickle(self, file):
           with open(file, 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
           
   def pickle_search(self):
           with open('_Obj_temp.txt', 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
   def compare(self, b):
      if(b.id_object == self.id_object and b.author_object == self.author_object
         and self.add_date==b.add_date and self.types==b.types and self.city==b.city and self.street==b.street
         and self.district==b.district and self.num_house==b.num_house and self.num_kor==b.num_kor 
         and self.rooms==b.rooms and self.floor==b.floor and self.floors==b.floors and self.plan==b.plan
         and self.price==b.price and self.square==b.square and self.text_info==b.text_info):
         return True
   def assign(self, b):
      b.add_date=self.add_date
      b.types=self.types
      b.city=self.city
      b.street=self.street
      b.district=self.district
      b.num_house=self.num_house
      b.num_kor=self.num_kor 
      b.rooms=self.rooms
      b.floor=self.floor
      b.floors=self.floors
      b.plan=self.plan
      b.price=self.price
      b.square=self.square
      b.text_info=self.text_info
      b.id_object = self.id_object
      b.author_object = self.author_object
      return b
   
   
   def convert_to_tuple(self):
        t=(self_add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
           self.rooms, self.floor, self.floors, self.plan, self.price, self.square, self.text_info)
        return t   
   @staticmethod
   def unpickle(self):
            with open('11.txt', 'rb') as f:
               return pickle.load(f)
   
        
class Houses (Housing):
   def __init__(self, id_object, author_object, add_date, types, city, street, district, num_house, num_kor, rooms, floors, square, land, part, price, text_info):
        
        super().__init__(id_object, author_object, add_date, types, city, street, district, num_house, num_kor, price, text_info) 
        self.rooms = rooms
        self.floors = floors
        self.square = square
        self.land = land
        self.part = part
   def __repr__(self):
       return "<id_object:%s author_object:%s add_date:%s types:%s city:%s street:%s disctrict:%s num_house:%s num_kor:%s appart:%s rooms:%s floors:%s square:%s land:%s part:%s price:%s text_info:%s>" % (self.id_object, self.author_object,
            self.add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
          self.rooms, self.floors, self.square, self.land, self.part, self.price, self.text_info)
   def __str__(self):
        return "%s %s  %s %s %s %s %s %s %s %s %s %s %s %s %s %s  " % (self.id_object, self.author_object, self.add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
          self.rooms, self.floors, self.square, self.land, self.part, self.price, self.text_info)
   def pickle(self, file):
           with open(file, 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
   def compare(self, b):
      if(b.id_object == self.id_object and b.author_object == self.author_object
         and self.add_date==b.add_date and self.types==b.types and self.city==b.city and self.street==b.street
         and self.district==b.district and self.num_house==b.num_house and self.num_kor==b.num_kor 
         and self.rooms==b.rooms and self.floors==b.floors and self.square==b.square and self.land==b.land
         and self.part==b.part and self.price==b.price and self.text_info==b.text_info):
         return True
   def assign(self, b):
      b.add_date=self.add_date
      b.types=self.types
      b.city=self.city
      b.street=self.street
      b.district=self.district
      b.num_house=self.num_house
      b.num_kor=self.num_kor 
      b.rooms=self.rooms
      b.floors=self.floors
      b.land=self.land
      b.part=self.part
      b.price=self.price
      b.square=self.square
      b.text_info=self.text_info
      b.id_object = self.id_object
      b.author_object = self.author_object
      return b
   def pickle_search(self):
           with open('_Obj_temp.txt', 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
   
   def convert_to_tuple(self):
        t=(self.add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
           self.rooms, self.floors, self.square, self.land, self. part, self.price, self.text_info)
        return t   
   @staticmethod
   def unpickle(self):
            with open('11.txt', 'rb') as f:
               return pickle.load(f)
   

class Gostinki(Housing):
   def __init__(self, id_object, author_object, add_date, types, city, street, district, num_house, num_kor, rooms, floor, floors, square, price, text_info):
        super().__init__(id_object, author_object, add_date, types, city, street, district, num_house, num_kor, price, text_info) 
        self.rooms = rooms
        self.floor = floor
        self.floors = floors
        self.square = square
   def __repr__(self):
       return "<id_object:%s author_object:%s add_date:%s types:%s city:%s street:%s disctrict:%s num_house:%s num_kor:%s appart:%s rooms:%s floor:%s floors:%s square:%s price:%stext_info:%s>" % (self.id_object, self.author_object,
          self.add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
          self.rooms, self.floor, self.floors, self.square, self.price, self.text_info)
   def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" % (self.id_object, self.author_object, self.add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
          self.rooms, self.floor, self.floors, self.square, self.price,  self.text_info)
        
   def pickle(self, file):
           with open(file, 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
   def compare(self, b):
      if(b.id_object == self.id_object and b.author_object == self.author_object
         and self.add_date==b.add_date and self.types==b.types and self.city==b.city and self.street==b.street
         and self.district==b.district and self.num_house==b.num_house and self.num_kor==b.num_kor 
         and self.rooms==b.rooms and self.floor==b.floor and self.floors==b.floors 
         and self.price==b.price and self.square==b.square and self.text_info==b.text_info):
         return True
   def assign(self, b):
      b.add_date=self.add_date
      b.types=self.types
      b.city=self.city
      b.street=self.street
      b.district=self.district
      b.num_house=self.num_house
      b.num_kor=self.num_kor 
      b.rooms=self.rooms
      b.floor=self.floor
      b.floors=self.floors
      b.price=self.price
      b.square=self.square
      b.text_info=self.text_info
      b.id_object = self.id_object
      b.author_object = self.author_object
      return b
           
   def pickle_search(self):
           with open('_Obj_temp.txt', 'ab') as f:
              pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
   
   def convert_to_tuple(self):
        t=(self.add_date, self.types, self.city, self.street, self.district, self.num_house, self.num_kor,
           self.rooms, self.floor, self.floors, self.price, self.square, self.text_info)
        return t   
   @staticmethod
   def unpickle(self):
            with open('11.txt', 'rb') as f:
               return pickle.load(f)
   
        
