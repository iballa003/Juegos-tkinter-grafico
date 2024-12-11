from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
import os
import random




def menu():
  # Root
  root.geometry("512x512")
  root.resizable(False,False)
  root.title('Juegos')
  # Canvas
  img = ImageTk.PhotoImage(Image.open("./imagenes/canvasBackgound.jpg").resize((512, 512)))
  canvas = tk.Canvas(root, width=512, height=512)
  canvas.create_image(0, 0, anchor=tk.NW, image=img)
  canvas.pack()
  # Create the frame A and their content
  canvas.create_text(256, 60, text="Elige un juego", font=('Impact', -30), fill="white")




  # Create the frame B and their content
  button1 = ttk.Button(root, text="Piedra, papel o tijeras",command=juego1)
  canvas.create_window(256,200,anchor="center",window=button1)
  button2 = ttk.Button(root, text="Traduce del ingles")
  canvas.create_window(256,250,anchor="center",window=button2)
  button3 = ttk.Button(root, text="Adivina el número")
  canvas.create_window(256,300,anchor="center",window=button3)
  button4 = ttk.Button(root, text="Salir", command=root.destroy)
  canvas.create_window(256,350,anchor="center",window=button4)
  # Run mainloop
  root.mainloop()


def juego1():
  root.destroy()
  juego1root = Tk()
  juego1root.geometry("512x512")
  juego1root.title('Piedra, papel, tijeras')
  global canvas, player_option, computer_option

  canvas = Canvas(
    juego1root,
    bg="#FFFFFF",
    height=512,
    width=512,
    bd=0,
    highlightthickness=0,
    relief="ridge"
  )

  canvas.place(x=0, y=0)
  canvas.create_text(
    66.0,
    83.0,
    anchor="nw",
    text="Jugador",
    fill="#000000",
    font=("Inter", 20 * -1)
  )

  txt = canvas.create_text(
    221.0,
    318.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter", 13 * -1)
  )

  canvas.create_text(
    338.0,
    72.0,
    anchor="nw",
    text="Ordenador",
    fill="#000000",
    font=("Inter", 20 * -1)
  )

  image_image_1 = PhotoImage(
    file="./Imagenes/empty.png")
  player_option = canvas.create_image(
    105.0,
    194.0,
    image=image_image_1
  )

  image_image_2 = PhotoImage(
    file="./Imagenes/empty.png")
  computer_option = canvas.create_image(
    393.0,
    194.0,
    image=image_image_2
  )

  button_image_1 = PhotoImage(
    file="./Imagenes/button_1.png")
  button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: canvas.itemconfig(txt, text=jugar("Piedra")),
    relief="flat"
  )
  button_1.place(
    x=98.0,
    y=368.0,
    width=76.0,
    height=44.0
  )

  button_image_2 = PhotoImage(
    file="./Imagenes/button_2.png")
  button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: canvas.itemconfig(txt, text=jugar("Papel")),
    relief="flat"
  )
  button_2.place(
    x=218.0,
    y=368.0,
    width=76.0,
    height=44.0
  )

  button_image_3 = PhotoImage(
    file="./Imagenes/button_3.png")
  button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: canvas.itemconfig(txt, text=jugar("Tijeras")),
    relief="flat"
  )
  button_3.place(
    x=338.0,
    y=368.0,
    width=88.0,
    height=44.0
  )
  juego1root.mainloop()

def jugar(opcion_jugador):
  global newImagePlayer, newImageComputer
  opciones = ['Piedra', 'Papel', 'Tijeras']
  opcion_computadora = random.choice(opciones)
  newImagePlayer = PhotoImage(file="./Imagenes/" + opcion_jugador.lower() + ".png")
  newImageComputer = PhotoImage(file="./Imagenes/" + opcion_computadora.lower() + ".png")
  # Actualiza las imágenes en el canvas
  canvas.itemconfig(player_option, image=newImagePlayer)
  canvas.itemconfig(computer_option, image=newImageComputer)
  if opcion_jugador == opcion_computadora:
    resultado = "¡Empate!"
  elif (opcion_jugador == "Piedra" and opcion_computadora == "Tijeras") or \
          (opcion_jugador == "Papel" and opcion_computadora == "Piedra") or \
          (opcion_jugador == "Tijeras" and opcion_computadora == "Papel"):
    resultado = "¡Ganaste!"
  else:
    resultado = "¡Perdiste!"

  return resultado


def juego2():
  root.destroy()
  juego2 = Tk()
  juego2.geometry("512x512")
  juego2.title('Traduce del ingles')


def juego3():
  root.destroy()
  juego2 = Tk()
  juego2.geometry("512x512")
  juego2.title('Adivina')


root = Tk()
menu()
