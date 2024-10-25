import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from class_housing import *
import pandas as pd
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from datetime import *
import pickle
from boolean import *



class child_edit_house_info():
   def __init__(self, child_report_search, temp_):

    self.temp_=temp_
    global AdressCityString, TypesString, AdressStreetString, AdressHouseString, AdressHouse2String, AdressDistrictString, RoomsString
    global LandString, FloorsString, PartLandString, PriceString, SquareString, DateString, Text_infoString, IdString, AuthorString
    global ent_text_info, str_

    
     
    TypesString = tk.StringVar()  
    RoomsString = tk.IntVar()
    LandString = tk.DoubleVar()
    FloorsString = tk.IntVar()
    PartLandString = tk.DoubleVar()
    PriceString = tk.DoubleVar()
    SquareString = tk.DoubleVar()
    resultString = tk.StringVar()
    AdressString = tk.StringVar()
    AdressCityString = tk.StringVar()
    AdressStreetString = tk.StringVar()
    AdressHouseString = tk.IntVar()
    AdressHouse2String = tk.StringVar()
    AdressDistrictString = tk.StringVar()
    Text_infoString = tk.StringVar()
    DateString = tk.StringVar()
    IdString = tk.IntVar()
    AuthorString  = tk.StringVar()
      
    self.slave = Toplevel(child_report_search)
    self.slave.title('Ввод характеристик')
    self.slave.geometry('350x550+250+150')

    fr_1 = Frame(self.slave)
    fr_1.pack()

    fr_2 = Frame(self.slave)
    fr_2.pack()
    fr_but = Frame(self.slave)
    fr_but.pack()
    
    self.lbl_adress = Label(fr_1, text="Адрес")
    self.lbl_adress_city = Label(fr_1, text="Н.Пункт")
    self.lbl_adress_street = Label(fr_1, text="Улица")
    self.lbl_adress_house = Label(fr_1, text="Дом")
    self.lbl_adress_house2 = Label(fr_1, text="Корпус")
    self.lbl_adress_district = Label(fr_1, text="Район")
    self.ent_adress_house = Entry(fr_1, width=10, textvariable=AdressHouseString)
    self.ent_adress_house2 = Entry(fr_1, width=10, textvariable=AdressHouse2String)
    self.ent_adress_district = Entry(fr_1, width=10, textvariable=AdressDistrictString)
    self.lbl_adress.grid(row=0, column=0, sticky="w")
    self.lbl_adress_city.grid(row=1, column=0, sticky="w")
    self.lbl_adress_street.grid(row=2, column=0, sticky="w")
    self.lbl_adress_district.grid(row=3, column=0, sticky="w")

    AdressHouseString.set(self.temp_.num_house)
    RoomsString.set(self.temp_.rooms)
    LandString.set(self.temp_.land)
    PartLandString.set(self.temp_.part)
    FloorsString.set(self.temp_.floors)
    SquareString.set(self.temp_.square)
    PriceString.set(self.temp_.price)
    TypesString.set(self.temp_.types)
    DateString = date.today()
    IdString.set(self.temp_.id_object)
    AuthorString.set(self.temp_.author_object)
    
    values_city = [] 
    with open('_Cities.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_city.append(line.replace('\n', ''))
    combi_city = ttk.Combobox(fr_1, values=values_city, textvariable=AdressCityString)
    combi_city.grid(row=1, column=1, sticky="w")
    combi_city.set(temp_.city)
    
    values_street = [] 
    with open('_Streets.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_street.append(line.replace('\n', ''))
    combi_street = ttk.Combobox(fr_1, values=values_street, textvariable=AdressStreetString)
    combi_street.grid(row=2, column=1, sticky="w")
    combi_street.set(temp_.street)
    
    
    values_district = [] 
    with open('_Districts.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_district.append(line.replace('\n', ''))
    combi_district = ttk.Combobox(fr_1, values=values_district, textvariable=AdressDistrictString)
    combi_district.grid(row=3, column=1, sticky="w")
    combi_district.set(temp_.district)
    
    self.lbl_adress_house.grid(row=6, column=0, sticky="w")
    self.lbl_adress_house2.grid(row=7, column=0, sticky="w")
    self.ent_adress_house.grid(row=6, column=1, sticky="w")
    self.ent_adress_house2.grid(row=7, column=1, sticky="w")
    self.ent_adress_house2.insert(tk.END, temp_.num_kor)
    
          
    self.lbl_char = Label(fr_2, text="Характеристики")
    self.lbl_char.grid(row=0, column=0, sticky="e")
    
    self.lbl_rooms = Label(fr_2, text="Кол-во комнат")
    self.ent_rooms = Entry(fr_2, width=10, textvariable=RoomsString)
    self.lbl_rooms.grid(row=1, column=0, sticky="w")
    self.ent_rooms.grid(row=1, column=1, sticky="w")

    self.lbl_floors = Label(fr_2, text="Этажность")
    self.ent_floors = Entry(fr_2, width=10, textvariable=FloorsString)
    self.lbl_floors.grid(row=2, column=0, sticky="w")
    self.ent_floors.grid(row=2, column=1, sticky="w")
       
    self.lbl_square = Label(fr_2, text="Площадь")
    self.ent_square = Entry(fr_2, width=10, textvariable=SquareString)
    self.lbl_square.grid(row=3, column=0, sticky="w")
    self.ent_square.grid(row=3, column=1, sticky="w")
    self.lbl_square_land = Label(fr_2, text="Площадь участка")
    self.ent_square_land = Entry(fr_2, width=10, textvariable=LandString)
    self.lbl_square_land.grid(row=4, column=0, sticky="w")
    self.ent_square_land.grid(row=4, column=1, sticky="w")
    self.lbl_part_land = Label(fr_2, text="Часть домовладения")
    self.ent_part_land = Entry(fr_2, width=10, textvariable=PartLandString)
    self.lbl_part_land.grid(row=5, column=0, sticky="w")
    self.ent_part_land.grid(row=5, column=1, sticky="w")

    self.lbl_price = Label(fr_2, text="Цена")
    self.ent_price = Entry(fr_2, width=10, textvariable=PriceString)
    self.lbl_price.grid(row=6, column=0, sticky="w")
    self.ent_price.grid(row=6, column=1, sticky="w")
    
    self.lbl_text_info = Label(fr_2, text="Информация")
    ent_text_info = Text(fr_2, width=20, height=10)
    self.lbl_text_info.grid(row=7, column=0, sticky="e")
    ent_text_info.grid(row=7, column=1)
    ent_text_info.insert(1.0, temp_.text_info)
    str_=ent_text_info.get(1.0, END)
    Text_infoString.set(str_)

    #self.btn_photo = Button(fr_but, text="Добавить фото", command=self.photo_add)
    #self.btn_photo.grid(row=0, column=1, sticky='w')

    self.btn_save = Button(fr_but, text="Сохранить", command=self.edit_stat)
    self.btn_save.grid(row=1, column=1, sticky='w')
    
    #self.btn_cont = Button(fr_but, text="Далее", command=self.next_stat)
    #self.btn_cont.grid(row=2, column=1, sticky='w')
    
    self.btn_end = Button(fr_but, text="Завершить", command=self.end_stat)
    self.btn_end.grid(row=3, column=1, sticky='w')
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()


   def check(self):
        try:
            type(RoomsString.get())==int
            type(FloorsString.get())==int
            type(PriceString.get())==float
            type(SquareString.get())==float
            type(LandString.get())==float
            type(PartLandString.get())==float
            
            return 0
        except:
            mb.showerror("Ошибка", "Должно быть чсло")


   def photo_add(self):
       
       file_name = fd.askopenfilename()
       if (len(file_name))>0: 
           f = open(file_name)
   
   def edit_stat(self):
      self.dialog = yesno(self.slave)
      self.returnValue = self.dialog.go('question',
                                      'Изменить данные?')
      if self.returnValue:   
        str_=ent_text_info.get(1.0, END)
        Text_infoString.set(str_)
                   
        a = Houses(IdString.get(), AuthorString.get(), DateString, TypesString.get(),AdressCityString.get(),
                         AdressStreetString.get(), AdressDistrictString.get(),
                         AdressHouseString.get(), AdressHouse2String.get(), RoomsString.get(),
                         FloorsString.get(), SquareString.get(), LandString.get(),
                         PartLandString.get(), PriceString.get(), Text_infoString.get())
        
   
   def ret(self):
       a = Houses(IdString.get(), AuthorString.get(), DateString, TypesString.get(),AdressCityString.get(),
                         AdressStreetString.get(), AdressDistrictString.get(),
                         AdressHouseString.get(), AdressHouse2String.get(), RoomsString.get(),
                         FloorsString.get(), SquareString.get(), LandString.get(),
                         PartLandString.get(), PriceString.get(), Text_infoString.get())
       return a
       
   def end_stat(self):
   
       self.slave.destroy()
