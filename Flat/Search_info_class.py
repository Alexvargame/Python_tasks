import tkinter as tk
from tkinter import *
from class_housing import *
import pandas as pd
from report1_class import *
from ClassCalendar import *
from tkinter import messagebox as mb
from datetime import *

class child_search:
   def __init__(self, master, user):
    self.user=user
    self.Rooms_min = tk.IntVar()
    self.Rooms_max = tk.IntVar()
    
    self.Floor_min = tk.IntVar()
    self.Floor_max = tk.IntVar()
    self.Floors_min = tk.IntVar()
    self.Floors_max = tk.IntVar()
    self.Plan = tk.StringVar()
    self.Price_min = tk.DoubleVar()
    self.Price_max = tk.DoubleVar()
    self.Square_min = tk.DoubleVar()
    self.Square_max = tk.DoubleVar()
    self.resultString = tk.StringVar()
    self.AdressCityString = tk.StringVar()
    self.AdressStreetString = tk.StringVar()
    self.AdressDistrictString = tk.StringVar()
    self.TypeString = tk.StringVar()
    self.Date1 = tk.StringVar()
    self.Date2 = tk.StringVar()
    self.Period = tk.StringVar()
    self.Square_land_min = tk.DoubleVar()
    self.Square_land_max = tk.DoubleVar()
    self.value_city = []
    self.value_street = []
    self.value_district = []

    
    def city_add():
     select=list(box_city.curselection())
     for i in select:
       box_city1.insert(END, box_city.get(i))
       self.value_city.append(box_city.get(i))
     select.reverse()
     return self.value_city    
    def city_del():    
     select=list(box_city1.curselection())
     for i in select:
          for j in self.value_city:
             if j==box_city1.get(i):
                  self.value_city.remove(j)
          box_city1.delete(i)
     select.reverse()
     return self.value_city
    def street_add():
     select=list(box_street.curselection())
     for i in select:
       box_street1.insert(END, box_street.get(i))
       self.value_street.append(box_street.get(i))
     select.reverse()
     return self.value_street   
    def street_del():    
     select=list(box_street1.curselection())
     for i in select:
          for j in self.value_street:
             if j==box_street1.get(i):
                  self.value_street.remove(j)
          box_street1.delete(i)
     select.reverse()
     return self.value_street
    def district_add():
     select=list(box_district.curselection())
     for i in select:
       box_district1.insert(END, box_district.get(i))
       self.value_district.append(box_district.get(i))
     select.reverse()
     return self.value_district   
    def district_del():    
     select=list(box_district1.curselection())
     for i in select:
          for j in self.value_district:
             if j==box_district1.get(i):
                  self.value_district.remove(j)
          box_district1.delete(i)
     select.reverse()
     return self.value_district
    
    
    self.slave = Toplevel(master)
    self.slave.title('Поиск по параметрам')
    self.slave.geometry('550x550+250+150')

    fr_0 = Frame(self.slave)
    fr_0.pack()
    
    fr_1 = Frame(self.slave)
    fr_1.pack()

    self.fr_2 = Frame(self.slave)
    self.fr_2.pack()
   

    fr_but = Frame(self.slave)
    fr_but.pack()


    self.lbl_type_obj = Label(fr_0, text="Тип Объекта")
    self.lbl_type_obj.grid(row=0, column=2, sticky="e")
    values_type_obj = ['Квартира', 'Дом', 'Гостинка']   
    combi_type_obj = ttk.Combobox(fr_0, width=30, values=values_type_obj, textvariable=self.TypeString)
    combi_type_obj.grid(row=1, column=1, columnspan=3)
    combi_type_obj.bind('<<ComboboxSelected>>', self.frame_choice)
    

    self.lbl_date1 = Label(fr_0, text="Начальная дата")
    self.lbl_date2 = Label(fr_0, text="Конечная дата")
    self.lbl_period = Label(fr_0, text="Период")  
    self.lbl_date1.grid(row=3, column=1, sticky="w")
    self.lbl_date2.grid(row=3, column=3, sticky="e")
    self.lbl_period.grid(row=3, column=2)
    self.ent_date1 = Entry(fr_0, width=10, textvariable=self.Date1)
    self.ent_date2 = Entry(fr_0, width=10, textvariable=self.Date2)
    values_period = ['1 день', '3 дня', 'Неделя', 'Месяц', 'Другой период']   
    combi_period = ttk.Combobox(fr_0, width=12, values=values_period, textvariable=self.Period)
    combi_period.grid(row=4, column=2, sticky="w")
    combi_period.bind('<<ComboboxSelected>>', self.period_choice)
    
    self.ent_date1.grid(row=4, column=1, sticky="w")
    self.ent_date2.grid(row=4, column=3, sticky="e")
    self.btn_calen1 = Button(fr_0, text="<<", width=2, command=self.openCalendar)
    self.btn_calen1.grid(row=4, column=0, sticky='w')
    self.btn_calen2 = Button(fr_0, text=">>", width=2, command=self.openCalendar)
    self.btn_calen2.grid(row=4, column=4, sticky='w') 

    
    self.lbl_adress = Label(fr_0, text="Адрес", font=("Arial", 16, "bold"))
    self.lbl_adress_city = Label(fr_1, text="Населенный пункт")
    self.lbl_adress_street = Label(fr_1, text="Улица")
    self.lbl_adress_district = Label(fr_1, text="Район")
    self.lbl_adress.grid(row=5, column=1, columnspan=3)
    self.lbl_adress_city.grid(row=0, column=0, columnspan=3, sticky="w")
    self.lbl_adress_street.grid(row=4, column=0, columnspan=3, sticky="w")
    self.lbl_adress_district.grid(row=8, column=0, columnspan=3, sticky="w")
       
    box_city = Listbox(fr_1, height=3, selectmode=EXTENDED)
    box_city.grid(row=1, column=0, columnspan=3, rowspan=3, sticky="w")
    scroll = Scrollbar(fr_1, command=box_city.yview)
    box_city.config(yscrollcommand=scroll.set)
    with open('_Cities.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
           box_city.insert(END, line.replace('\n', ''))
    box_city1 = Listbox(fr_1, height=3, selectmode=EXTENDED)
    box_city1.grid(row=1, column=4, columnspan=3, rowspan=3,  sticky="w")
    scroll = Scrollbar(fr_1, command=box_city1.yview)
    box_city1.config(yscrollcommand=scroll.set)
    self.btn_add = Button(fr_1, text=">>", width=5, command=city_add)
    self.btn_add.grid(row=1, column=3, sticky='w')
    self.btn_del = Button(fr_1, text="<<", width=5, command=city_del)
    self.btn_del.grid(row=2, column=3, sticky='w') 

    box_street = Listbox(fr_1, height=3, selectmode=EXTENDED)
    box_street.grid(row=5, column=0, columnspan=3, rowspan=3, sticky="w")
    scroll = Scrollbar(fr_1, command=box_street.yview)
    box_street.config(yscrollcommand=scroll.set)
    with open('_Streets.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
           box_street.insert(END, line.replace('\n', ''))
    box_street1 = Listbox(fr_1, height=3, selectmode=EXTENDED)
    box_street1.grid(row=5, column=4, columnspan=3, rowspan=3, sticky="w")
    scroll = Scrollbar(fr_1, command=box_street1.yview)
    box_street1.config(yscrollcommand=scroll.set)
    self.btn_add = Button(fr_1, text=">>", width=5, command=street_add)
    self.btn_add.grid(row=6, column=3, sticky='w')
    self.btn_del = Button(fr_1, text="<<", width=5, command=street_del)
    self.btn_del.grid(row=7, column=3, sticky='w')

    box_district = Listbox(fr_1, height=3, selectmode=EXTENDED)
    box_district.grid(row=9, column=0,  columnspan=3, rowspan=3, sticky="w")
    scroll = Scrollbar(fr_1, command=box_district.yview)
    box_district.config(yscrollcommand=scroll.set)
    with open('_Districts.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
           box_district.insert(END, line.replace('\n', ''))
    box_district1 = Listbox(fr_1, height=3, selectmode=EXTENDED)
    box_district1.grid(row=9, column=4, columnspan=3, rowspan=3, sticky="w")
    scroll = Scrollbar(fr_1, command=box_district1.yview)
    box_district1.config(yscrollcommand=scroll.set)
    self.btn_add = Button(fr_1, text=">>", width=5, command=district_add)
    self.btn_add.grid(row=10, column=3, sticky='w')
    self.btn_del = Button(fr_1, text="<<", width=5, command=district_del)
    self.btn_del.grid(row=11, column=3, sticky='w') 

    self.btn_find = Button(fr_but, text="Найти", command=self.search_stat)
    self.btn_find.grid(row=1, column=1, sticky='w')
    self.btn_end = Button(fr_but, text="Завершить", command=self.end_stat)
    self.btn_end.grid(row=2, column=1, sticky='w')

    self.slave.wait_window()
   
   def frame_choice(self, event): 
         if self.TypeString.get()=='Квартира':
            self.frame_flats()
         elif self.TypeString.get()=='Дом':
            self.frame_house()
         elif self.TypeString.get()=='Гостинка':
            self.frame_gostinki()
            
   def period_choice(self, event): 
         if self.Period.get()=='1 день':
            self.Date2.set(date.today())
            self.Date1.set(date.today()-timedelta(days=1))

         elif self.Period.get()=='3 дня':
            self.Date2.set(date.today())
            self.Date1.set(date.today()-timedelta(days=3))
         elif self.Period.get()=='Неделя':
            self.Date2.set(date.today())
            self.Date1.set(date.today()-timedelta(days=7))
            print(self.Date1.get(), self.Date2.get())
         elif self.Period.get()=='Месяц':
            self.Date2.set(date.today())
            self.Date1.set(date.today()-timedelta(days=30))
         elif self.Period.get()=='Другой период':
            self.openCalendar()
            t1,t2=calendar_choice.toget(self)
            self.Date2.set(t1)
            self.Date1.set(t2)
         
         
   def frame_flats(self):
    
    for widget in self.fr_2.winfo_children():
         widget.destroy()
    self.lbl_char = Label(self.fr_2, text="Характеристики")
    self.lbl_char.grid(row=0, column=0, sticky="e")
    
    self.lbl_rooms = Label(self.fr_2, text="Кол-во комнат")
    self.lbl_rooms.grid(row=1, column=0, sticky="e")        
    self.ent_rooms_min = Entry(self.fr_2, width=10, textvariable=self.Rooms_min)
    self.ent_rooms_max = Entry(self.fr_2, width=10, textvariable=self.Rooms_max)
    self.ent_rooms_min.grid(row=1, column=1, sticky="w")
    self.ent_rooms_max.grid(row=1, column=2, sticky="e")
    
    self.lbl_floor = Label(self.fr_2, text="Этаж")
    self.ent_floor_min = Entry(self.fr_2, width=10, textvariable=self.Floor_min)
    self.ent_floor_max = Entry(self.fr_2, width=10, textvariable=self.Floor_max)
    self.lbl_floor.grid(row=2, column=0, sticky="e")
    self.ent_floor_min.grid(row=2, column=1, sticky="w")
    self.ent_floor_max.grid(row=2, column=2, sticky="e")


    self.lbl_floors = Label(self.fr_2, text="Этажность")
    self.ent_floors_min = Entry(self.fr_2, width=10, textvariable=self.Floors_min)
    self.ent_floors_max = Entry(self.fr_2, width=10, textvariable=self.Floors_max)
    self.lbl_floors.grid(row=3, column=0, sticky="e")
    self.ent_floors_min.grid(row=3, column=1, sticky="w")
    self.ent_floors_max.grid(row=3, column=2, sticky="e")

    plans = ["Улучшенная", "Обычная"]
    self.dropdown1 = OptionMenu(self.fr_2, self.Plan, *plans)
    self.dropdown1.grid(row=4,column=1, sticky="w")

    self.lbl_square = Label(self.fr_2, text="Площадь")
    self.ent_square_min = Entry(self.fr_2, width=10, textvariable=self.Square_min)
    self.ent_square_max = Entry(self.fr_2, width=10, textvariable=self.Square_max)    
    self.lbl_square.grid(row=5, column=0, sticky="e")
    self.ent_square_min.grid(row=5, column=1, sticky="w")
    self.ent_square_max.grid(row=5, column=2, sticky="e")
    
    self.lbl_price = Label(self.fr_2, text="Цена")
    self.ent_price_min = Entry(self.fr_2, width=10, textvariable=self.Price_min)
    self.ent_price_max = Entry(self.fr_2, width=10, textvariable=self.Price_max)    
    self.lbl_price.grid(row=6, column=0, sticky="e")
    self.ent_price_min.grid(row=6, column=1, sticky="w")
    self.ent_price_max.grid(row=6, column=2, sticky="e")

   def frame_house(self):
    
    for widget in self.fr_2.winfo_children():
         widget.destroy()
    self.lbl_char = Label(self.fr_2, text="Характеристики")
    self.lbl_char.grid(row=0, column=0, sticky="e")
    
    self.lbl_rooms = Label(self.fr_2, text="Кол-во комнат")
    self.lbl_rooms.grid(row=1, column=0, sticky="e")        
    self.ent_rooms_min = Entry(self.fr_2, width=10, textvariable=self.Rooms_min)
    self.ent_rooms_max = Entry(self.fr_2, width=10, textvariable=self.Rooms_max)
    self.ent_rooms_min.grid(row=1, column=1, sticky="w")
    self.ent_rooms_max.grid(row=1, column=2, sticky="e")

    self.lbl_floors = Label(self.fr_2, text="Этажность")
    self.ent_floors_min = Entry(self.fr_2, width=10, textvariable=self.Floors_min)
    self.ent_floors_max = Entry(self.fr_2, width=10, textvariable=self.Floors_max)
    self.lbl_floors.grid(row=2, column=0, sticky="e")
    self.ent_floors_min.grid(row=2, column=1, sticky="w")
    self.ent_floors_max.grid(row=2, column=2, sticky="e")

    self.lbl_square = Label(self.fr_2, text="Площадь")
    self.ent_square_min = Entry(self.fr_2, width=10, textvariable=self.Square_min)
    self.ent_square_max = Entry(self.fr_2, width=10, textvariable=self.Square_max)    
    self.lbl_square.grid(row=3, column=0, sticky="e")
    self.ent_square_min.grid(row=3, column=1, sticky="w")
    self.ent_square_max.grid(row=3, column=2, sticky="e")
    
    self.lbl_square_land = Label(self.fr_2, text="Площадь участка")
    self.ent_square_land_min = Entry(self.fr_2, width=10, textvariable=self.Square_land_min)
    self.ent_square_land_max = Entry(self.fr_2, width=10, textvariable=self.Square_land_max)    
    self.lbl_square_land.grid(row=4, column=0, sticky="e")
    self.ent_square_land_min.grid(row=4, column=1, sticky="w")
    self.ent_square_land_max.grid(row=4, column=2, sticky="e")
    
    self.lbl_price = Label(self.fr_2, text="Цена")
    self.ent_price_min = Entry(self.fr_2, width=10, textvariable=self.Price_min)
    self.ent_price_max = Entry(self.fr_2, width=10, textvariable=self.Price_max)    
    self.lbl_price.grid(row=5, column=0, sticky="e")
    self.ent_price_min.grid(row=5, column=1, sticky="w")
    self.ent_price_max.grid(row=5, column=2, sticky="e")

   def frame_gostinki(self):
    
    for widget in self.fr_2.winfo_children():
         widget.destroy()
    self.lbl_char = Label(self.fr_2, text="Характеристики")
    self.lbl_char.grid(row=0, column=0, sticky="e")
    
    self.lbl_rooms = Label(self.fr_2, text="Кол-во комнат")
    self.lbl_rooms.grid(row=1, column=0, sticky="e")        
    self.ent_rooms_min = Entry(self.fr_2, width=10, textvariable=self.Rooms_min)
    self.ent_rooms_max = Entry(self.fr_2, width=10, textvariable=self.Rooms_max)
    self.ent_rooms_min.grid(row=1, column=1, sticky="w")
    self.ent_rooms_max.grid(row=1, column=2, sticky="e")
    
    self.lbl_floor = Label(self.fr_2, text="Этаж")
    self.ent_floor_min = Entry(self.fr_2, width=10, textvariable=self.Floor_min)
    self.ent_floor_max = Entry(self.fr_2, width=10, textvariable=self.Floor_max)
    self.lbl_floor.grid(row=2, column=0, sticky="e")
    self.ent_floor_min.grid(row=2, column=1, sticky="w")
    self.ent_floor_max.grid(row=2, column=2, sticky="e")

    self.lbl_floors = Label(self.fr_2, text="Этажность")
    self.ent_floors_min = Entry(self.fr_2, width=10, textvariable=self.Floors_min)
    self.ent_floors_max = Entry(self.fr_2, width=10, textvariable=self.Floors_max)
    self.lbl_floors.grid(row=3, column=0, sticky="e")
    self.ent_floors_min.grid(row=3, column=1, sticky="w")
    self.ent_floors_max.grid(row=3, column=2, sticky="e")

    self.lbl_square = Label(self.fr_2, text="Площадь")
    self.ent_square_min = Entry(self.fr_2, width=10, textvariable=self.Square_min)
    self.ent_square_max = Entry(self.fr_2, width=10, textvariable=self.Square_max)    
    self.lbl_square.grid(row=4, column=0, sticky="e")
    self.ent_square_min.grid(row=4, column=1, sticky="w")
    self.ent_square_max.grid(row=4, column=2, sticky="e")
    
    self.lbl_price = Label(self.fr_2, text="Цена")
    self.ent_price_min = Entry(self.fr_2, width=10, textvariable=self.Price_min)
    self.ent_price_max = Entry(self.fr_2, width=10, textvariable=self.Price_max)    
    self.lbl_price.grid(row=5, column=0, sticky="e")
    self.ent_price_min.grid(row=5, column=1, sticky="w")
    self.ent_price_max.grid(row=5, column=2, sticky="e") 
   
   def search_stat(self):
   
      if not self.Rooms_min.get():
             self.Rooms_min.set(0)
      if not self.Rooms_max.get():
             self.Rooms_max.set(100)
      if not self.Floor_min.get():
             self.Floor_min.set(0)
      if not self.Floor_max.get():
             self.Floor_max.set(100)
      if not self.Floors_min.get():
             self.Floors_min.set(0)
      if not self.Floors_max.get():
             self.Floors_max.set(100)
      if not self.Square_min.get():
             self.Square_min.set(0.0)
      if not self.Square_max.get():
             self.Square_max.set(10000.0)
      if not self.Price_min.get():
             self.Price_min.set(0.0)
      if not self.Price_max.get():
             self.Price_max.set(1000000.0)
      if not self.Square_land_min.get():
             self.Square_land_min.set(0.0)
      if not self.Square_land_max.get():
             self.Square_land_max.set(100000.0)
      if not self.Date1.get():
             self.Date1.set('1970-01-01')
      if not self.Date2.get():
             self.Date2.set(date.today())
  
      

      f=open('_Obj_temp.txt', 'wb')
      f.close()
      name=''
      checkin = 1
      
      
      if self.TypeString.get()=='Квартира':
         name='Flats'
         checkin = 0
      elif self.TypeString.get()=='Дом':
         name='House'
         checkin = 0
      elif self.TypeString.get()=='Гостинка':
         name='Gostinki'
         checkin = 0
      
      city_check = 0
      street_check = 0
      district_check = 0
      date1=datetime.strptime(self.Date1.get(), '%Y-%m-%d').date()
      date2=datetime.strptime(self.Date2.get(), '%Y-%m-%d').date()
      if len(self.value_city)==0: city_check=1
      if len(self.value_street)==0: street_check=1
      if len(self.value_district)==0: district_check=1
      
      if checkin==0:   
         with open('_'+name+'_class.txt', 'rb') as output_file:
           while True:
            try:
               temp = pickle.load(output_file)
               index = 0
               i = 0
               for j in self.value_city:
                 if j==temp.city:
                    city_check=1
                    break
                 else: city_check=0
               for j1 in self.value_street:
                 if j1==temp.street:
                    street_check=1
                    break
                 else: street_check=0
               for j2 in self.value_district:
                 if j2==temp.district:
                    district_check=1
                    break
                 else: district_check=0
                  
                  
               if name=='Flats':  
                  if ( self.TypeString.get()==temp.types
                        and self.Rooms_min.get()<=int(temp.rooms)<=self.Rooms_max.get()
                        and self.Floor_min.get()<=int(temp.floor)<=self.Floor_max.get()
                        and self.Floors_min.get()<=int(temp.floors)<=self.Floors_max.get()
                        and self.Square_min.get()<=float(temp.square)<=self.Square_max.get()
                        and self.Price_min.get()<=float(temp.price)<=self.Price_max.get()
                        and (city_check==1) and (street_check==1) and (district_check==1)
                        and date1<=temp.add_date<=date2
                     ):
                     temp.pickle_search()
               elif name=='House':
                  if ( self.TypeString.get()==temp.types
                        and self.Rooms_min.get()<=int(temp.rooms)<=self.Rooms_max.get()
                       
                        and self.Floors_min.get()<=int(temp.floors)<=self.Floors_max.get()
                        and self.Square_min.get()<=float(temp.square)<=self.Square_max.get()
                        and self.Square_land_min.get()<=float(temp.land)<=self.Square_land_max.get()
                        and (city_check==1) and (street_check==1) and (district_check==1)
                        and date1<=temp.add_date<=date2
                       ):
                     temp.pickle_search()
               elif name=='Gostinki':
                  if ( self.TypeString.get()==temp.types
                        and self.Rooms_min.get()<=int(temp.rooms)<=self.Rooms_max.get()
                        and self.Floor_min.get()<=int(temp.floor)<=self.Floor_max.get()
                        and self.Floors_min.get()<=int(temp.floors)<=self.Floors_max.get()
                        and self.Square_min.get()<=float(temp.square)<=self.Square_max.get()
                        and self.Price_min.get()<=float(temp.price)<=self.Price_max.get()
                        and (city_check==1) and (street_check==1) and (district_check==1)
                        and date1<=temp.add_date<=date2
                       ):
                     temp.pickle_search()
                  
                
            except EOFError:
              break       
         self.report_search = child_report_search(self.slave, name, self.user)
         
      else:
         mb.showerror("Ошибка", "Должно быть чсло")
         
      self.slave.grab_set()
      self.slave.focus_set()
      self.slave.wait_window()
      return name    

    

   def openCalendar(self):
      calendar_choice(self.slave)  

      
   def end_stat(self):

       self.slave.destroy()
