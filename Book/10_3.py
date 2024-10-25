from tkinter import *
import tkinter as tk
from datetime import *



w=Tk()
w.title("W")
w.geometry("250x150")
ag=tk.IntVar()


f=Frame(w)
f.pack()
l=Label(f, text="Hi")
l.pack()
l1=Label(f, text="1")
l1.pack()
age=Entry(f, textvariable=ag)
age.pack()
def age_():
    print(ag.get())
    l1.configure(text=str(datetime.now().year-ag.get()))
b=Button(f,text="Ok", command=age_)
b.pack()


w.mainloop()
