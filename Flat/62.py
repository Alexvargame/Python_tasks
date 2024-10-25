from tkinter import*
import tkinter.ttk as ttk

def teget():
  global Toc_entry
  global btn2
  btn2.destroy()
  btn2 = Button(root, text = Toc_entry.get())
  #btn2.bind('<Button-1>', ???)
  btn2.pack()
  global children	
  children.destroy()

def Table_of_contents(event):
  global children
  children = Toplevel(root)
  children.title("Оглавление")
    
  global Toc_entry
  Toc_entry = Entry(children)
  Toc_entry.pack()

  Toc_e_btn = Button(children, text = "Принять", command=teget)
  Toc_e_btn.pack()

  
root = Tk()

root.title("Титульный лист")
#root.state('zoomed')

btn1 = Button(root, text = "Оглавление")
btn1.bind('<Button-1>', Table_of_contents)
btn1.pack()

global btn2
btn2 = Button(root, text = "Исполнитель")
#btn2.bind('<Button-1>', ???)
btn2.pack()

root.mainloop()
