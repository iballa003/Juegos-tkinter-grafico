from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk

root = Tk()
root.geometry("512x512")
# two panes, each of which would get widgets gridded into it:

frameA = tk.Frame(root)
frameA.pack(side='top', fill=None)

label_center = Label(frameA, text="Piedra, papel o tijeras", justify="center", font=("Arial", 25) )
label_center.pack(pady=10, padx=10, anchor="w")

frameB = ttk.Frame(root)
frameB.pack(side='left', fill=None)

f1 = ttk.Labelframe(frameB, text='Elige', width=100, height=100)
f1.grid(column=0, row=0, padx=40, pady=40)
c1 = tk.Checkbutton(f1, text='Piedra', onvalue=1, offvalue=0).pack()
c2 = tk.Checkbutton(f1, text='Papel', onvalue=1, offvalue=0).pack()
c3 = tk.Checkbutton(f1, text='Tijeras', onvalue=1, offvalue=0).pack()

sep = ttk.Separator(frameB,orient='horizontal')
sep.grid(sticky="ew")

button1 = ttk.Button(frameB, text="jugar")
button1.grid(pady=10, padx=10)
root.mainloop()