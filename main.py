from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import os
import random

#Root
root = Tk()
root.geometry("512x512")
root.title('Juegos')
#Canvas
img = ImageTk.PhotoImage(Image.open("./canvasBackgound.jpg").resize((512,512)))
canvas = tk.Canvas(root, width=512, height=512)
canvas.create_image(0, 0, anchor=tk.NW, image=img)
canvas.pack()
# canvas.pack(fill="both", expand=True)

#Pages
greet = Frame(root)
rockPaperScissorsGame = Frame(root)
translateGame = Frame(root)
guessGame = Frame(root)

#Change pages
def change_to_rockPaperScissorsGame():
   rockPaperScissorsGame.pack(fill='both', expand=1)
   greet.pack_forget()

#Create the frame A and their content
frameA = tk.Frame(root)
#frameA.configure(bg="red")
frameA.pack(side='top', fill=None)
frameA_window = canvas.create_window(256, 60, window=frameA) 


#label_center = Label(frameA, text="Elige un juego", justify="center")
#label_center.pack(pady=10, padx=10, anchor="w")
canvas.create_text(256, 60, text="Elige un juego",font=('Impact', -30), fill="white")

#Create the frame B and their content
frameB = ttk.Frame(root)
frameB.pack(side='top', fill=None)
frameB_window = canvas.create_window(256, 256, window=frameB)
sep = ttk.Separator(frameB,orient='horizontal')
sep.pack(fill='x')
button1 = ttk.Button(frameB, text="Piedra, papel o tijeras")
button1.pack(pady=10, padx=10)
button2 = ttk.Button(frameB, text="Traduce del ingles")
button2.pack(pady=10, padx=10)
button3 = ttk.Button(frameB, text="Adivina el número")
button3.pack(pady=10, padx=10)
button4 = ttk.Button(frameB, text="Salir", command=root.destroy)
button4.pack(pady=10, padx=10)

#Run mainloop
root.mainloop()