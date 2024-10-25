from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import xlsxwriter



class child_report_search:
   def __init__(self, child_search):
    #super().__init__(self)
    self.slave = Toplevel(child_search)
    self.slave.title('Отчет')
    self.slave.geometry('800x450+400+200')
  

    self.frm_label = Frame(self.slave, relief=tk.SUNKEN, borderwidth=3)
    self.frm_label.pack(fill=tk.X, ipadx=5, ipady=5)
    self.lbl_empty = tk.Label(master=self.frm_label, text="       ")
    self.lbl_empty.grid(row=0, column=0, sticky="w")
    self.lbl_city = tk.Label(master=self.frm_label, text="Город")
    self.lbl_city.grid(row=0, column=1, sticky="w")
    self.lbl_street = tk.Label(master=self.frm_label, text="Улица")
    self.lbl_street.grid(row=0, column=2, sticky="w")
    self.lbl_house_appart = tk.Label(master=self.frm_label, text="№дом/кв")
    self.lbl_house_appart.grid(row=0, column=3, sticky="w")
    self.lbl_rooms = tk.Label(master=self.frm_label, text="Кол-во комнат")
    self.lbl_rooms.grid(row=0, column=4, sticky="w")
    self.lbl_floor = tk.Label(master=self.frm_label, text="Этаж")
    self.lbl_floor.grid(row=0, column=5, sticky="w")
    self.lbl_floors = tk.Label(master=self.frm_label, text="Этажность")
    self.lbl_floors.grid(row=0, column=6, sticky="w")
    self.lbl_plan = tk.Label(master=self.frm_label, text="Планировка")
    self.lbl_plan.grid(row=0, column=7, sticky=tk.E)
    self.lbl_price = tk.Label(master=self.frm_label, text="Цена")
    self.lbl_price.grid(row=0, column=8, sticky=tk.E)

    #self.lbl_text = tk.Text(master=self.frm_label)
    #self.lbl_text.grid()

    self.frm_entry = Frame(self.slave)
    self.frm_entry.pack(side=tk.LEFT, fill=tk.Y, ipadx=5, ipady=5)
    self.frm_text = Frame(self.slave)
    self.frm_text.pack(side=tk.LEFT, fill=tk.BOTH, ipadx=5, ipady=5)

    

    with open('2.txt', 'r') as output_file:
           
          self.t = output_file.readlines()

       
          for i in range(len(self.t)):
             
               l = self.t[i].split(',')
               l1 = l[1].split('.')
               self.btn_info = tk.Button(master=self.frm_entry, text="I")
               self.btn_info.bind("<Button-1>", self.info_to_window)
               self.ent_city = tk.Entry(master=self.frm_entry, width=10)
               self.ent_city.insert(tk.END, l1[0])
               self.ent_street = tk.Entry(master=self.frm_entry, width=10)
               self.ent_street.insert(tk.END, l1[1])
               self.ent_house_appart = tk.Entry(master=self.frm_entry, width=10)
               self.ent_house_appart.insert(tk.END, 'Дом'+l1[2]+' Корп'+l1[3]+' Кв'+l1[4])  
               self.ent_rooms = tk.Entry(master=self.frm_entry, width=10)
               self.ent_rooms.insert(tk.END, l[2])  
               self.ent_floor = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floor.insert(tk.END, l[3])  
               self.ent_floors = tk.Entry(master=self.frm_entry, width=10)
               self.ent_floors.insert(tk.END, l[4])  
               self.ent_plan = tk.Entry(master=self.frm_entry, width=10)
               self.ent_plan.insert(tk.END, l[5])  
               self.ent_price = tk.Entry(master=self.frm_entry, width=10)
               self.ent_price.insert(tk.END, l[6])  
               self.btn_info.grid(row=i, column=0, sticky=tk.E)
               self.ent_city.grid(row=i, column=1, sticky=tk.E)
               self.ent_street.grid(row=i, column=2, sticky=tk.E)
               self.ent_house_appart.grid(row=i, column=3, sticky=tk.E)
               self.ent_rooms.grid(row=i, column=4, sticky=tk.E)
               self.ent_floor.grid(row=i, column=5, sticky=tk.E)
               self.ent_floors.grid(row=i, column=6, sticky=tk.E)
               self.ent_plan.grid(row=i, column=7, sticky=tk.E)
               self.ent_price.grid(row=i, column=8, sticky=tk.E)
              
    
    self.frm_excel = Frame(self.slave)
    self.frm_excel.pack(side=tk.BOTTOM, fill=tk.BOTH, ipadx=5, ipady=5)
    self.btn_excel = tk.Button(master=self.frm_excel, text="Получить ввиде таблицы", command=self.info_to_excel)
    #self.btn_info.bind("<Button-1>", self.info_to_window)
    self.btn_excel.grid(row=0, column=0, sticky=tk.NW)
    self.btn_end = tk.Button(master=self.frm_excel, text="Завершить", command=self.end_stat)
    self.btn_end.grid(row=0, column=2, sticky='e')

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
            
      
      self.txt_info = tk.Text(master=self.frm_text, width=40)
      self.txt_info.grid(row=0, column=0, sticky=tk.E)
      self.txt_info.delete(1.0, END)
      
      with open('2.txt', 'r') as output_file:
           
          self.t = output_file.readlines()

       
          for i in range(len(self.t)):

               l = self.t[i].split(',')
               if int(l[0])==grid_info["row"]:
                  self.txt_info.insert(1.0, self.t[i])
                  break

      
   def info_to_excel(self):

      workbook = xlsxwriter.Workbook('2.xlsx')
      worksheet = workbook.add_worksheet()
      bold = workbook.add_format({'bold': True})
      worksheet.write('A1', 'Наименование', bold)
      worksheet.write('B1', 'Город', bold)
      worksheet.write('C1', 'Улица', bold)
      worksheet.write('D1', 'Дом/кв', bold)
      worksheet.write('E1', 'Кол-во', bold)
      worksheet.write('F1', 'Этаж', bold)
      worksheet.write('G1', 'Этажность', bold)
      worksheet.write('H1', 'Планировка', bold)
      worksheet.write('I1', 'Цена', bold)

      l = []
      
      with open('2.txt', 'r') as output_file:
         self.t = output_file.readlines()
         for i in range(len(self.t)):
           l1 = list(self.t[i].split(','))
           l2 = list(l1[1].split('.'))
           l1.pop(0)
           l1.pop(0)
           l1.insert(0, l2[0])
           l1.insert(1, l2[1])
           l1.insert(2, "".join(['Дом'+l2[2]+' Кор'+l2[3]+' Кв'+l2[4]]))
           print(l2[2]+l2[3]+l2[4])
           l.append(l1)
          
      t1 = tuple(l)
      for i, (city, street, house, rooms, floor, floors, plan, price) in enumerate(t1, start=2):
        
          worksheet.write(f'A{i}', "Квартира")
          worksheet.write(f'B{i}', city)
          worksheet.write(f'C{i}', street)
          worksheet.write(f'D{i}', house)
          worksheet.write(f'E{i}', rooms)
          worksheet.write(f'F{i}', floor)
          worksheet.write(f'G{i}', floors)
          worksheet.write(f'H{i}', plan)
          worksheet.write(f'I{i}', price)
      
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
  



   
