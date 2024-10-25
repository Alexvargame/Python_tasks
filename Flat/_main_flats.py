import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from Enter_info import *
from Search_info_class import *
from boolean import *
from Type_object import *
import xlsxwriter
from tkinter.filedialog import askopenfilename, asksaveasfilename
import pickle
from Autorization import *
from Registration import *
from Private_room import *
from admin_room import *
from tkinter import messagebox as mb





class main:
   def __init__(self, master):
      self.user = Users("","","","","","","")
      self.admin_user = ("admin","admin","admin","admin@gmail.com", "admin", "admin")
      self.master = master
      self.master.title('DATA')
      self.master.geometry('250x250+300+225')
      self.main_frame = Frame(self.master)
      self.main_frame.pack(expand=1)
      self.admin_frame = Frame(self.master)
      self.admin_frame.pack(expand=1)
      self.main_panel(self.user)
      self.master.mainloop()
      

   def main_panel(self, user): 
      
      for widget in self.main_frame.winfo_children():
               widget.destroy()
      self.button1 = Button(master=self.main_frame,
                            text="Жилые объекты",width=15, height=3,
                            command = self.openAddObject)
      self.button1.pack()

      self.button2 = Button(master=self.main_frame, text="Поиск",width=15, height=3,
                            command = self.openSearch)
      self.button2.pack(pady=2)
      try:
         if user.accept!="user" and user.accept!="admin" :
            self.button3 = Button(master=self.main_frame, text="Войти",width=15, height=2, command=self.openAutoriz)                 
            self.button3.pack(pady=2)
            self.button4 = Button(master=self.main_frame, text="Регистрация",width=15, height=2, command = self.openRegistr)
            self.button4.pack()
         elif user.accept=='admin' or user.accept=='user':
            self.label = Label(master=self.main_frame, text='Привет, ' + user.nik)
            self.label.pack()
            self.admin_button()
      except:
         pass
      
      
      """
      try:
         if autorization.user_value(self)=="admin" :
            self.button5 = Button(master=self.main_frame, text="Админ-панель",width=15, height=2,
                           command = self.admin_panel)
            self.button5.pack()
      except:
         pass
      """
      self.master.protocol('WM_DELETE_WINDOW', 
                         self.exitMethod)
      
   
   def admin_button(self):

      self.button5 = Button(master=self.main_frame, text="Личный кабинет",width=15, height=2, command = self.admin_panel)
      self.button5.pack()
      self.button6 = Button(master=self.main_frame, text="Выход",width=15, height=2, command = self.exit_user)
      self.button6.pack()

   def admin_panel(self):
      if self.user.accept=="user":
         private_room(self.master, autorization.return_user(self))
      elif self.user.accept=="admin" :
         admin_room(self.master, autorization.return_user(self))
         
   def exit_user(self):
      self.user= Users("","","","","","","")
      self.main_panel(self.user)
      
    
 
   def openAddObject(self):
      try:
         if self.user.accept=="user" or self.user.accept=="admin" : 
            child(self.master, self.user)
         else:
            mb.showwarning("","Войдите пол своим аккаунтом или зарегистрируйтесь")
      except:
         pass
        
   def openReport(self):
      self.report = child_report(self.master)
      with open('1.txt', 'r') as output_file:
           self.t = output_file.read() 
           self.returnText = self.report.go(self.t)
   def openAutoriz(self):
      autorization(self.master, self.user)
      self.user=autorization.return_user(self)
      if self.user.accept=="user" or self.user.accept=="admin" : 
         self.main_panel(self.user)
      

   def openRegistr(self):
      registration(self.master)
      
              
   def openSearch(self):
      try:
         if self.user.accept=="user" or self.user.accept=="admin" :
            child_search(self.master, self.user)
         else:
            mb.showwarning("","Войдите пол своим аккаунтом или зарегистрируйтесь")
      except:
         pass
         

   def exitMethod(self):
    self.dialog = yesno(self.master)
    self.returnValue = self.dialog.go('question',
                                      'Вы хотите выйти?')
    if self.returnValue:
      self.master.destroy()
      

        



root = Tk()
main(root)
      
    
