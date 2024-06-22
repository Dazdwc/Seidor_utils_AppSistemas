import tkinter as tk
from tkinter import messagebox

def mi_funcion():
    messagebox.showinfo("Información", "¡El botón ha sido presionado!")
    # Aquí puedes agregar la función que desees ejecutar

# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz con Botón")
root.geometry("300x200")

# Crear un marco para centrar los elementos
frame = tk.Frame(root)
frame.pack(expand=True)

# Crear el botón
boton = tk.Button(frame, text="Haz clic aquí", command=mi_funcion, padx=10, pady=5, bg="#4CAF50", fg="white", relief="raised")
boton.pack(pady=20)

# Ejecutar la aplicación
root.mainloop()
