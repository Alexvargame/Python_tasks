import tkinter as tk
from tkinter import *
from class_housing import *
import pandas as pd
from report1 import *

class child_search:
   def __init__(self, master):
    #super().__init__(self, master)
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
    self.AdressCityString = tk.StringVar()
    self.AdressStreetString = tk.StringVar()

    def city(event):
      self.ent_adress_city.delete(0, END)
      self.ent_adress_city.insert(0, box_city.get(box_city.curselection()))
    def street(event):
      self.ent_adress_street.delete(0, END)
      self.ent_adress_street.insert(0, box_street.get(box_street.curselection()))


    
    self.slave = Toplevel(master)
    self.slave.title('Поиск по параметрам')
    self.slave.geometry('350x550+400+200')

    fr_1 = Frame(self.slave)
    fr_1.pack()

    fr_2 = Frame(self.slave)
    fr_2.pack()

    fr_but = Frame(self.slave)
    fr_but.pack()

    self.lbl_adress = Label(fr_1, text="Адрес")
    self.lbl_adress_city = Label(fr_1, text="Н.Пункт")
    self.lbl_adress_street = Label(fr_1, text="Улица")
    self.lbl_adress.grid(row=0, column=0, sticky="e")
    self.lbl_adress_city.grid(row=1, column=0, sticky="e")
    self.lbl_adress_street.grid(row=2, column=0, sticky="e")
    #self.ent_adress_city = Entry(fr_1, width=50, textvariable=self.AdressCityString)
    #self.ent_adress_street = Entry(fr_1, width=50, textvariable=self.AdressStreetString)
    #self.ent_adress_city.grid(row=1, column=1)
    #self.ent_adress_street.grid(row=3, column=1)
    

    
    values_city = []
    values_city.insert(0, "")
    with open('Населенные пункты.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_city.append(line.replace('\n', ''))
    combi_city = ttk.Combobox(fr_1, values=values_city, textvariable=self.AdressCityString)
    combi_city.grid(row=1, column=1, sticky="w")

    
    
    values_street = []
    values_street.insert(0, "")
    with open('Улицы.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_street.append(line.replace('\n', ''))
    combi_street = ttk.Combobox(fr_1, values=values_street, textvariable=self.AdressStreetString)
    combi_street.grid(row=2, column=1, sticky="w")

     
    self.lbl_char = Label(fr_2, text="Характеристики")
    self.lbl_char.grid(row=0, column=0, sticky="e")
    self.lbl_rooms = Label(fr_2, text="Кол-во комнат")
    self.ent_rooms_min = Entry(fr_2, width=10, textvariable=self.Rooms_min)
    self.ent_rooms_max = Entry(fr_2, width=10, textvariable=self.Rooms_max)
    self.lbl_rooms.grid(row=1, column=0, sticky="e")
    self.ent_rooms_min.grid(row=1, column=1, sticky="w")
    self.ent_rooms_max.grid(row=1, column=2, sticky="e")
    
    self.lbl_floor = Label(fr_2, text="Этаж")
    self.ent_floor_min = Entry(fr_2, width=10, textvariable=self.Floor_min)
    self.ent_floor_max = Entry(fr_2, width=10, textvariable=self.Floor_max)
    self.lbl_floor.grid(row=2, column=0, sticky="e")
    self.ent_floor_min.grid(row=2, column=1, sticky="w")
    self.ent_floor_max.grid(row=2, column=2, sticky="e")


    self.lbl_floors = Label(fr_2, text="Этажность")
    self.ent_floors_min = Entry(fr_2, width=10, textvariable=self.Floors_min)
    self.ent_floors_max = Entry(fr_2, width=10, textvariable=self.Floors_max)
    self.lbl_floors.grid(row=3, column=0, sticky="e")
    self.ent_floors_min.grid(row=3, column=1, sticky="w")
    self.ent_floors_max.grid(row=3, column=2, sticky="e")

    plans = ["Улучшенная", "Обычная"]
    self.dropdown1 = OptionMenu(fr_2, self.Plan, *plans)
    self.dropdown1.grid(row=4,column=1, sticky="w")


    self.lbl_price = Label(fr_2, text="Цена")
    self.ent_price_min = Entry(fr_2, width=10, textvariable=self.Price_min)
    self.ent_price_max = Entry(fr_2, width=10, textvariable=self.Price_max)    
    self.lbl_price.grid(row=5, column=0, sticky="e")
    self.ent_price_min.grid(row=5, column=1, sticky="w")
    self.ent_price_max.grid(row=5, column=2, sticky="e")


    self.btn_find = Button(fr_but, text="Найти", command=self.search_stat)
    self.btn_find.grid(row=7, column=1, sticky='w')
    
    #self.btn_excel = Button(self.slave, text="Вывод в таблицу")#, command=self.new_search )
    #self.btn_excel.grid(row=7, column=1, sticky='w')
    
    self.btn_end = Button(fr_but, text="Завершить", command=self.end_stat)
    self.btn_end.grid(row=8, column=1, sticky='w')
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
            print(len(line))
            if len(line)>1:     #длина 1 , потому что там \n
              l = line.split(',')
              l.insert(index, 0)
              l_ad = l[1].split('.')
              if (int(self.Rooms_min.get())<=int(l[2])<=int(self.Rooms_max.get())
                     and int(self.Floor_min.get())<=int(l[3])<=int(self.Floor_max.get())
                     and int(self.Floors_min.get())<=int(l[4])<=int(self.Floors_max.get())
                     and int(self.Price_min.get())<=int(l[6])<=int(self.Price_max.get())
                     and (self.AdressCityString.get()==l_ad[0] or self.AdressCityString.get()=="")
                     and (self.AdressStreetString.get()==l_ad[1] or self.AdressStreetString.get()=="")
                  ):
              
                     l[0]=i 
                     line=','.join(map(str,l))
                     i = i+1
                     print(line)
                     with open('2.txt', 'a') as output_file:
                       self.text = line.strip()
                       output_file.write(self.text + '\n')          
          
                        
      self.report_search = child_report_search(self.slave)
      self.slave.grab_set()
      self.slave.focus_set()
      self.slave.wait_window()
    

    

      

      
   def end_stat(self):

       self.slave.destroy()
