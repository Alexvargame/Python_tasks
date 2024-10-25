from tkinter import *
from class_users import *
from report1_class import *

import pickle
import os
import shutil
from email_validate import validate, validate_or_fail
from tkinter import messagebox as mb
from CheckButton import *



class private_room:
    def __init__ (self, master, user):
        self.master=master
        self.user=user
        self.slave = Toplevel(master)
        self.slave.title('Вы вошли в личный кабинет')
        self.slave.geometry('220x200+150+50')
        self.slave.grab_set()
        self.slave.focus_set()
        
        fr_main = Frame(self.slave)
        fr_main.pack()
        fr_main2 = Frame(self.slave)
        fr_main2.pack()
        fr_left = Frame(fr_main)
        fr_left.pack(side=LEFT)
        self.fr_right = Frame(fr_main)
        self.fr_right.pack(side=LEFT)
        self.fr_2 = Frame(self.fr_right)
        self.fr_2.pack()
        self.fr_2a = Frame(self.fr_right)
        self.fr_2a.pack()
        self.fr_2b = Frame(self.fr_right)
        self.fr_2b.pack()
        self.var1 = IntVar()
        self.var1.set(1)
        self.Id_userString=StringVar()
        self.NameString=StringVar()
        self.Name2String=StringVar()
        self.FamilyString=StringVar()
        self.PassString=StringVar()
        self.NikString=StringVar()
        self.MailString=StringVar()
        self.Text_infoString=StringVar()
        self.AcceptString=StringVar()
        self.CountryString=StringVar()
        self.CityString=StringVar()
        self.Id_userString.set(self.user.id_user)
        self.NameString.set(self.user.name)
        self.Name2String.set(self.user.add_info['name2'][0])
        self.FamilyString.set(self.user.add_info['family'][0])
        self.PassString.set(self.user.password)
        self.NikString.set(self.user.nik)
        self.MailString.set(self.user.mail)
        self.AcceptString.set(self.user.accept)
        self.Text_infoString.set(self.user.text_info)
        self.CountryString.set(self.user.add_info['country'][0])
        self.CityString.set(self.user.add_info['city'][0])
        

        lbl_list=Label(fr_left, text="Перечень")
        lbl_list.grid(row=0, column=0)
        #lbl_list1=Label(self.fr_right, text="Данные")
        #lbl_list1.pack()#.grid(row=0, column=0, sticky='e')
        
        lbl_pr_data=Label(fr_left, text="Личные данные")
        lbl_pr_data.grid(row=1, column=0, sticky='w')
        btn=Button(fr_left, text="i", command=self.show_data)
        btn.grid(row=1, column=1)
        lbl_pr_data_add=Label(fr_left, text="Допольнительные")
        lbl_pr_data_add.grid(row=2, column=0, sticky='w')
        btn=Button(fr_left, text="i", command=self.show_data_add)
        btn.grid(row=2, column=1)
        lbl_pr_data_add=Label(fr_left, text="Список объектов")
        lbl_pr_data_add.grid(row=3, column=0, sticky='w')
        btn=Button(fr_left, text="i", command=self.show_object)
        btn.grid(row=3, column=1)
        btn_end=Button(fr_main2, text="Закончить", command=self.ends)
        btn_end.grid(row=1, column=1)
        
    def show_data(self):
        for widget in self.fr_2b.winfo_children():
               widget.destroy()
        self.slave.geometry('350x450+150+50')
        lbl_name=Label(self.fr_2, width=10, text="Имя")
        lbl_name2=Label(self.fr_2, width=10, text="Отчество")
        lbl_family=Label(self.fr_2, width=10, text="Фамилия")
        lbl_nik=Label(self.fr_2, width=10, text="Ник")
        lbl_mail=Label(self.fr_2, width=10, text="E-mail")
        lbl_pass=Label(self.fr_2, width=10, text="Пароль")
  
        self.ent_name=Entry(self.fr_2, width=20, textvariable=self.NameString)
        self.ent_name2=Entry(self.fr_2, width=20, textvariable=self.Name2String)
        self.ent_family=Entry(self.fr_2, width=20, textvariable=self.FamilyString)
        self.ent_nik=Entry(self.fr_2, width=20, textvariable=self.NikString)
        self.ent_mail=Entry(self.fr_2, width=20, textvariable=self.MailString)
        self.ent_pass=Entry(self.fr_2, width=20, textvariable=self.PassString)

        lbl_name.grid(row=0, column=0)
        lbl_name2.grid(row=1, column=0)
        lbl_family.grid(row=2, column=0)
        lbl_nik.grid(row=4, column=0)
        lbl_mail.grid(row=5, column=0)
        lbl_pass.grid(row=6, column=0)

        self.ent_name.grid(row=0, column=1)
        self.ent_name2.grid(row=1, column=1)
        self.ent_family.grid(row=2, column=1)
        self.ent_nik.grid(row=4, column=1)
        self.ent_mail.grid(row=5, column=1)
        self.ent_pass.grid(row=6, column=1)
        self.c_n=CheckButton(self.fr_2,self.user.add_info['name2'][1],1,2)
        self.c_f=CheckButton(self.fr_2,self.user.add_info['family'][1],2,2)
        lbl=Label(self.fr_2b, text="Отметьте открытую \n всем информацию")
        lbl.grid(row=8,column=1)
        btn=Button(self.fr_2b, text="Сохранить изменения", command=self.save_change)
        btn.grid(row=9, column=1)
        btn=Button(self.fr_2b, text="Закрыть", command=self.close_data)
        btn.grid(row=10, column=1)
    def show_data_add(self):
        for widget in self.fr_2b.winfo_children():
               widget.destroy()
        self.slave.geometry('350x450+150+50')


        
        lbl_country=Label(self.fr_2a, width=10, text="Страна")
        lbl_city=Label(self.fr_2a, width=10, text="Город")
        lbl_text_info=Label(self.fr_2a, width=10, text="Инф-ия")

        self.ent_country=Entry(self.fr_2a,width=20, textvariable=self.CountryString)
        self.ent_city=Entry(self.fr_2a, width=20, textvariable=self.CityString)
        self.ent_text_info=Text(self.fr_2a,width=15, height=10)
        lbl_country.grid(row=4, column=0)
        lbl_city.grid(row=5, column=0)
        lbl_text_info.grid(row=6, column=0)

        self.ent_country.grid(row=4, column=1)
        self.ent_city.grid(row=5, column=1)
        self.ent_text_info.grid(row=6, column=1)
        self.c_ct=CheckButton(self.fr_2a,self.user.add_info['country'][1],4,2)
        self.c_c=CheckButton(self.fr_2a,self.user.add_info['city'][1],5,2)
        lbl=Label(self.fr_2b, text="Отметьте открытую \n всем информацию")
        lbl.grid(row=8,column=1)
        btn=Button(self.fr_2b, text="Сохранить изменения", command=self.save_change)
        btn.grid(row=9, column=1)
        btn=Button(self.fr_2b, text="Закрыть", command=self.close_data)
        btn.grid(row=10, column=1)
    def close_data(self):
        for widget in self.fr_2.winfo_children():
               widget.destroy()
        for widget in self.fr_2a.winfo_children():
               widget.destroy()
        for widget in self.fr_2b.winfo_children():
               widget.destroy()
        self.slave.geometry('220x200+150+50')
    def show_object(self):
        self.search_my_object()
        self.report_search = child_report_search(self.slave, "my_object", self.user)
    def show_(self):
        if self.c_n.var.get():
            self.user.add_info['name2'][1]=1
        else: self.user.add_info['name2'][1]=0
        if self.c_f.var.get():
            self.user.add_info['family'][1]=1
        else: self.user.add_info['family'][1]=0
        if self.c_ct.var.get():
            self.user.add_info['country'][1]=1
        else: self.user.add_info['country'][1]=0
        if self.c_c.var.get():
            self.user.add_info['city'][1]=1
        else: self.user.add_info['city'][1]=0
       
    def search_my_object(self):

      f=open('_Obj_temp.txt', 'wb')
      f.close()   
      name=''
      objects=['Flats', 'House', 'Gostinki']
      for name in objects:
          with open('_'+name+'_class.txt', 'rb') as output_file:
            while True:
                try:
                   temp = pickle.load(output_file)
                   l=temp.author_object.split(' ')
                   if l[1]==self.user.id_user:
                       print("1")
                       temp.pickle_search()
                except EOFError:
                   break       

       
    def save_change(self):
            f=open('_Users_del.txt', 'wb')
            f.close()
               
        #try:
        #    validate_or_fail(self.MailString.get(), check_blacklist=False, check_smtp=False)
            #if validate_or_fail(self.MailString.get(), check_blacklist=True, check_smtp=True):  - чтобы проверить на черный список доменов и существование почты

            
            if (self.NameString.get()=="" or  self.NikString.get()=="" or self.MailString.get()=="" or self.PassString.get()==""):
                mb.showwarning("","Есть пустые поля")
            else:
                    check=0
                    with open('_Users.txt', 'rb') as output_file:       
                         while True:
                             try:
                               temp=pickle.load(output_file)
                               if temp.nik==self.NikString.get() and self.user.nik!=self.NikString.get():
                                   check=1
                                   self.ent_nik['bg']='red'
                                   mb.showwarning("","Пользователь с таким ником уже существует")
                                   break
                               elif temp.mail==self.MailString.get() and self.user.mail!=self.MailString.get():
                                   
                                   check=1
                                   self.ent_mail['bg']='red'
                                   mb.showwarning("","E-mail уже зарегистрирован")
                                   break 
                             except EOFError:
                                 break
                    print(check)
                    if check==0:
                         print("DO", self.user)
                         self.user=Users(self.Id_userString.get(),self.NameString.get(),  self.NikString.get(), self.MailString.get(),
                                         self.PassString.get(), self.AcceptString.get(), self.Text_infoString.get())
                         self.user.add_info={'name2': [self.Name2String.get(), 0], 'family': [self.FamilyString.get(), 0],
                                             'country': [self.CountryString.get(), 0],'city': [self.CityString.get(), 0],}
                         
                         print("AF",self.user)
                         self.show_()
                         self.print_info=self.user.print_info_()
                         print("AF1", self.user)
                         with open('_Users.txt', 'rb') as output_file1:
                           while True:
                                try:
                                   temp1=pickle.load(output_file1)
                                   with open('_Users_del.txt', 'rb') as output_file2:
                                       if temp1.id_user==self.user.id_user:
                                           self.user.assign(temp1)
                                           temp1.pickle('_Users_del.txt')
                                           print(temp1.add_info['family'][0])
                                           del temp1
                                       else:
                                           temp1.pickle('_Users_del.txt')
                                           del temp1         
                                except EOFError:
                                      break
                         file_oldname = os.path.join("C:\Python36-32\Flat", "_Users_del.txt")
                         file_newname = os.path.join("C:\Python36-32\Flat","_Users.txt")
                         shutil.move(file_oldname, file_newname)
        #except: mb.showwarning("","Email введен некорректно")
        
            return self.user
    def ends(self):
         self.slave.destroy()
    
        

