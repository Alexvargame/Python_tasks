from tkinter import *
from class_users import *
import pickle
from tkinter import messagebox as mb
from email_validate import validate, validate_or_fail
import random
from datetime import *


class registration:
    def __init__ (self, master):
    
    
        self.slave = Toplevel(master)
        self.slave.title('Введите логин и пароль')
        self.slave.geometry('220x300+150+50')

        self.Id_userString=StringVar()
        self.NameString=StringVar()
        self.PassString=StringVar()
        self.NikString=StringVar()
        self.MailString=StringVar()
        self.Pass1String=StringVar()
        self.AcceptString=StringVar()
        self.Id_userString.set("")
        #self.AcceptString.set('user')
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
        lbl_name=Label(fr_2, text="Имя")
        lbl_nik=Label(fr_2, text="Ник")
        lbl_mail=Label(fr_2, text="E-mail")
        lbl_pass=Label(fr_2, text="Пароль")
        lbl_pass1=Label(fr_2, text="Пароль еще раз")
        self.ent_name=Entry(fr_2, width=20, textvariable=self.NameString)
        self.ent_nik=Entry(fr_2, width=20, textvariable=self.NikString)
        self.ent_mail=Entry(fr_2, width=20, textvariable=self.MailString)
        self.ent_pass=Entry(fr_2, show='*', width=20, textvariable=self.PassString)
        self.ent_pass1=Entry(fr_2, show='*', width=20, textvariable=self.Pass1String)
        lbl_name.grid(row=0, column=0)
        lbl_nik.grid(row=2, column=0)
        lbl_mail.grid(row=4, column=0)
        lbl_pass.grid(row=6, column=0)
        lbl_pass1.grid(row=8, column=0)


        self.ent_name.grid(row=1, column=0)
        self.ent_nik.grid(row=3, column=0)
        self.ent_mail.grid(row=5, column=0)
        self.ent_pass.grid(row=7, column=0)
        self.ent_pass1.grid(row=9, column=0)
        self.c1 = Checkbutton(fr_2, text="Показать пароль",
                 variable=self.var1,
                 onvalue=1, offvalue=0,
                 command=self.show_pass)
        self.c1.grid(row=10, column=0)
        btn_sub=Button(fr_3, text="Регистрация", width=20, command=self.registr)
        btn_sub.grid(row=0, column=0)
        btn_sub=Button(fr_3, text="Выход", width=20, command=self.close_window)
        btn_sub.grid(row=1, column=0)
    def show_pass(self):
       
       if self.var1.get()==1:
           self.ent_pass.config(show="*")
           self.ent_pass1.config(show="*")
       else:
           self.ent_pass.config(show="")
           self.ent_pass1.config(show="") 
    def registr(self):
            self.ent_nik['bg']='white'
            self.ent_mail['bg']='white'
        #try:
        #    validate_or_fail(self.MailString.get(), check_blacklist=False, check_smtp=False)
            #if validate_or_fail(self.MailString.get(), check_blacklist=True, check_smtp=True):  - чтобы проверить на черный список доменов и существование почты

            
            if (self.NameString.get()=="" or  self.NikString.get()=="" or self.MailString.get()=="" or self.PassString.get()=="" or self.Pass1String.get()==""):
                mb.showwarning("","Есть пустые поля")
            else:
                if self.Pass1String.get()==self.PassString.get():
                    new_user = Users(self.Id_userString.get(), self.NameString.get(),  self.NikString.get(), self.MailString.get(), self.PassString.get(), datetime.now())#, self.AcceptString.get())
                    check=0
                    with open('_Users.txt', 'rb') as output_file:       
                         while True:
                             try:
                               temp=pickle.load(output_file)
                               
                               if temp.nik==new_user.nik:
                                   check=1
                                   self.ent_nik['bg']='red'
                                   mb.showwarning("","Пользователь с таким ником уже существует")
                                   break
                               elif temp.mail==new_user.mail:
                                   check=1
                                   self.ent_mail['bg']='red'
                                   mb.showwarning("","E-mail уже зарегистрирован")
                                   break 
                             except EOFError:
                                break
                    if check==0:
                      #new_user.add_info= {'data': [4, 2.5]}
                      new_user.id_user=str(random.randint(1,10000))+new_user.nik
                      with open('_Users.txt', 'rb') as output_file:
                            new_user.pickle('_Users.txt')
                            mb.showinfo("", "Регистрация прошла успешно")
                            self.slave.destroy()
                else: mb.showwarning("","Пароли не совпадают")
        #except: mb.showwarning("","Email введен некорректно")
    def close_window(self):
         self.slave.destroy()
                 




