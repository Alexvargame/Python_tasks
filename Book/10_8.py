from tkinter import *
import tkinter as tk
from datetime import *



w=Tk()
w.title("W")
w.geometry("250x150")
m=StringVar()
def r():
    st=m.get()  

    l.configure(text=eval(st))
f=Frame(w)
f.pack()
ent=Entry(f, textvariable=m)
ent.pack()
print(type(m.get()))
l=Label(f, text='1')

b=Button(w, command=r)
b.pack()

l.pack()


w.mainloop()
