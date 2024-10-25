class Housing(object):
   def __init__(self, types):
        self.types = types 
        self.floor = floor
        self.price = price
   def show(self):
       print("Rooms",self.rooms,"Floor",self.floor,"Price",self.price)            


      
class Flats(Housing):
   def __init__(self, rooms, floor, floors, plan, price):
        self.rooms = rooms
        self.floor = floor
        self.floors = floors
        self.plan = plan
        self.price = price
   def brake(self):
       if self.rooms==3:  
         print("Rooms",self.rooms,"Floor",self.floor,"Price",self.price)
       else:
         print("Это не трехкомтная квартира")
         
