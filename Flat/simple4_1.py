import tkinter as tk
from tkinter import *


from tkinter.filedialog import askopenfilename, asksaveasfilename

class main:
   def __init__(self, master):
      self.master = master
      self.master.title('Flats')
      self.master.geometry('150x150+300+225')
      self.button1 = Button(self.master,
                            text="Данные",
                            command = self.openDialog)
      self.button1.pack(side = TOP)
      self.button2 = Button(self.master, text="Oтчет",
                            command = self.openReport)
      self.button2.pack(side = BOTTOM)
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

   def exitMethod(self):
    self.dialog = yesno(self.master)
    self.returnValue = self.dialog.go('question',
                                      'Вы хотите выйти?')
    if self.returnValue:
      self.master.destroy()

      

class child:
   def __init__(self, master):

    self.RoomsString = tk.StringVar()
    self.FloorString = tk.StringVar()
    self.PriceString = tk.StringVar()
    self.resultString = tk.StringVar()

    
    self.slave = Toplevel(master)
    self.slave.title('Ввод характеристик')
    self.slave.geometry('200x150+500+375')
    self.lbl_rooms = Label(self.slave, text="Кол-во комнат")
    self.ent_rooms = Entry(self.slave, width=50, textvariable=self.RoomsString)
    
    self.lbl_rooms.grid(row=0, column=0, sticky="e")
    self.ent_rooms.grid(row=0, column=1)
    
    
    
    self.lbl_floor = Label(self.slave, text="Этаж")
    self.ent_floor = Entry(self.slave, width=50, textvariable=self.FloorString)
    self.lbl_floor.grid(row=1, column=0, sticky="e")
    self.ent_floor.grid(row=1, column=1)

    self.lbl_price = Label(self.slave, text="Цена")
    self.ent_price = Entry(self.slave, width=50, textvariable=self.PriceString)
    self.lbl_price.grid(row=2, column=0, sticky="e")
    self.ent_price.grid(row=2, column=1)

    self.btn_save = Button(self.slave, text="Сохранить", command=self.save_stat)
    self.btn_save.grid(row=3, column=1, sticky='w')
    
    self.btn_save = Button(self.slave, text="Далее", command=self.next_stat )
    self.btn_save.grid(row=4, column=1, sticky='w')
    
    self.btn_save = Button(self.slave, text="Завершить", command=self.end_stat)
    self.btn_save.grid(row=5, column=1, sticky='w')
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()

   
   def save_stat(self):

     self.resultString.set("Кол-во комнат -{} Этаж -  {} Цена - {}\n".format(self.RoomsString.get(), self.FloorString.get(), self.PriceString.get()))

    
        
   def next_stat(self):
       self.RoomsString.set("")
       self.FloorString.set("")
       self.PriceString.set("")
       
   def end_stat(self):
   
       self.slave.destroy()
  

class child_report:
   def __init__(self, master):

    self.slave = Toplevel(master)
    self.slave.title('Отчет')
    self.slave.geometry('500x450+500+375')
    self.button = Button(self.slave,
                         text = "Отмена",
                         command=self.ends)
    self.button.pack(side=BOTTOM)
    
    self.text = Text(self.slave)
    self.text.pack(side=TOP, fill=BOTH, expand=YES) 

   def ends(self):
     self.slave.destroy()

   def go(self, myText = ''):
    self.text.insert('0.0', myText)
    self.newText = None
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()
    return self.newText


   


   def report(self):
       with open('1.txt', 'r') as output_file:
        self.t = output_file.read()
        print(self.t)
        self.text.insert('0.0', self.t)

# класс диалогового окна выхода
class yesno:
  def __init__(self, master):
    self.slave = Toplevel(master)
    self.slave.title('Выход')
    self.slave.geometry('200x100+300+250')
    self.frame = Frame(self.slave)
    self.frame.pack(side = BOTTOM)
    self.yes_button = Button(self.frame,
                             text = 'yes',
                             command = self.yes)
    self.yes_button.pack(side = LEFT)
    self.no_button = Button(self.frame,
                            text = 'no',
                            command = self.no)
    self.no_button.pack(side = RIGHT)
    self.label = Label(self.slave)
    self.label.pack(side = TOP, fill = BOTH, expand = YES)
    self.slave.protocol('WM_DELETE_WINDOW', self.no)

  def go(self, title = '', message = ''):
    self.slave.title(title)
    self.label.configure(text = message)
    self.booleanValue = TRUE
    self.slave.grab_set()
    self.slave.focus_set()
    self.slave.wait_window()
    return self.booleanValue

  def yes(self):
    self.booleanValue = TRUE
    self.slave.destroy()

  def no(self):
    self.booleanValue = FALSE
    self.slave.destroy()      

root = Tk()
main(root)
      
    
