from tkinter import *
class CheckButton:
      def __init__(self, master, a, i, j):
        self.var = BooleanVar()
        self.a=a
        self.var.set(self.a)
        self.i = i
        self.j = j
        self.cb = Checkbutton(
            master, variable=self.var,
            onvalue=1, offvalue=0)
        self.cb.grid(row=i, column=j)
