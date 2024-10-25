from tkinter import *

class child_report:
   def __init__(self, master):

    self.slave = Toplevel(master)
    self.slave.title('Отчет')
    self.slave.geometry('700x450+500+375')
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


   


   
