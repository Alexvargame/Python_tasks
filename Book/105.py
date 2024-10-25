from tkinter import *
import tkinter as tk
from datetime import *



w=Tk()
w.title("W")
w.geometry("250x150")
ent=tk.IntVar()


f=Frame(w)
f.pack()

l=Label(f, text="Hello")
l.pack()


def bigger_():
    l.configure(font="24")
def smaller_():
    l.configure(font.size=8)
b=Button(f,text="1", command=bigger_)
b.pack()
b1=Button(f,text="2", command=smaller_)
b1.pack()


w.mainloop()
