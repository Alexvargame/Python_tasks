import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from class_housing import *
import pandas as pd
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from datetime import *
import pickle
import random


class child_ent_house():
   def __init__(self, child, user):


    self.user=user
    self.TypesString = tk.StringVar()  
    self.RoomsString = tk.IntVar()
    self.LandString = tk.DoubleVar()
    self.FloorsString = tk.IntVar()
    self.PartLandString = tk.DoubleVar()
    self.PriceString = tk.DoubleVar()
    self.SquareString = tk.DoubleVar()
    self.resultString = tk.StringVar()
    self.AdressString = tk.StringVar()
    self.AdressCityString = tk.StringVar()
    self.AdressStreetString = tk.StringVar()
    self.AdressHouseString = tk.IntVar()
    self.AdressHouse2String = tk.StringVar()
    self.AdressDistrictString = tk.StringVar()
    self.Text_infoString = tk.StringVar()
    self.DateString = tk.StringVar()
    self.IdString=tk.IntVar()
    self.AuthorString=tk.StringVar()
      
    self.slave = Toplevel(child)
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
    self.ent_adress_house = Entry(fr_1, width=10, textvariable=self.AdressHouseString)
    self.ent_adress_house2 = Entry(fr_1, width=10, textvariable=self.AdressHouse2String)
    self.ent_adress_district = Entry(fr_1, width=10, textvariable=self.AdressDistrictString)
    self.lbl_adress.grid(row=0, column=0, sticky="w")
    self.lbl_adress_city.grid(row=1, column=0, sticky="w")
    self.lbl_adress_street.grid(row=2, column=0, sticky="w")
    self.lbl_adress_district.grid(row=3, column=0, sticky="w")


    values_city = [] 
    with open('_Cities.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_city.append(line.replace('\n', ''))
    combi_city = ttk.Combobox(fr_1, values=values_city, textvariable=self.AdressCityString)
    combi_city.grid(row=1, column=1, sticky="w")
    
    values_street = [] 
    with open('_Streets.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_street.append(line.replace('\n', ''))
    combi_street = ttk.Combobox(fr_1, values=values_street, textvariable=self.AdressStreetString)
    combi_street.grid(row=2, column=1, sticky="w")
    
    values_district = [] 
    with open('_Districts.txt', 'r') as output_file:
       t = output_file.readlines()
       for line in t:
         if len(line)>1:
            values_district.append(line.replace('\n', ''))
    combi_district = ttk.Combobox(fr_1, values=values_district, textvariable=self.AdressDistrictString)
    combi_district.grid(row=3, column=1, sticky="w")
    
    self.lbl_adress_house.grid(row=6, column=0, sticky="w")
    self.lbl_adress_house2.grid(row=7, column=0, sticky="w")
    self.ent_adress_house.grid(row=6, column=1, sticky="w")
    self.ent_adress_house2.grid(row=7, column=1, sticky="w")

    

          
    self.lbl_char = Label(fr_2, text="Характеристики")
    self.lbl_char.grid(row=0, column=0, sticky="e")
    
    self.lbl_rooms = Label(fr_2, text="Кол-во комнат")
    self.ent_rooms = Entry(fr_2, width=10, textvariable=self.RoomsString)
    self.lbl_rooms.grid(row=1, column=0, sticky="w")
    self.ent_rooms.grid(row=1, column=1, sticky="w")

    self.lbl_floors = Label(fr_2, text="Этажность")
    self.ent_floors = Entry(fr_2, width=10, textvariable=self.FloorsString)
    self.lbl_floors.grid(row=2, column=0, sticky="w")
    self.ent_floors.grid(row=2, column=1, sticky="w")
       
    self.lbl_square = Label(fr_2, text="Площадь")
    self.ent_square = Entry(fr_2, width=10, textvariable=self.SquareString)
    self.lbl_square.grid(row=3, column=0, sticky="w")
    self.ent_square.grid(row=3, column=1, sticky="w")
    self.lbl_square_land = Label(fr_2, text="Площадь участка")
    self.ent_square_land = Entry(fr_2, width=10, textvariable=self.LandString)
    self.lbl_square_land.grid(row=4, column=0, sticky="w")
    self.ent_square_land.grid(row=4, column=1, sticky="w")
    self.lbl_part_land = Label(fr_2, text="Часть домовладения")
    self.ent_part_land = Entry(fr_2, width=10, textvariable=self.PartLandString)
    self.lbl_part_land.grid(row=5, column=0, sticky="w")
    self.ent_part_land.grid(row=5, column=1, sticky="w")

    self.lbl_price = Label(fr_2, text="Цена")
    self.ent_price = Entry(fr_2, width=10, textvariable=self.PriceString)
    self.lbl_price.grid(row=6, column=0, sticky="w")
    self.ent_price.grid(row=6, column=1, sticky="w")
    
    self.lbl_text_info = Label(fr_2, text="Информация")
    self.ent_text_info = Text(fr_2, width=20, height=10)
    self.lbl_text_info.grid(row=7, column=0, sticky="e")
    self.ent_text_info.grid(row=7, column=1)

    self.btn_photo = Button(fr_but, text="Добавить фото", command=self.photo_add)
    self.btn_photo.grid(row=0, column=1, sticky='w')

    self.btn_save = Button(fr_but, text="Сохранить", command=self.save_stat)
    self.btn_save.grid(row=1, column=1, sticky='w')
    
    self.btn_cont = Button(fr_but, text="Далее", command=self.next_stat)
    self.btn_cont.grid(row=2, column=1, sticky='w')
    
    self.btn_end = Button(fr_but, text="Завершить", command=self.end_stat)
    self.btn_end.grid(row=3, column=1, sticky='w')
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()


   def check(self):
        try:
            type(self.RoomsString.get())==int
            type(self.FloorsString.get())==int
            type(self.PriceString.get())==float
            type(self.SquareString.get())==float
            type(self.LandString.get())==float
            type(self.PartLandString.get())==float
            
            return 0
        except:
            mb.showerror("Ошибка", "Должно быть чсло")


   def photo_add(self):
       
       file_name = fd.askopenfilename()
       if (len(file_name))>0: 
           f = open(file_name)
   
   def save_stat(self):

      if self.check()==0:

        self.Text_infoString=self.ent_text_info.get(1.0, END)
        self.DateString = date.today()
        self.TypesString.set("Дом")
        self.IdString.set(random.randint(0,100000))
        self.AuthorString.set(str(random.randint(0,1000))+' '+self.user.id_user)


        self.AdressString.set("{}.{}.{}.{}.{}".format(self.AdressCityString.get(),
                         self.AdressStreetString.get(), self.AdressDistrictString.get(), 
                         self.AdressHouseString.get(), self.AdressHouse2String.get()))
        self.resultString.set("{},{},{},{},{},{},{},{},{},{},{},{}".format(self.IdString.get(), self.AuthorString.get(),
                         self.DateString, self.TypesString.get(), self.AdressString.get(), self.RoomsString.get(),
                         self.FloorsString.get(), self.SquareString.get(), self.LandString.get(),
                         self.PartLandString.get(), self.PriceString.get(), self.Text_infoString))
        with open('_Cities.txt', 'r+') as output_file:
           t = output_file.readlines()
           i=0
           for line in t:
              if line.lower()==self.AdressCityString.get().lower()+ '\n':
                 i=1
                 break
           if i==0:
              output_file.write(self.AdressCityString.get() + '\n')
            
        with open('_Streets.txt', 'r+') as output_file:
           t = output_file.readlines()
           i=0
           for line in t:
              if line.lower()==self.AdressStreetString.get().lower()+ '\n':
                 i=1
                 break
           if i==0:
              output_file.write(self.AdressStreetString.get() + '\n')
        with open('_Districts.txt', 'r+') as output_file:
           t = output_file.readlines()
           i=0
           for line in t:
              if line.lower()==self.AdressDistrictString.get().lower()+ '\n':
                 i=1
                 break
           if i==0:
              output_file.write(self.AdressDistrictString.get() + '\n')


      

        with open('_House.txt', 'a') as output_file:
           self.text = self.resultString.get()
           output_file.write(self.text)
           
        a = Houses(self.IdString.get(), self.AuthorString.get(),
                   date.today(), self.TypesString.get(),self.AdressCityString.get(),
                   self.AdressStreetString.get(), self.AdressDistrictString.get(), self.AdressHouseString.get(),
                   self.AdressHouse2String.get(), self.RoomsString.get(),
                   self.FloorsString.get(), self.SquareString.get(), self.LandString.get(),
                   self.PartLandString.get(), self.PriceString.get(), self.Text_infoString)
        a.pickle('_House_class.txt')
        del a
        with open('_House_class.txt', 'rb') as f:
           while True:
              try:
                 temp = pickle.load(f)
              except EOFError:
                 break

   def next_stat(self):
       self.RoomsString.set(0)
       self.LandString.set(0)
       self.FloorsString.set(0)
       self.PartLandString.set(0)
       self.PriceString.set(0)
       self.AdressCityString.set("")
       self.AdressStreetString.set("")
       self.AdressHouseString.set("")
       self.AdressHouse2String.set("")
       self.AdressDistrictString.set("")
       self.ent_text_info.delete(1.0, END)
       self.IdString.set(0)
       self.AuthorString.set("")

       
   def end_stat(self):
   
       self.slave.destroy()
