import calendar
from datetime import *
from tkinter import *
import tkinter as tk

class calendar_choice:
    def __init__(self, child_search):
        global CalDate1         
        CalDate1 = tk.StringVar()
        global CalDate2         
        CalDate2 = tk.StringVar()
        
        def month_prev():
            if m_y[0]!=1:
                m_y[0]=m_y[0]-1
                m_y[1]=m_y[1]
                self.lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
                day_number(list_day, m_y)
                #self.ent_date_begin.delete(0, END)
                #self.ent_date_end.delete(0, END)
            else:
                m_y[0]=12
                m_y[1]=m_y[1]-1
                self.lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
                day_number(list_day, m_y)
                #self.ent_date_begin.delete(0, END)
                #self.ent_date_end.delete(0, END)
                return m_y
            
        def month_post():
            if m_y[0]!=12:
                m_y[0]=m_y[0]+1
                m_y[1]=m_y[1]
                self.lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
                day_number(list_day, m_y)
                #self.ent_date_begin.delete(0, END)
                #self.ent_date_end.delete(0, END)
            else:
                m_y[0]=1
                m_y[1]=m_y[1]+1
                self.lbl_m_y['text'] = str(month_[m_y[0]])+"  "+str(m_y[1])
                day_number(list_day, m_y)
                #self.ent_date_begin.delete(0, END)
                #self.ent_date_end.delete(0, END)
                return m_y


        def choice_date(event):
            grid_info = event.widget.grid_info()
            if self.ent_date_begin.get()=="":
               self.date_begin=date(m_y[1], m_y[0], list_day[grid_info["row"]*7+grid_info["column"]])
               self.ent_date_begin.insert(0, self.date_begin)          
            else:   
               self.date_end=date(m_y[1], m_y[0], list_day[grid_info["row"]*7+grid_info["column"]])
               self.ent_date_end.insert(0, self.date_end)

    
    
        def day_number(list_day, m_y):
            list_day.clear()
            for widget in self.fr_1.winfo_children():
                    widget.destroy()

            c = calendar.Calendar()
            for k in c.itermonthdays (m_y[1], m_y[0]):
                list_day.append(k)
            for i in range(int(len(list_day)/7)):
             for j in range(7):
     
                self.btn_day=Button(self.fr_1,width=1, height=1)
                self.btn_day.bind("<Button-1>", choice_date)
                self.btn_day['text']=""
                if list_day[j+7*i]!=0:
                   self.btn_day['text']=list_day[j+7*i]
                   self.btn_day.grid(row=i, column=j)
                j=j+1
             i=i+1
            return list_day
        

        self.slave = Toplevel(child_search)
        self.slave.title('Выбор даты')
        self.slave.geometry('180x250+150+50')
        self.fr = Frame(self.slave)
        self.fr.pack()
        self.fr_1 = Frame(self.slave)
        self.fr_1.pack()
        self.fr_2 = Frame(self.slave)
        self.fr_2.pack()

        month_={1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
        today=datetime.today()
        
        i=0
        j=0
        m_y = [today.month,today.year]
        list_day=[]
        c = calendar.Calendar()
        for k in c.itermonthdays (today.year, today.month):
            list_day.append(k)
        self.lbl_m_y = Label(self.fr, text="  ")
        self.lbl_m_y['text'] = str(month_[today.month])+"  "+str(today.year)
        self.lbl_week = Label(self.fr, text="Mo  Tu  We  Th  Fr  Sa  Su")
        self.btn_prev = Button(self.fr, text="<<", width=2, command=month_prev)
        self.btn_post = Button(self.fr, text=">>", width=2, command=month_post)
        self.btn_prev.grid(row=0, column=0)
        self.btn_post.grid(row=0, column=6)
        self.lbl_m_y.grid(row=0, column=1, columnspan=5)
        self.lbl_week.grid(row=1, column=0, columnspan=7)
        self.ent_date_begin = Entry(self.fr_2, width=10, textvariable=CalDate1)
        self.ent_date_end = Entry(self.fr_2, width=10, textvariable=CalDate2)
        self.ent_date_begin.grid(row=0, column=0)
        self.ent_date_end.grid(row=0, column=6)
        self.btn_end = Button(self.fr_2, text="Очистить", command=self.clear_date)
        self.btn_end.grid(row=2, column=0, sticky='w')
        self.btn_end = Button(self.fr_2, text="Выбрать", command=self.end_stat)
        self.btn_end.grid(row=3, column=0, sticky='w')
        
       
        for i in range(int(len(list_day)/7)):
             for j in range(7):     
                self.btn_day=Button(self.fr_1,width=1, height=1)
                self.btn_day.bind("<Button-1>", choice_date)
                if list_day[j+7*i]!=0:
                    self.btn_day['text']=list_day[j+7*i]
                    self.btn_day.grid(row=i, column=j)   
                j=j+1
             i=i+1
        self.slave.grab_set()
        self.slave.focus_set()
        self.slave.wait_window()
        print(CalDate1.get())
        self.toget()
    def toget(self):
        print(CalDate1.get(), CalDate2.get())
        return CalDate1.get(), CalDate2.get()
    def clear_date(self):
        self.ent_date_begin.delete(0, END)
        self.ent_date_end.delete(0, END)
    def end_stat(self):
       self.slave.destroy()

   
    

        

