import tkinter as tk

window = tk.Tk()







for i in range(5):
  
    frame = tk.Frame(
            master=window,
            borderwidth=1
            )
    l=['Ко-во комнат', 'Этаж','Этажность','Планировка','Цена']
    frame.grid(row=1, column=i, padx=5, pady=5, sticky="e")
    label = tk.Label(master=frame, text=l[i])
    label.pack(padx=5, pady=5)
    frame.grid(row=2, column=i, padx=5, pady=5, sticky="e")
    label1 = tk.Label(master=frame, text='4') 
    label1.pack(padx=5, pady=5)


    #for j in range [5]:

     #   frame = tk.Frame(
      #      master=window,
       #     borderwidth=1
         #   )
        #
      #  
       # frm_buttons = tk.Frame()
        # frm_buttons.grid(row=j, column =0, ipadx=5, ipady=5, sticky="e")
    
    
#for i in range(8):
 #   frame = tk.Frame(
  #          master=window,
   #         borderwidth=1
    #        )
   # frame.grid(,column=2,padx=5, pady=5) 
    # entry = tk.Entry(master=frame,width=100)
    #entry.pack(padx=5, pady=5)

frm_buttons = tk.Frame()
frm_buttons.grid(row=9, ipadx=5, ipady=5, sticky="e")

btn_submit = tk.Button(master=frm_buttons, text="Отправить")
btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

button_clear = tk.Button(master=frm_buttons, text="Очистить")
button_clear.pack(side=tk.RIGHT, ipadx=10)


window.mainloop()
