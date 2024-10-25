import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from class_housing import *
import pandas as pd
from Enter_info import *
from Enter_info_house import *
from Enter_info_gost import *




class child:
   def __init__(self, master, user):

      
    self.slave = Toplevel(master)
    self.slave.title('Выберите тип объекта')
    self.slave.geometry('250x150+300+275')
    self.user=user
    self.ObjectString = tk.StringVar()
    objects = ["Квартира", "Дом", "Гостинка"]

    self.ObjectString.set("Выберите тип объекта")
    self.dropdown = OptionMenu(self.slave, self.ObjectString, *objects, command=self.func)
    self.dropdown.pack(expand=1)
    self.btn_choise = Button(self.slave, text="Выбрать", command=self.openDialog1)
    self.btn_choise.pack(expand=1)
    self.btn_end = Button(self.slave, text="Завершить", command=self.end_stat)
    self.btn_end.pack(expand=1)
   
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()

   def func(self, t):
      self.t=self.ObjectString.get()
     
      
   def openDialog1(self):
      if (self.ObjectString.get() == 'Квартира'): 
         child_ent(self.slave, self.user)
      elif(self.ObjectString.get() == 'Дом'):
         child_ent_house(self.slave, self.user)
      elif(self.ObjectString.get() == 'Гостинка'):
         child_ent_gost(self.slave, self.user)
   def end_stat(self):
       self.slave.destroy()
         
  
   def end_stat(self):
   
       self.slave.destroy()
