import tkinter as tk
from tkinter import *
from class_housing import *
import pandas as pd
from report1 import *

class child_search:
   def __init__(self, master):

    self.Rooms_min = tk.StringVar()
    self.Rooms_max = tk.StringVar()
    
    self.Floor_min = tk.StringVar()
    self.Floor_max = tk.StringVar()
    self.Floors_min = tk.StringVar()
    self.Floors_max = tk.StringVar()
    self.Plan = tk.StringVar()
    self.Price_min = tk.StringVar()
    self.Price_max = tk.StringVar()
    self.resultString = tk.StringVar()

    
    self.slave = Toplevel(master)
    self.slave.title('Поиск по параметрам')
    self.slave.geometry('300x250+500+375')
    self.lbl_rooms = Label(self.slave, text="Кол-во комнат")
    self.ent_rooms_min = Entry(self.slave, width=10, textvariable=self.Rooms_min)
    self.ent_rooms_max = Entry(self.slave, width=10, textvariable=self.Rooms_max)
    self.lbl_rooms.grid(row=0, column=0, sticky="e")
    self.ent_rooms_min.grid(row=0, column=1, sticky="w")
    self.ent_rooms_max.grid(row=0, column=2, sticky="e")
    
    self.lbl_floor = Label(self.slave, text="Этаж")
    self.ent_floor_min = Entry(self.slave, width=10, textvariable=self.Floor_min)
    self.ent_floor_max = Entry(self.slave, width=10, textvariable=self.Floor_max)
    self.lbl_floor.grid(row=1, column=0, sticky="e")
    self.ent_floor_min.grid(row=1, column=1, sticky="w")
    self.ent_floor_max.grid(row=1, column=2, sticky="e")


    self.lbl_floors = Label(self.slave, text="Этажность")
    self.ent_floors_min = Entry(self.slave, width=10, textvariable=self.Floors_min)
    self.ent_floors_max = Entry(self.slave, width=10, textvariable=self.Floors_max)
    self.lbl_floors.grid(row=2, column=0, sticky="e")
    self.ent_floors_min.grid(row=2, column=1, sticky="w")
    self.ent_floors_max.grid(row=2, column=2, sticky="e")

    plans = ["Улучшенная", "Обычная"]
    self.dropdown1 = OptionMenu(self.slave, self.Plan, *plans)
    self.dropdown1.grid(row=4,column=1, sticky="w")


    self.lbl_price = Label(self.slave, text="Цена")
    self.ent_price_min = Entry(self.slave, width=10, textvariable=self.Price_min)
    self.ent_price_max = Entry(self.slave, width=10, textvariable=self.Price_max)    
    self.lbl_price.grid(row=3, column=0, sticky="e")
    self.ent_price_min.grid(row=5, column=1, sticky="w")
    self.ent_price_max.grid(row=5, column=2, sticky="e")


    self.btn_find = Button(self.slave, text="Найти", command=self.search_stat)
    self.btn_find.grid(row=6, column=1, sticky='w')
    
    self.btn_find_excel = Button(self.slave, text="Найти в таблицу")#, command=self.search_stat)
    self.btn_find_excel.grid(row=7, column=1, sticky='w')
    
    
    self.btn_save = Button(self.slave, text="Завершить", command=self.end_stat)
    self.btn_save.grid(row=8, column=1, sticky='w')
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()

   
   def search_stat(self):
      
      
      
      if not self.Rooms_min.get():
             self.Rooms_min.set(1)
      if not self.Rooms_max.get():
             self.Rooms_max.set(100)
      if not self.Floor_min.get():
             self.Floor_min.set(1)
      if not self.Floor_max.get():
             self.Floor_max.set(100)
      if not self.Floors_min.get():
             self.Floors_min.set(1)
      if not self.Floors_max.get():
             self.Floors_max.set(100)
      if not self.Price_min.get():
             self.Price_min.set(1)
      if not self.Price_max.get():
             self.Price_max.set(1000000)

      f=open('2.txt', 'w')
      f.close()
      with open('1.txt', 'r') as output_file:
           
          self.t = output_file.readlines()
          index = 0
          i = 0
          for line in self.t:
              l = line.split(',')
              l.insert(index, 0) 
              if (int(self.Rooms_min.get())<=int(l[2])<=int(self.Rooms_max.get()) and int(self.Floor_min.get())<=int(l[4])<=int(self.Floor_max.get())
                     and int(self.Floors_min.get())<=int(l[6])<=int(self.Floors_max.get()) and int(self.Price_min.get())<=int(l[10])<=int(self.Price_max.get()) ):
                                      
                     l[0]=i #self.t.index(line)
                     line=','.join(map(str,l))
                     i = i+1
                     print(line.strip())
                     print(i)
                     
                     with open('2.txt', 'a') as output_file:
                       self.text = line.strip()
                       output_file.write(self.text + '\n')          
          
                        
      self.report_search = child_report_search(self.slave)
      self.slave.grab_set()
      self.slave.focus_set()
      self.slave.wait_window()
    
        
 
   def search_stat_excel(self):
      
      
      
      if not self.Rooms_min.get():
             self.Rooms_min.set(1)
      if not self.Rooms_max.get():
             self.Rooms_max.set(100)
      if not self.Floor_min.get():
             self.Floor_min.set(1)
      if not self.Floor_max.get():
             self.Floor_max.set(100)
      if not self.Floors_min.get():
             self.Floors_min.set(1)
      if not self.Floors_max.get():
             self.Floors_max.set(100)
      if not self.Price_min.get():
             self.Price_min.set(1)
      if not self.Price_max.get():
             self.Price_max.set(1000000)

      f=open('2.txt', 'w')
      f.close()
      with open('1.txt', 'r') as output_file:
           
          self.t = output_file.readlines()
          index = 0
          i = 0
          for line in self.t:
              l = line.split(',')
              l.insert(index, 0) 
              if (int(self.Rooms_min.get())<=int(l[2])<=int(self.Rooms_max.get()) and int(self.Floor_min.get())<=int(l[4])<=int(self.Floor_max.get())
                     and int(self.Floors_min.get())<=int(l[6])<=int(self.Floors_max.get()) and int(self.Price_min.get())<=int(l[10])<=int(self.Price_max.get()) ):
                                      
                     l[0]=i #self.t.index(line)
                     line=','.join(map(str,l))
                     i = i+1
                     print(line.strip())
                     print(i)

                     workbook = xlsxwriter.Workbook('2.xlsx')
                     worksheet = workbook.add_worksheet()
                     





                     with open('2.txt', 'a') as output_file:
                       self.text = line.strip()
                       output_file.write(self.text + '\n')          
          
                        
      self.report_search = child_report_search(self.slave)
      self.slave.grab_set()
      self.slave.focus_set()
      self.slave.wait_window()
    
        

      

      

   def end_stat(self):
   
       self.slave.destroy()
