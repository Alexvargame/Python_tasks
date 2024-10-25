from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import xlsxwriter
import pandas
import pickle
import os
import shutil
from boolean import *
from Edit_flat_info import *
from Edit_info_house import *
from Edit_info_gost import *



class child_report_search:
   def __init__(self, child_search, name, user):
    #super().__init__(self)
       self.slave = Toplevel(child_search)
       self.slave.title('Отчет')
       self.slave.geometry('1000x450+200+200')
       self.name = name
       self.user=user
       self.frm_label = Frame(self.slave, relief=tk.SUNKEN, borderwidth=3)
       self.frm_label.pack(fill=tk.X, ipadx=5, ipady=5)
       self.frm_entry = Frame(self.slave)
       self.frm_entry.pack(side=tk.LEFT, fill=tk.Y, ipadx=5, ipady=5)
       self.frm_text = Frame(self.slave)
       self.frm_text.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5, ipady=5)
       self.frm_edit = Frame(self.slave)
       self.frm_edit.pack(side=tk.BOTTOM, fill=tk.BOTH, ipadx=5, ipady=5)
       

       if name=='Flats':
          self.show_flats(name)       
       elif name=='House':
          self.show_house(name)
       elif name=='Gostinki':
          self.show_gostinki(name)
       elif name=='my_object':
          self.show_my_object(name)

   def show_flats(self, name):
   
       self.lbl_empty = tk.Label(master=self.frm_label, text="   ", width=10)
       self.lbl_empty.grid(row=0, column=0)
       self.lbl_city = tk.Label(master=self.frm_label, text="Город", width=10)
       self.lbl_city.grid(row=0, column=2)
       self.lbl_street = tk.Label(master=self.frm_label, text="Улица", width=8)
       self.lbl_street.grid(row=0, column=3)
       self.lbl_district = tk.Label(master=self.frm_label, text="Район", width=8)
       self.lbl_district.grid(row=0, column=4)
       self.lbl_house_appart = tk.Label(master=self.frm_label, text="№дом/кв", width=8)
       self.lbl_house_appart.grid(row=0, column=5)
       self.lbl_rooms = tk.Label(master=self.frm_label, text="Кол-во\nкомнат", width=8)
       self.lbl_rooms.grid(row=0, column=6, sticky="w")
       self.lbl_floor = tk.Label(master=self.frm_label, text="Этаж", width=8)
       self.lbl_floor.grid(row=0, column=7, sticky="w")
       self.lbl_floors = tk.Label(master=self.frm_label, text="Эт-ть", width=8)
       self.lbl_floors.grid(row=0, column=8, sticky="w")
       self.lbl_square = tk.Label(master=self.frm_label, text="Площадь", width=8)
       self.lbl_square.grid(row=0, column=9, sticky="w")
       self.lbl_plan = tk.Label(master=self.frm_label, text="План-ка", width=8)
       self.lbl_plan.grid(row=0, column=10, sticky=tk.E)
       self.lbl_price = tk.Label(master=self.frm_label, text="Цена", width=8)
       self.lbl_price.grid(row=0, column=11, sticky=tk.E)
       self.lbl_date = tk.Label(master=self.frm_label, text="Дата", width=8)
       self.lbl_date.grid(row=0, column=12, sticky=tk.E)
       
       with open('_Obj_temp.txt', 'rb') as output_file:
 
         i=0
         while True:
            try:
               temp = pickle.load(output_file)
               self.btn_info = tk.Button(master=self.frm_entry, text="I")
               self.btn_info.bind("<Button-1>", self.info_to_window)
               self.btn_edit = tk.Button(master=self.frm_entry, text="Edit")
               self.btn_edit.bind("<Button-1>", self.edit_)
               self.btn_del = tk.Button(master=self.frm_entry, text="Del")
               self.btn_del.bind("<Button-1>", self.del_)
               self.ent_city = tk.Entry(master=self.frm_entry, width=10)
               self.ent_city.insert(tk.END, temp.city)
               self.ent_street = tk.Entry(master=self.frm_entry, width=10)
               self.ent_street.insert(tk.END, temp.street)
               self.ent_district = tk.Entry(master=self.frm_entry, width=10)
               self.ent_district.insert(tk.END, temp.district)
               self.ent_house_appart = tk.Entry(master=self.frm_entry, width=10)
               self.ent_house_appart.insert(tk.END, 'Дом'+str(temp.num_house)+' Корп'+str(temp.num_kor))  
               self.ent_rooms = tk.Entry(master=self.frm_entry, width=10)
               self.ent_rooms.insert(tk.END, temp.rooms)  
               self.ent_floor = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floor.insert(tk.END,temp.floor )  
               self.ent_floors = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floors.insert(tk.END, temp.floors)
               self.ent_square = tk.Entry(master=self.frm_entry, width=10)
               self.ent_square.insert(tk.END, temp.square)
               self.ent_plan = tk.Entry(master=self.frm_entry, width=10)
               self.ent_plan.insert(tk.END, temp.plan)
               self.ent_price = tk.Entry(master=self.frm_entry, width=10)
               self.ent_price.insert(tk.END, temp.price)
               self.ent_date = tk.Entry(master=self.frm_entry, width=10)
               self.ent_date.insert(tk.END, temp.add_date)
               
               self.btn_info.grid(row=i, column=0, sticky=tk.E)
               self.btn_edit.grid(row=i, column=1, sticky=tk.E)
               self.btn_del.grid(row=i, column=2, sticky=tk.E)
               self.ent_city.grid(row=i, column=3, sticky=tk.E)
               self.ent_street.grid(row=i, column=4, sticky=tk.E)
               self.ent_district.grid(row=i, column=5, sticky=tk.E)
               self.ent_house_appart.grid(row=i, column=6, sticky=tk.E)
               self.ent_rooms.grid(row=i, column=7, sticky=tk.E)
               self.ent_floor.grid(row=i, column=8, sticky=tk.E)
               self.ent_floors.grid(row=i, column=9, sticky=tk.E)
               self.ent_square.grid(row=i, column=10, sticky=tk.E)
               self.ent_plan.grid(row=i, column=11, sticky=tk.E)
               self.ent_price.grid(row=i, column=12, sticky=tk.E)
               self.ent_date.grid(row=i, column=13, sticky=tk.E)
               
               i=i+1
            except EOFError:
               break
         self.btn_excel = tk.Button(master=self.frm_entry, text="Отчет в Excel", command=self.info_to_excel(name))
         self.btn_excel.grid(row=i+2, column=1, columnspan=3, sticky='w')
         self.btn_end = tk.Button(master=self.frm_entry, text="Завершить", command=self.end_stat)
         self.btn_end.grid(row=i+2, column=10, sticky='w')

      
   def show_house(self, name):
       
       self.lbl_empty = tk.Label(master=self.frm_label, text="", width=10)
       self.lbl_empty.grid(row=0, column=0, sticky="w")
       self.lbl_city = tk.Label(master=self.frm_label, text="Город", width=8)
       self.lbl_city.grid(row=0, column=2, sticky="w")
       self.lbl_street = tk.Label(master=self.frm_label, text="Улица", width=8)
       self.lbl_street.grid(row=0, column=3, sticky="w")
       self.lbl_district = tk.Label(master=self.frm_label, text="Район", width=8)
       self.lbl_district.grid(row=0, column=4, sticky="w")
       self.lbl_house_appart = tk.Label(master=self.frm_label, text="№дом", width=8)
       self.lbl_house_appart.grid(row=0, column=5, sticky="w")
       self.lbl_rooms = tk.Label(master=self.frm_label, text="Кол-во комнат", width=8)
       self.lbl_rooms.grid(row=0, column=6, sticky="w")
       self.lbl_part = tk.Label(master=self.frm_label, text="Часть", width=8)
       self.lbl_part.grid(row=0, column=8, sticky="w")
       self.lbl_floors = tk.Label(master=self.frm_label, text="Этажность", width=10)
       self.lbl_floors.grid(row=0, column=7, sticky="w")
       self.lbl_square = tk.Label(master=self.frm_label, text="Площадь", width=10)
       self.lbl_square.grid(row=0, column=9, sticky="w")
       self.lbl_land = tk.Label(master=self.frm_label, text="Участок", width=8)
       self.lbl_land.grid(row=0, column=10, sticky=tk.E)
       self.lbl_price = tk.Label(master=self.frm_label, text="Цена", width=8)
       self.lbl_price.grid(row=0, column=11, sticky=tk.E)
       self.lbl_date = tk.Label(master=self.frm_label, text="Дата", width=8)
       self.lbl_date.grid(row=0, column=12, sticky=tk.E)
       
       with open('_Obj_temp.txt', 'rb') as output_file:
 
         i=0
         while True:
            try:
               temp = pickle.load(output_file)
               self.btn_info = tk.Button(master=self.frm_entry, text="I")
               self.btn_info.bind("<Button-1>", self.info_to_window)
               self.btn_edit = tk.Button(master=self.frm_entry, text="Edit")
               self.btn_edit.bind("<Button-1>", self.edit_)
               self.btn_del = tk.Button(master=self.frm_entry, text="Del")
               self.btn_del.bind("<Button-1>", self.del_)
               self.ent_city = tk.Entry(master=self.frm_entry, width=10)
               self.ent_city.insert(tk.END, temp.city)
               self.ent_street = tk.Entry(master=self.frm_entry, width=10)
               self.ent_street.insert(tk.END, temp.street)
               self.ent_district = tk.Entry(master=self.frm_entry, width=10)
               self.ent_district.insert(tk.END, temp.district)
               self.ent_house_appart = tk.Entry(master=self.frm_entry, width=10)
               self.ent_house_appart.insert(tk.END, 'Дом'+str(temp.num_house)+' Корп'+str(temp.num_kor))  
               self.ent_rooms = tk.Entry(master=self.frm_entry, width=10)
               self.ent_rooms.insert(tk.END, temp.rooms)  
               self.ent_part = tk.Entry(master=self.frm_entry, width=10)
               self.ent_part.insert(tk.END,temp.part)  
               self.ent_floors = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floors.insert(tk.END, temp.floors)
               self.ent_square = tk.Entry(master=self.frm_entry, width=10)
               self.ent_square.insert(tk.END, temp.square)
               self.ent_land = tk.Entry(master=self.frm_entry, width=10)
               self.ent_land.insert(tk.END, temp.land)  
               self.ent_price = tk.Entry(master=self.frm_entry, width=10)
               self.ent_price.insert(tk.END, temp.price)
               self.ent_date = tk.Entry(master=self.frm_entry, width=10)
               self.ent_date.insert(tk.END, temp.add_date)
               
               self.btn_info.grid(row=i, column=0, sticky=tk.E)
               self.btn_edit.grid(row=i, column=1, sticky=tk.E)
               self.btn_del.grid(row=i, column=2, sticky=tk.E)
               self.ent_city.grid(row=i, column=3, sticky=tk.E)
               self.ent_street.grid(row=i, column=4, sticky=tk.E)
               self.ent_district.grid(row=i, column=5, sticky=tk.E)
               self.ent_house_appart.grid(row=i, column=6, sticky=tk.E)
               self.ent_rooms.grid(row=i, column=7, sticky=tk.E)
               self.ent_floors.grid(row=i, column=8, sticky=tk.E)
               self.ent_part.grid(row=i, column=9, sticky=tk.E)
               self.ent_square.grid(row=i, column=10, sticky=tk.E)
               self.ent_land.grid(row=i, column=11, sticky=tk.E)
               self.ent_price.grid(row=i, column=12, sticky=tk.E)
               self.ent_date.grid(row=i, column=13, sticky=tk.E)
               i=i+1
            except EOFError:
               break
         self.btn_excel = tk.Button(master=self.frm_entry, text="Отчет в Excel", command=self.info_to_excel(name))
         self.btn_excel.grid(row=i+2, column=1, columnspan=3, sticky='w')
         self.btn_end = tk.Button(master=self.frm_entry, text="Завершить", command=self.end_stat)
         self.btn_end.grid(row=i+2, column=10, sticky='w')
         
   def show_gostinki(self, name):

       self.lbl_empty = tk.Label(master=self.frm_label, text="", width=10)
       self.lbl_empty.grid(row=0, column=0, sticky="w")
       self.lbl_city = tk.Label(master=self.frm_label, text="Город", width=8)
       self.lbl_city.grid(row=0, column=2, sticky="w")
       self.lbl_street = tk.Label(master=self.frm_label, text="Улица", width=8)
       self.lbl_street.grid(row=0, column=3, sticky="w")
       self.lbl_district = tk.Label(master=self.frm_label, text="Район", width=8)
       self.lbl_district.grid(row=0, column=4, sticky="w")
       self.lbl_house_appart = tk.Label(master=self.frm_label, text="№дом/кв", width=8)
       self.lbl_house_appart.grid(row=0, column=5, sticky="w")
       self.lbl_rooms = tk.Label(master=self.frm_label, text="Кол-во комнат", width=8)
       self.lbl_rooms.grid(row=0, column=6, sticky="w")
       self.lbl_floor = tk.Label(master=self.frm_label, text="Этаж", width=8)
       self.lbl_floor.grid(row=0, column=7, sticky="w")
       self.lbl_floors = tk.Label(master=self.frm_label, text="Этажность", width=8)
       self.lbl_floors.grid(row=0, column=8, sticky="w")
       self.lbl_square = tk.Label(master=self.frm_label, text="Площадь", width=8)
       self.lbl_square.grid(row=0, column=9, sticky="w")
       self.lbl_price = tk.Label(master=self.frm_label, text="Цена", width=8)
       self.lbl_price.grid(row=0, column=10, sticky=tk.E)
       self.lbl_date = tk.Label(master=self.frm_label, text="Дата", width=8)
       self.lbl_date.grid(row=0, column=11, sticky=tk.E)
       
       with open('_Obj_temp.txt', 'rb') as output_file:
 
         i=0
         while True:
            try:
               temp = pickle.load(output_file)
               self.btn_info = tk.Button(master=self.frm_entry, text="I")
               self.btn_info.bind("<Button-1>", self.info_to_window)
               self.btn_edit = tk.Button(master=self.frm_entry, text="Edit")
               self.btn_edit.bind("<Button-1>", self.edit_)
               self.btn_del = tk.Button(master=self.frm_entry, text="Del")
               self.btn_del.bind("<Button-1>", self.del_)
               self.ent_city = tk.Entry(master=self.frm_entry, width=10)
               self.ent_city.insert(tk.END, temp.city)
               self.ent_street = tk.Entry(master=self.frm_entry, width=10)
               self.ent_street.insert(tk.END, temp.street)
               self.ent_district = tk.Entry(master=self.frm_entry, width=10)
               self.ent_district.insert(tk.END, temp.district)
               self.ent_house_appart = tk.Entry(master=self.frm_entry, width=10)
               self.ent_house_appart.insert(tk.END, 'Дом'+str(temp.num_house)+' Корп'+str(temp.num_kor))  
               self.ent_rooms = tk.Entry(master=self.frm_entry, width=10)
               self.ent_rooms.insert(tk.END, temp.rooms)  
               self.ent_floor = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floor.insert(tk.END,temp.floor )  
               self.ent_floors = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floors.insert(tk.END, temp.floors)
               self.ent_square = tk.Entry(master=self.frm_entry, width=10)
               self.ent_price = tk.Entry(master=self.frm_entry, width=10)
               self.ent_price.insert(tk.END, temp.price)
               self.ent_date = tk.Entry(master=self.frm_entry, width=10)
               self.ent_date.insert(tk.END, temp.add_date)
               
               self.btn_info.grid(row=i, column=0, sticky=tk.E)
               self.btn_edit.grid(row=i, column=1, sticky=tk.E)
               self.btn_del.grid(row=i, column=2, sticky=tk.E)
               self.ent_city.grid(row=i, column=3, sticky=tk.E)
               self.ent_street.grid(row=i, column=4, sticky=tk.E)
               self.ent_district.grid(row=i, column=5, sticky=tk.E)
               self.ent_house_appart.grid(row=i, column=6, sticky=tk.E)
               self.ent_rooms.grid(row=i, column=7, sticky=tk.E)
               self.ent_floor.grid(row=i, column=8, sticky=tk.E)
               self.ent_floors.grid(row=i, column=9, sticky=tk.E)
               self.ent_square.grid(row=i, column=10, sticky=tk.E)
               self.ent_price.grid(row=i, column=11, sticky=tk.E)
               self.ent_date.grid(row=i, column=12, sticky=tk.E)
               i=i+1
            except EOFError:
               break
         self.btn_excel = tk.Button(master=self.frm_entry, text="Отчет в Excel", command=self.info_to_excel(name))
         self.btn_excel.grid(row=i+2, column=1, columnspan=3, sticky='w')
         self.btn_end = tk.Button(master=self.frm_entry, text="Завершить", command=self.end_stat)
         self.btn_end.grid(row=i+2, column=10, sticky='w')

       self.slave.grab_set()
       self.slave.focus_set()
       self.slave.wait_window()

   def end_stat(self):

       self.slave.destroy() 
    

               
   def info_to_window (self, event):
     
      grid_info = event.widget.grid_info()
      #print("row:", grid_info["row"], "column:",
          #grid_info["column"])
    
      for widget in self.frm_text.winfo_children():
            widget.destroy()
            
      
      self.txt_info = tk.Text(master=self.frm_text, width=20)
      self.txt_info.grid(row=0, column=0, sticky=tk.E)
      self.txt_info.delete(1.0, END)
      
      with open('_Obj_temp.txt', 'rb') as output_file:
           
          i=0

          while True:
             try:
               
                temp=pickle.load(output_file)
                if i==grid_info["row"]:
                     self.txt_info.insert(1.0, temp.text_info) 
                     del temp
                     break
                i=i+1
             except EOFError:
                break     
      self.slave.update_idletasks()
   def del_ (self, event):
      f=open('_Obj_temp_del.txt', 'wb')
      f.close()
     
      self.dialog = yesno(self.slave)
      self.returnValue = self.dialog.go('question',
                                      'Вы хотите удалить данные?')
      if self.returnValue:   
         grid_info = event.widget.grid_info()
         with open('_Obj_temp.txt', 'rb') as output_file:       
             i=0
             while True:
                try:               
                   temp=pickle.load(output_file)
                   if i==grid_info["row"]:
                         with open('_'+self.name+'_class.txt', 'rb') as output_file1:
                            j=0
                            while True:
                               try:
                                  temp1=pickle.load(output_file1)
                                  if not temp.compare(temp1):
                                     with open('_Obj_temp_del.txt', 'rb') as output_file2:
                                        temp1.pickle('_Obj_temp_del.txt')
                                        del temp1
                                  j=j+1
                               except EOFError:
                                  break                           
                         del temp
                         break
                   i=i+1
                except EOFError:
                   break
      file_oldname = os.path.join("C:\Python36-32\Flat", "_Obj_temp_del.txt")
      str='_'+self.name+'_class.txt'
      file_newname = os.path.join("C:\Python36-32\Flat", str)
      shutil.move(file_oldname, file_newname)
         #self.slave.update_idletasks()
   def del_my_object (self, event):
      f=open('_Obj_temp_del.txt', 'wb')
      f.close()
     
      self.dialog = yesno(self.slave)
      self.returnValue = self.dialog.go('question',
                                      'Вы хотите удалить данные?')
      if self.returnValue:
         
         grid_info = event.widget.grid_info()
         with open('_Obj_temp.txt', 'rb') as output_file:       
             i=0
             while True:
                try:               
                   temp=pickle.load(output_file)
                   if temp.types=='Квартира': t='Flats'
                   elif temp.types=='Дом': t='House'
                   elif temp.types=='Гостинка': t='Gostinki'
                   if i==grid_info["row"]:
                         with open('_'+t+'_class.txt', 'rb') as output_file1:
                            j=0
                            while True:
                               try:
                                  temp1=pickle.load(output_file1)
                                  if not temp.compare(temp1):
                                     with open('_Obj_temp_del.txt', 'rb') as output_file2:
                                        temp1.pickle('_Obj_temp_del.txt')
                                        del temp1
                                  j=j+1
                               except EOFError:
                                  break                           
                         del temp
                         break
                   i=i+1
                except EOFError:
                   break
      file_oldname = os.path.join("C:\Python36-32\Flat", "_Obj_temp_del.txt")
      str='_'+t+'_class.txt'
      file_newname = os.path.join("C:\Python36-32\Flat", str)
      shutil.move(file_oldname, file_newname)
   def edit_ (self, event):
      f=open('_Obj_temp_del.txt', 'wb')
      f.close()
      grid_info = event.widget.grid_info()
      with open('_Obj_temp.txt', 'rb') as output_file:       
             i=0
             while True:
                try:               
                   temp=pickle.load(output_file)
                   if i==grid_info["row"]:
                         with open('_'+self.name+'_class.txt', 'rb') as output_file1:
                            j=0
                            while True:
                               try:
                                  temp1=pickle.load(output_file1)
                                  with open('_Obj_temp_del.txt', 'rb') as output_file2:
                                     if temp.compare(temp1):
                                        if (self.name == 'Flats'):
                                           
                                             self.edit_flat_info=child_edit_flat_info(self.slave, temp1)
                                             child_edit_flat_info.ret(self).assign(temp1)
                                            
                                           
                                             temp1.pickle('_Obj_temp_del.txt')
                                             del temp1
                                             
                                        elif (self.name == 'House'):
                                             
                                             self.edit_house_info=child_edit_house_info(self.slave, temp1)
                                            
                                             child_edit_house_info.ret(self).assign(temp1)
                                            
                                             temp1.pickle('_Obj_temp_del.txt')
                                             del temp1
                                           
                                        elif(self.name == 'Gostinki'):
                                             
                                             self.edit_gost_info=child_edit_gost_info(self.slave, temp1)
                                             
                                             child_edit_gost_info.ret(self).assign(temp1)
                                             
                                             temp1.pickle('_Obj_temp_del.txt')
                                             del temp1

                                     else:
                                         temp1.pickle('_Obj_temp_del.txt')
                                         del temp1
                                          

                                  j=j+1
                               except EOFError:
                                  break
                                  
                         del temp
                         break
                   i=i+1
                except EOFError:
                   break
   
      file_oldname = os.path.join("C:\Python36-32\Flat", "_Obj_temp_del.txt")
      str='_'+self.name+'_class.txt'
      file_newname = os.path.join("C:\Python36-32\Flat", str)
      shutil.move(file_oldname, file_newname)

      #self.slave.update_idletasks()
   def edit_my_object (self, event):
      f=open('_Obj_temp_del.txt', 'wb')
      f.close()
      grid_info = event.widget.grid_info()
      with open('_Obj_temp.txt', 'rb') as output_file:       
             i=0
             while True:
                try:               
                   temp=pickle.load(output_file)
                   if temp.types=='Квартира': t='Flats'
                   elif temp.types=='Дом': t='House'
                   elif temp.types=='Гостинка': t='Gostinki'
                   if i==grid_info["row"]:
                         with open('_'+t+'_class.txt', 'rb') as output_file1:
                            j=0
                            while True:
                               try:
                                  temp1=pickle.load(output_file1)
                                  with open('_Obj_temp_del.txt', 'rb') as output_file2:
                                     if temp.compare(temp1):
                                        if (t == 'Flats'):
                                           
                                             self.edit_flat_info=child_edit_flat_info(self.slave, temp1)
                                             child_edit_flat_info.ret(self).assign(temp1)
                                            
                                           
                                             temp1.pickle('_Obj_temp_del.txt')
                                             del temp1
                                             
                                        elif (t == 'House'):
                                             
                                             self.edit_house_info=child_edit_house_info(self.slave, temp1)
                                            
                                             child_edit_house_info.ret(self).assign(temp1)
                                            
                                             temp1.pickle('_Obj_temp_del.txt')
                                             del temp1
                                           
                                        elif(t == 'Gostinki'):
                                             
                                             self.edit_gost_info=child_edit_gost_info(self.slave, temp1)
                                             
                                             child_edit_gost_info.ret(self).assign(temp1)
                                             
                                             temp1.pickle('_Obj_temp_del.txt')
                                             del temp1

                                     else:
                                         temp1.pickle('_Obj_temp_del.txt')
                                         del temp1
                                          

                                  j=j+1
                               except EOFError:
                                  break
                                  
                         del temp
                         break
                   i=i+1
                except EOFError:
                   break
   
      file_oldname = os.path.join("C:\Python36-32\Flat", "_Obj_temp_del.txt")
      str='_'+t+'_class.txt'
      file_newname = os.path.join("C:\Python36-32\Flat", str)
      shutil.move(file_oldname, file_newname)

      #self.slave.update_idletasks()
   def show_my_object(self, name):
       
       self.lbl_empty = tk.Label(master=self.frm_label, text="", width=10)
       self.lbl_empty.grid(row=0, column=0, sticky="w")
       self.lbl_empty = tk.Label(master=self.frm_label, text="Тип надв.", width=10)
       self.lbl_empty.grid(row=0, column=1, sticky="w")
       self.lbl_city = tk.Label(master=self.frm_label, text="Город", width=8)
       self.lbl_city.grid(row=0, column=2, sticky="w")
       self.lbl_street = tk.Label(master=self.frm_label, text="Улица", width=8)
       self.lbl_street.grid(row=0, column=3, sticky="w")
       self.lbl_district = tk.Label(master=self.frm_label, text="Район", width=8)
       self.lbl_district.grid(row=0, column=4, sticky="w")
       self.lbl_house_appart = tk.Label(master=self.frm_label, text="№дом", width=8)
       self.lbl_house_appart.grid(row=0, column=5, sticky="w")
       self.lbl_rooms = tk.Label(master=self.frm_label, text="Кол-во комнат", width=8)
       self.lbl_rooms.grid(row=0, column=6, sticky="w")
       self.lbl_part = tk.Label(master=self.frm_label, text="Часть", width=8)
       self.lbl_part.grid(row=0, column=11, sticky="w")
       self.lbl_floor = tk.Label(master=self.frm_label, text="Этаж", width=8)
       self.lbl_floor.grid(row=0, column=7, sticky="w")
       self.lbl_floors = tk.Label(master=self.frm_label, text="Этажность", width=10)
       self.lbl_floors.grid(row=0, column=8, sticky="w")
       self.lbl_plan = tk.Label(master=self.frm_label, text="План-ка", width=8)
       self.lbl_plan.grid(row=0, column=9, sticky=tk.E)
       self.lbl_square = tk.Label(master=self.frm_label, text="Площадь", width=10)
       self.lbl_square.grid(row=0, column=10, sticky="w")
       self.lbl_land = tk.Label(master=self.frm_label, text="Участок", width=8)
       self.lbl_land.grid(row=0, column=12, sticky=tk.E)
       self.lbl_price = tk.Label(master=self.frm_label, text="Цена", width=8)
       self.lbl_price.grid(row=0, column=13, sticky=tk.E)
       self.lbl_date = tk.Label(master=self.frm_label, text="Дата", width=8)
       self.lbl_date.grid(row=0, column=14, sticky=tk.E)
       
       with open('_Obj_temp.txt', 'rb') as output_file:
 
         i=0
         while True:
            try:
               temp = pickle.load(output_file)
               self.btn_info = tk.Button(master=self.frm_entry, text="I")
               self.btn_info.bind("<Button-1>", self.info_to_window)
               self.btn_edit = tk.Button(master=self.frm_entry, text="Edit")
               self.btn_edit.bind("<Button-1>", self.edit_my_object)
               self.btn_del = tk.Button(master=self.frm_entry, text="Del")
               self.btn_del.bind("<Button-1>", self.del_my_object)
               self.ent_type = tk.Entry(master=self.frm_entry, width=10)
               self.ent_type.insert(tk.END, temp.types)
               self.ent_city = tk.Entry(master=self.frm_entry, width=10)
               self.ent_city.insert(tk.END, temp.city)
               self.ent_street = tk.Entry(master=self.frm_entry, width=10)
               self.ent_street.insert(tk.END, temp.street)
               self.ent_district = tk.Entry(master=self.frm_entry, width=10)
               self.ent_district.insert(tk.END, temp.district)
               self.ent_house_appart = tk.Entry(master=self.frm_entry, width=10)
               self.ent_house_appart.insert(tk.END, 'Дом'+str(temp.num_house)+' Корп'+str(temp.num_kor))  
               self.ent_rooms = tk.Entry(master=self.frm_entry, width=10)
               self.ent_rooms.insert(tk.END, temp.rooms)  
               self.ent_part = tk.Entry(master=self.frm_entry, width=10)
               if temp.types=='House':
                  self.ent_part.insert(tk.END,temp.part)  
               self.ent_floors = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floors.insert(tk.END, temp.floors)

               self.ent_floor = tk.Entry(master=self.frm_entry, width=10)
               if temp.types=='Flats' or temp.types=='Gostinki':
                  self.ent_floor.insert(tk.END,temp.floor )  
               self.ent_plan = tk.Entry(master=self.frm_entry, width=10)
               if temp.types=='Flats':
                  self.ent_plan.insert(tk.END, temp.plan)
               
               self.ent_square = tk.Entry(master=self.frm_entry, width=10)
               self.ent_square.insert(tk.END, temp.square)
               self.ent_land = tk.Entry(master=self.frm_entry, width=10)
               if temp.types=='House':
                  self.ent_land.insert(tk.END, temp.land)  
               self.ent_price = tk.Entry(master=self.frm_entry, width=10)
               self.ent_price.insert(tk.END, temp.price)
               self.ent_date = tk.Entry(master=self.frm_entry, width=10)
               self.ent_date.insert(tk.END, temp.add_date)
               
               self.btn_info.grid(row=i, column=0, sticky=tk.E)
               self.btn_edit.grid(row=i, column=1, sticky=tk.E)
               self.btn_del.grid(row=i, column=2, sticky=tk.E)
               self.ent_type.grid(row=i, column=3, sticky=tk.E)
               self.ent_city.grid(row=i, column=4, sticky=tk.E)
               self.ent_street.grid(row=i, column=5, sticky=tk.E)
               self.ent_district.grid(row=i, column=6, sticky=tk.E)
               self.ent_house_appart.grid(row=i, column=7, sticky=tk.E)
               self.ent_rooms.grid(row=i, column=8, sticky=tk.E)
               self.ent_floor.grid(row=i, column=9, sticky=tk.E)
               self.ent_floors.grid(row=i, column=10, sticky=tk.E)
               self.ent_plan.grid(row=i, column=11, sticky=tk.E)
               self.ent_square.grid(row=i, column=12, sticky=tk.E)
               self.ent_part.grid(row=i, column=13, sticky=tk.E)            
               self.ent_land.grid(row=i, column=14, sticky=tk.E)
               self.ent_price.grid(row=i, column=15, sticky=tk.E)
               self.ent_date.grid(row=i, column=16, sticky=tk.E)
               i=i+1
            except EOFError:
               break
         self.btn_excel = tk.Button(master=self.frm_entry, text="Отчет в Excel", command=self.info_to_excel(name))
         self.btn_excel.grid(row=i+2, column=1, columnspan=3, sticky='w')
         self.btn_end = tk.Button(master=self.frm_entry, text="Завершить", command=self.end_stat)
         self.btn_end.grid(row=i+2, column=10, sticky='w')    
      
   def info_to_excel(self, name):
      
    if name=='Flats':
      
      workbook = xlsxwriter.Workbook('2.xlsx')
      worksheet = workbook.add_worksheet()
      bold = workbook.add_format({'bold': True})
      date_format = workbook.add_format({'num_format': 'yy-mm-dd'}) 
      worksheet.write('A1', 'Дата', bold)
      worksheet.write('B1', 'ID', bold)
      worksheet.write('C1', 'Автор', bold)
      worksheet.write('D1', 'Наименование', bold)
      worksheet.write('E1', 'Город', bold)
      worksheet.write('F1', 'Улица', bold)
      worksheet.write('G1', 'Район', bold)
      worksheet.write('H1', 'Дом', bold)
      worksheet.write('I1', 'Корпус', bold)
      worksheet.write('J1', 'Кол-во', bold)
      worksheet.write('K1', 'Этаж', bold)
      worksheet.write('L1', 'Этажность', bold)
      worksheet.write('M1', 'Площадь', bold)
      worksheet.write('N1', 'Планировка', bold)
      worksheet.write('O1', 'Цена', bold)
      worksheet.write('P1', 'ИНФО', bold)

   
      with open('_Obj_temp.txt', 'rb') as output_file:
   
         i=2
         while True:
            try:
                   temp = pickle.load(output_file)
                   
                   #print(temp.convert_to_tuple())
             #  for i, (city, street, num_house, num_kor, appart, rooms, floor, floors, plan, price, square, text_info) in enumerate(temp.convert_to_tuple(), start=2):

                   worksheet.write(f'A{i}', temp.add_date, date_format)
                   worksheet.write(f'B{i}', temp.id_object)
                   worksheet.write(f'C{i}', temp.author_object)
                   worksheet.write(f'D{i}', temp.types)
                   worksheet.write(f'E{i}', temp.city)
                   worksheet.write(f'F{i}', temp.street)
                   worksheet.write(f'G{i}', temp.district)
                   worksheet.write(f'H{i}', temp.num_house)
                   worksheet.write(f'I{i}', temp.num_kor)
                   worksheet.write(f'J{i}', temp.rooms)
                   worksheet.write(f'K{i}', temp.floor)
                   worksheet.write(f'L{i}', temp.floors)
                   worksheet.write(f'M{i}', temp.square)
                   worksheet.write(f'N{i}', temp.plan)
                   worksheet.write(f'O{i}', temp.price)
                   worksheet.write(f'P{i}', temp.text_info)
                   i=i+1
            except EOFError:
                break
      workbook.close()

      
    elif name=='House':
      workbook = xlsxwriter.Workbook('2.xlsx')
      worksheet = workbook.add_worksheet()
      bold = workbook.add_format({'bold': True})
      date_format = workbook.add_format({'num_format': 'yy-mm-dd'}) 
      worksheet.write('A1', 'Дата', bold)
      worksheet.write('B1', 'ID', bold)
      worksheet.write('C1', 'Автор', bold)
      worksheet.write('D1', 'Наименование', bold)
      worksheet.write('E1', 'Город', bold)
      worksheet.write('F1', 'Улица', bold)
      worksheet.write('G1', 'Район', bold)
      worksheet.write('H1', 'Дом', bold)
      worksheet.write('I1', 'Корпус', bold)
      worksheet.write('J1', 'Кол-во', bold)
      worksheet.write('K1', 'Этажность', bold)
      worksheet.write('L1', 'Площадь', bold)
      worksheet.write('M1', 'Площадь участка', bold)
      worksheet.write('N1', 'Часть', bold)
      worksheet.write('O1', 'Цена', bold)
      worksheet.write('P1', 'ИНФО', bold)

   
      with open('_Obj_temp.txt', 'rb') as output_file:

         i=2
         
         while True:
            try:
                   temp = pickle.load(output_file)
                   worksheet.write(f'A{i}', temp.add_date, date_format)
                   worksheet.write(f'B{i}', temp.id_object)
                   worksheet.write(f'C{i}', temp.author_object)
                   worksheet.write(f'D{i}', temp.types)
                   worksheet.write(f'E{i}', temp.city)
                   worksheet.write(f'F{i}', temp.street)
                   worksheet.write(f'G{i}', temp.district)
                   worksheet.write(f'H{i}', temp.num_house)
                   worksheet.write(f'I{i}', temp.num_kor)
                   worksheet.write(f'J{i}', temp.rooms)
                   worksheet.write(f'K{i}', temp.floors)
                   worksheet.write(f'L{i}', temp.square)
                   worksheet.write(f'M{i}', temp.land)
                   worksheet.write(f'N{i}', temp.part)
                   worksheet.write(f'O{i}', temp.price)
                   worksheet.write(f'P{i}', temp.text_info)
                   i=i+1
            except EOFError:
                break
      workbook.close()

    elif name=='Gostinki':
      workbook = xlsxwriter.Workbook('2.xlsx')
      worksheet = workbook.add_worksheet()
      bold = workbook.add_format({'bold': True})
      date_format = workbook.add_format({'num_format': 'yy-mm-dd'}) 
      worksheet.write('A1', 'Дата', bold)
      worksheet.write('B1', 'ID', bold)
      worksheet.write('C1', 'Автор', bold)
      worksheet.write('D1', 'Наименование', bold)
      worksheet.write('E1', 'Город', bold)
      worksheet.write('F1', 'Улица', bold)
      worksheet.write('G1', 'Район', bold)
      worksheet.write('H1', 'Дом', bold)
      worksheet.write('I1', 'Корпус', bold)
      worksheet.write('J1', 'Кол-во', bold)
      worksheet.write('K1', 'Этаж', bold)
      worksheet.write('L1', 'Этажность', bold)
      worksheet.write('M1', 'Площадь', bold)
      worksheet.write('N1', 'Цена', bold)
      worksheet.write('O1', 'ИНФО', bold)

   
      with open('_Obj_temp.txt', 'rb') as output_file:

         i=2
         while True:
            try:
                   temp = pickle.load(output_file)
                   #print(temp.convert_to_tuple())
             #  for i, (city, street, num_house, num_kor, appart, rooms, floor, floors, plan, price, square, text_info) in enumerate(temp.convert_to_tuple(), start=2):

                  
                   worksheet.write(f'A{i}', temp.add_date, date_format)
                   worksheet.write(f'B{i}', temp.id_object)
                   worksheet.write(f'C{i}', temp.author_object)
                   worksheet.write(f'D{i}', temp.types)
                   worksheet.write(f'E{i}', temp.city)
                   worksheet.write(f'F{i}', temp.street)
                   worksheet.write(f'G{i}', temp.district)
                   worksheet.write(f'H{i}', temp.num_house)
                   worksheet.write(f'I{i}', temp.num_kor)
                   worksheet.write(f'J{i}', temp.rooms)
                   worksheet.write(f'K{i}', temp.floor)
                   worksheet.write(f'L{i}', temp.floors)
                   worksheet.write(f'M{i}', temp.square)
                   worksheet.write(f'N{i}', temp.price)
                   worksheet.write(f'O{i}', temp.text_info)
                   i=i+1
            except EOFError:
                break

      
      workbook.close()
      

     

   def ends(self):
     self.slave.destroy()

   def go(self, text = ''):
    self.ent_rooms.insert(tk.END, text)
    self.newText = None
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()
    return self.newText
  



   
