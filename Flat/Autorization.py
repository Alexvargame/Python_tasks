from tkinter import *
import pickle
from tkinter import messagebox as mb
from class_users import *
from datetime import *


class autorization:
    def __init__ (self, master, user):
    
        global Enter, NikString, PassString, AcceptString, NameString, MailString
        NikString=StringVar()
        PassString=StringVar()
        AcceptString=StringVar()
        NameString=StringVar()
        MailString=StringVar()
        Enter=StringVar()
        self.user = user
        self.slave = Toplevel(master)
        self.slave.title('Введите логин/e-mail и пароль')
        self.slave.geometry('220x120+150+50')
        
        
        
        self.var1 = IntVar()
        self.var1.set(1)

        fr = Frame(self.slave)
        fr.pack()
        fr_1 = Frame(self.slave)
        fr_1.pack()
        fr_2 = Frame(self.slave)
        fr_2.pack()
        fr_3 = Frame(self.slave)
        fr_3.pack()
        lbl_auto=Label(fr_1, text="Enter data")
        lbl_auto.grid(row=0, column=0) 
        self.ent_nik=Entry(fr_2, width=20, textvariable=NikString)
        self.ent_pass=Entry(fr_2, show='*', width=20, textvariable=PassString)
        self.ent_nik.grid(row=0, column=0)
        self.ent_pass.grid(row=1, column=0)
        btn_sub=Button(fr_3, text="Submit", width=20, command=self.autoriz)
        #btn_sub=Button(fr_3, text="Submit", width=20, command= lambda: self.autoriz(NikString.get(), PassString.get()))
        btn_sub.grid(row=0, column=0)
        self.c1 = Checkbutton(fr_2, text="Показать пароль",
                 variable=self.var1,
                 onvalue=1, offvalue=0,
                 command=self.show_pass)
        self.c1.grid(row=2, column=0)
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()

    def autoriz(self):

        Enter.set("")
        if NikString.get()=='admin' and PassString.get()=='admin':
            Enter.set("admin")
            NikString.set("admin")
            PassString.set("admin")
            AcceptString.set("admin")
            NameString.set("admin")
            MailString.set("admin")
            
            temp=Users("admin",NameString.get(), NikString.get(),  MailString.get(), PassString.get(), datetime.now(), AcceptString.get())
            temp.assign(self.user)
            self.user.add_info={'name2': [None, 0], 'family': [None , 0], 'country': [None, 0],'city': [None, 0],}
            self.user.print_info = self.user.print_info_()
            mb.showinfo("",'Привет, ' + NikString.get())      
            self.slave.destroy()
            return self.user
        else:
            with open('_Users.txt', 'rb') as output_file:
                 while True:
                     try:
                       temp=pickle.load(output_file)
                       if ((temp.nik==NikString.get() or temp.mail==NikString.get()) and temp.password==PassString.get()
                           and NikString.get()!='' and PassString.get()!=''):
                    
                           temp.assign(self.user)
                           self.user.print_info = self.user.print_info_()
                           self.user.time_last_vizit=datetime.today()
                           Enter.set("user")
                           self.slave.destroy()
                           mb.showinfo("",'Привет, ' + NikString.get())

                           break
                     except EOFError:
                       break
            
            return self.user
       # if Enter.get()=='':
        #    mb.showwarning("",'такого пользователя нет')
        return self.user
        
        
  
    def show_pass(self):
       
       if self.var1.get()==1:
           self.ent_pass.config(show="*")
       else: self.ent_pass.config(show="")
    """
    def user_value(self):
            value=Enter.get()
            print("4", value)
            return value
    """
    def return_user(self):
       ret_user=self.user
       return ret_user


