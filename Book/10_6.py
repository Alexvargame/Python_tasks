from tkinter import *
import tkinter as tk
from datetime import *



w=Tk()
w.title("W")
w.geometry("250x150")


f=Frame(w)
f.pack()
color=StringVar()
def colors():
    l.configure(bg=color.get())
l=Label(f, textvariable=color)
rd1=Radiobutton(f, text='red', value='red', command=colors, variable=color)

rd2=Radiobutton(f, text='blue', value='blue', command=colors, variable=color)

rd3=Radiobutton(f, text='green', value='green', command=colors, variable=color)

color.set('red')
l.pack()
rd1.pack()
rd2.pack()
rd3.pack()
w.mainloop()
