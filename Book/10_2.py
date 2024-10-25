from tkinter import *
def movie(event):
    x=event.x
    y=event.y
    print( x,y)

w=Tk()
w.title("W")
w.geometry("250x150")

def movie(event):
    x=event.x
    y=event.y
    print(x,y)
f=Frame(w)
f.pack()
l=Label(f, text="Hi")
l.pack()
l1=Label(f, text="1")

l1.pack()
l1.bind("<B1-Motion>", movie)
b=Button(f,text="Ok", command=w.destroy)
b.pack()

w.mainloop()
