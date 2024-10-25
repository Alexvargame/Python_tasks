from tkinter import *

w=Tk()
w.title("W")
w.geometry("250x150")


f=Frame(w)
f.pack()
l=Label(f, text="Hi")
l.pack()
l1=Label(f, image=PhotoImage(file="C:\Python36-32\ex\Book\in.png"))
print(PhotoImage(file="C:\Python36-32\ex\Book\in.png"))
l1.place(x=30, y=40)
b=Button(f,text="Ok", command=w.destroy)
b.pack()

w.mainloop()
