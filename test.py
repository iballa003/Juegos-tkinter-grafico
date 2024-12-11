import tkinter as tk
import random


def jugar(opcion_jugador):
    opciones = ['Piedra', 'Papel', 'Tijeras']
    opcion_computadora = random.choice(opciones)

    if opcion_jugador == opcion_computadora:
        resultado = "¡Empate!"
    elif (opcion_jugador == "Piedra" and opcion_computadora == "Tijeras") or \
            (opcion_jugador == "Papel" and opcion_computadora == "Piedra") or \
            (opcion_jugador == "Tijeras" and opcion_computadora == "Papel"):
        resultado = "¡Ganaste!"
    else:
        resultado = "¡Perdiste!"

    label_resultado.config(text=f"Tú: {opcion_jugador} | Computadora: {opcion_computadora}\nResultado: {resultado}")


# Configuración principal de la ventana
root = tk.Tk()
root.title("Piedra, Papel o Tijeras")

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(root, text="Elige tu opción", font=("Arial", 14), padx=10, pady=10)
label_resultado.pack()

# Botones de elección
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_piedra = tk.Button(frame_botones, text="Piedra", font=("Arial", 12), width=10, command=lambda: jugar("Piedra"))
btn_piedra.grid(row=0, column=0, padx=5)

btn_papel = tk.Button(frame_botones, text="Papel", font=("Arial", 12), width=10, command=lambda: jugar("Papel"))
btn_papel.grid(row=0, column=1, padx=5)

btn_tijeras = tk.Button(frame_botones, text="Tijeras", font=("Arial", 12), width=10, command=lambda: jugar("Tijeras"))
btn_tijeras.grid(row=0, column=2, padx=5)

# Iniciar la ventana principal
root.mainloop()
