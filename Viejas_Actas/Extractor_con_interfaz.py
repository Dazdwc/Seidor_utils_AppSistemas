import openpyxl
from openpyxl import Workbook
import os
import tkinter as tk
from tkinter import messagebox, filedialog

# Variables globales para almacenar la ruta del archivo y del destino
ruta_archivo = None
ruta_destino = None

# Función para solicitar el archivo Excel
def solicitar_archivo():
    global ruta_archivo
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo Excel",
        filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
    )
    if not archivo or not os.path.exists(archivo):
        messagebox.showerror("Error", "El archivo no existe. Inténtalo de nuevo.")
        return
    ruta_archivo = archivo
    ruta_archivo_var.set(archivo)

# Función para solicitar la ruta de destino
def solicitar_destino():
    global ruta_destino
    destino = filedialog.askdirectory(
        title="Selecciona la carpeta de destino"
    )
    if destino:
        ruta_destino = destino
        ruta_destino_var.set(destino)

# Función para extraer la información de las celdas B2 y C4 de todas las hojas
def extraer_informacion(ruta_archivo):
    libro = openpyxl.load_workbook(ruta_archivo, data_only=True)
    datos = []
    hoja1 = libro.worksheets[0]
    codigo_centro = hoja1['C9'].value  # Extraer el título de la primera hoja (C9)
    nombre_centro = hoja1['F9'].value

    for hoja in libro.worksheets[1:]:
        C16 = hoja['C16'].value
        K17 = hoja['K17'].value
        datos.append((C16, K17))

    return datos, nombre_centro, codigo_centro

# Función para crear un nuevo archivo Excel con la información extraída
def crear_nuevo_archivo(datos, nombre_centro, codigo_centro, ruta_destino):
    nuevo_libro = Workbook()
    nueva_hoja = nuevo_libro.active
    nueva_hoja.title = "Datos Extraídos"

    # Escribir los títulos en las celdas B2 y C2
    nueva_hoja['B2'] = "Aula"
    nueva_hoja['C2'] = "Alias"

    # Escribir los datos en las celdas B1 y C1
    for index, (b2, c4) in enumerate(datos, start=3):
        nueva_hoja[f'B{index}'] = b2
        nueva_hoja[f'C{index}'] = c4

    nombre_archivo = os.path.join(ruta_destino, f"{codigo_centro}_{nombre_centro}.xlsx")
    nuevo_libro.save(nombre_archivo)
    messagebox.showinfo("Éxito", f"Nuevo archivo creado como {nombre_archivo}.")

    # Abrir el archivo recién creado
    try:
        os.startfile(nombre_archivo)
    except AttributeError:
        # Para sistemas no Windows
        os.system(f"open {nombre_archivo}")

def procesar_archivo():
    if not ruta_archivo:
        messagebox.showerror("Error", "No se ha seleccionado ningún archivo de origen.")
        return
    if not ruta_destino:
        messagebox.showerror("Error", "No se ha seleccionado ningún destino.")
        return
    datos, nombre_centro, codigo_centro = extraer_informacion(ruta_archivo)
    crear_nuevo_archivo(datos, nombre_centro, codigo_centro, ruta_destino)

# Crear la ventana principal
root = tk.Tk()
root.title("Relación de Nombre Aulas/Alias")
root.geometry("600x600")
root.resizable(False, False)
root.configure(bg="#f0f0f0")

# Crear un marco para centrar los elementos
frame = tk.Frame(root, bg="#f0f0f0")
frame.pack(expand=True, padx=20, pady=20)

# Etiqueta de título
titulo = tk.Label(frame, text="Procesar Archivo Excel", font=("Helvetica", 16), bg="#f0f0f0")
titulo.pack(pady=10)

# Etiqueta y campo de texto para la ruta del archivo
descripcion = tk.Label(frame, text="""Este programa necesita un Excel de origen (Acta), 
un destino donde generar el nuevo Excel 
(Extracción de aulas) y darle a generar.""", font=("Helvetica", 9), bg="#f0f0f0")
descripcion.pack(pady=10)

# Campo para mostrar la ruta del archivo
ruta_archivo_var = tk.StringVar()
entrada_ruta = tk.Entry(frame, textvariable=ruta_archivo_var, width=40, state="readonly", font=("Helvetica", 10))
entrada_ruta.pack(pady=5)

# Botón para seleccionar archivo
boton_seleccionar = tk.Button(frame, text="1.Selecciona un Acta", command=solicitar_archivo, padx=10, pady=5, bg="#4CAF50", fg="white", relief="raised")
boton_seleccionar.pack(pady=10)

# Campo para mostrar la ruta de destino
ruta_destino_var = tk.StringVar()
entrada_destino = tk.Entry(frame, textvariable=ruta_destino_var, width=40, state="readonly", font=("Helvetica", 10))
entrada_destino.pack(pady=5)

# Botón para seleccionar destino
boton_destino = tk.Button(frame, text="2.Guardar Datos En...", command=solicitar_destino, padx=10, pady=5, bg="#4CAF50", fg="white", relief="raised")
boton_destino.pack(pady=10)


# Botón para procesar el archivo
boton_procesar = tk.Button(frame, text="¡Extrae la información!", command=procesar_archivo, padx=10, pady=5, bg="#4CAF50", fg="white", relief="raised")
boton_procesar.pack(pady=10)

# Etiqueta de autor
autor = tk.Label(frame, text="Creador por: Daniel Zafra", font=("Helvetica", 9), bg="#f0f0f0")
autor.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()