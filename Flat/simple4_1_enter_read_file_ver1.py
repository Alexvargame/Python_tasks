import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from Enter_info import *
from Enter_info_house import *
from Search_info import *
from report import *
from boolean import *
from Type_object import *


from tkinter.filedialog import askopenfilename, asksaveasfilename

class main:
   def __init__(self, master):
      self.master = master
      self.master.title('DATA')
      self.master.geometry('150x150+300+225')
      self.button1 = Button(self.master,
                            text="Жилые объекты",
                            command = self.openDialog)
      self.button1.pack(side = TOP)
      self.button2 = Button(self.master, text="Oтчет",
                            command = self.openReport)
      self.button2.pack(side = BOTTOM)

      self.button3 = Button(self.master, text="Поиск",
                            command = self.openSearch)
      self.button3.pack(side = LEFT)

      
      self.master.protocol('WM_DELETE_WINDOW', 
                         self.exitMethod)
      self. master.mainloop()

   def openDialog(self):
      child(self.master)

   def openReport(self):
      self.report = child_report(self.master)
      with open('1.txt', 'r') as output_file:
           self.t = output_file.read() 
           self.returnText = self.report.go(self.t)
           
       
              
   def openSearch(self):
    child_search(self.master)   

   def exitMethod(self):
    self.dialog = yesno(self.master)
    self.returnValue = self.dialog.go('question',
                                      'Вы хотите выйти?')
    if self.returnValue:
      self.master.destroy()
      
class Housing(object):
   def __init__(self, types, rooms, floor, floors, plan, prices, square, land, part):
        self.types = types
        self.rooms = rooms
        self.floor = floor
        self.floors = floors
        self.plan = plan
        self.price = price
        self.square = square
        self.land = land
        self.part = part
        


class Flats(Housing):
   def __init__(self, rooms, floor, floors, plan, price, square):
        self.rooms = rooms
        self.floor = floor
        self.floors = floors
        self.plan = plan
        self.price = price
        self.square = square

        
class Houses (Housing):
   def __init__(self, rooms, floors, prices, square, land, part):
        self.rooms = rooms
        self.floors = floors
        self.price = price
        self.square = square
        self.land = land
        self.part = part
        
root = Tk()
main(root)
      
    
