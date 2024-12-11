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
  button2 = ttk.Button(root, text="Traduce del ingles", command=juego2)
  canvas.create_window(256,250,anchor="center",window=button2)
  button3 = ttk.Button(root, text="Adivina el número", command=juego3)
  canvas.create_window(256,300,anchor="center",window=button3)
  button4 = ttk.Button(root, text="Salir", command=root.destroy)
  canvas.create_window(256,350,anchor="center",window=button4)

  # Run mainloop
  root.mainloop()


def juego1():
  root.destroy()
  juego1root = Tk()
  juego1root.geometry("512x512")
  juego1root.resizable(False, False)
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
    command=lambda: canvas.itemconfig(txt, text=comprobar_resultado("Piedra")),
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
    command=lambda: canvas.itemconfig(txt, text=comprobar_resultado("Papel")),
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
    command=lambda: canvas.itemconfig(txt, text=comprobar_resultado("Tijeras")),
    relief="flat"
  )
  button_3.place(
    x=338.0,
    y=368.0,
    width=88.0,
    height=44.0
  )
  juego1root.mainloop()

def comprobar_resultado(opcion_jugador):
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

words = {"hello": "hola", "beach": "playa", "keyboard": "teclado", "computer": "ordenador", "mouse": "ratón",
          "wall": "pared","light": "luz", "window": "ventana", "chair": "silla","bag": "bolsa","table": "mesa", "cat": "gato", "shoes": "zapato",
          "hair": "pelo", "eyes": "ojos", "book": "libro","classroom": "clase","weather": "clima", "sun": "sol", "moon": "luna"}


def corregir_respuestas(palabras_mostradas,entradas):
  correctas = 0
  for i, key in enumerate(palabras_mostradas):
    respuesta = entradas[i].get().strip().lower()
    if respuesta == words[key]:
      correctas += 1
  resultado_label.config(text=f"Resultado: tienes {correctas} correctas.")


# Seleccionar 5 palabras aleatorias
def juego2():
  global resultado_label
  root.destroy()
  juego2 = Tk()
  juego2.geometry("512x512")
  juego2.resizable(False, False)
  juego2.title('Traduce del ingles')

  palabras_mostradas = random.sample(list(words.keys()), 5)

  frame = tk.Frame(juego2, width=512, height=512)
  frame.place(x=0, y=0)

  entradas = []
  for i, palabra in enumerate(palabras_mostradas):
    text_label = tk.Label(frame, text=palabra)
    text_label.place(x=160, y=55 + i * 40)

    entrada = tk.Entry(frame)
    entrada.place(x=220, y=55 + i * 40)
    entradas.append(entrada)

  ttk.Separator(frame).place(x=0, y=260, relwidth=1)

  button_corregir = Button(frame, text="Corregir", width=20, command=lambda: corregir_respuestas(palabras_mostradas,entradas))
  button_corregir.place(x=195, y=298)

  resultado_label = tk.Label(frame, text="Resultado: ")
  resultado_label.place(x=195, y=370)


  juego2.mainloop()

def juego3():
  root.destroy()
  juego3 = Tk()
  juego3.geometry("512x512")
  juego3.resizable(False, False)
  juego3.title('Adivina el número')

  frame = tk.Frame(juego3, width=512, height=512)
  frame.place(x=0, y=0)

  title_label = tk.Label(frame, text="Adivina el número entre 0 y 200",font=("Arial", 18))
  title_label.place(x=93, y=50)
  #ttk.Separator(frame).place(x=0, y=90, relwidth=1)

  text_label = tk.Label(frame, text="Número: ")
  text_label.place(x=190, y=200)

  entrada = tk.Entry(frame, width=6)
  entrada.place(x=250, y=200)
  ttk.Separator(frame).place(x=0, y=250, relwidth=1)

  try_label = tk.Label(frame, text="Te queda 4 intentos")
  try_label.place(x=190, y=270)
  ttk.Separator(frame).place(x=0, y=310, relwidth=1)

  button_corregir = Button(frame, text="Comprobar", width=20)
                           #command=lambda: corregir_respuestas(palabras_mostradas, entradas))
  button_corregir.place(x=195, y=330)

  juego3.mainloop()

root = Tk()
menu()
