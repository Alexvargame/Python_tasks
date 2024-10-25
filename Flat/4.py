from tkinter import * 


root = Tk()

b=Button(root, text="00")
b.grid(row=0, column=0)
b2=Button(root, text="11")
b2.grid(row=1, column=1)
b3=Button(root, text="22")
b3.grid(row=2, column=2)
b4=Button(root, text="33")
b4.grid(row=3, column=3)
b5=Button(root, text="44")
b5.grid(row=4, column=4)

def mouse(event):
    grid_info = event.widget.grid_info()
    print("row:", grid_info["row"], "column:", grid_info["column"])

root.bind("<Button-1>", mouse)

root.mainloop()
