from tkinter import *
import tkinter as tk
from datetime import *



w=Tk()
w.title("W")
w.geometry("250x150")
ent=tk.IntVar()


f=Frame(w)
f.pack()


entr=Entry(f, textvariable=ent)
entr.pack()
l=Label(f, textvariable=ent)
l.pack()
def clear_():
    ent.set('')
    l.configure(text="")
b=Button(f,text="1", command=clear_)
b.pack()
b1=Button(f,text="2", command=w.destroy)
b1.pack()


w.mainloop()
