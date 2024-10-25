import tkinter as tk
from tkinter import *
from Enter_info import *
from report import *
from boolean import *


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

      


  



# класс диалогового окна выхода


root = Tk()
main(root)
      
    
