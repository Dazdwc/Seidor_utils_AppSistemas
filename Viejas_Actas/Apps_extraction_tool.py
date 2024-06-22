import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl
import os

def solicitar_archivo():
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo Excel",
        filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
    )
    return archivo

def solicitar_destino():
    destino = filedialog.askdirectory(title="Selecciona la carpeta de destino")
    return destino

def volver_al_menu_principal(root, frame):
    frame.pack_forget()
    mostrar_menu_principal(root)

def mostrar_menu_principal(root):
    menu_principal = tk.Frame(root)
    menu_principal.pack(expand=True, padx=20, pady=20)

    titulo = tk.Label(menu_principal, text="Selecciona el tipo de archivo a procesar", font=("Helvetica", 16))
    titulo.pack(pady=10)

    boton_replanteo = tk.Button(menu_principal, text="Acta Replanteo", command=lambda: procesar_archivo(root, "replanteo"))
    boton_replanteo.pack(pady=5)

    boton_instalacion = tk.Button(menu_principal, text="Acta Instalación", command=lambda: procesar_archivo(root, "instalacion"))
    boton_instalacion.pack(pady=5)

def procesar_archivo(root, tipo_archivo):
    menu_principal = root.nametowidget(root.winfo_children()[0])
    menu_principal.pack_forget()

    frame = tk.Frame(root)
    frame.pack(expand=True, padx=20, pady=20)

    titulo = tk.Label(frame, text=f"Procesar Archivo {tipo_archivo.capitalize()} Excel", font=("Helvetica", 16))
    titulo.pack(pady=10)

    descripcion = tk.Label(frame, text="""Este programa necesita un Excel de origen (Acta), 
    un destino donde generar el nuevo Excel 
    (Extracción de aulas) y darle a generar.""", font=("Helvetica", 9))
    descripcion.pack(pady=10)

    ruta_archivo_var = tk.StringVar()
    entrada_ruta = tk.Entry(frame, textvariable=ruta_archivo_var, width=40, state="readonly", font=("Helvetica", 10))
    entrada_ruta.pack(pady=5)

    boton_seleccionar = tk.Button(frame, text="Seleccionar Acta", command=lambda: solicitar_archivo())
    boton_seleccionar.pack(pady=10)

    ruta_destino_var = tk.StringVar()
    entrada_destino = tk.Entry(frame, textvariable=ruta_destino_var, width=40, state="readonly", font=("Helvetica", 10))
    entrada_destino.pack(pady=5)

    boton_destino = tk.Button(frame, text="Guardar Datos En...", command=lambda: solicitar_destino())
    boton_destino.pack(pady=10)

    boton_procesar = tk.Button(frame, text="¡Extraer la Información!", command=lambda: procesar(tipo_archivo, ruta_archivo_var, ruta_destino_var, frame))
    boton_procesar.pack(pady=10)

    boton_volver = tk.Button(frame, text="Volver al Menú Principal", command=lambda: volver_al_menu_principal(root, frame))
    boton_volver.pack(pady=10)

def procesar(tipo_archivo, ruta_archivo_var, ruta_destino_var, frame):
    ruta_archivo = ruta_archivo_var.get()
    if not ruta_archivo or not os.path.exists(ruta_archivo):
        messagebox.showerror("Error", "El archivo no existe. Inténtalo de nuevo.")
        return

    ruta_destino = ruta_destino_var.get()
    if not ruta_destino:
        messagebox.showerror("Error", "No se ha seleccionado ningún destino.")
        return

    datos, nombre_centro, codigo_centro = extraer_informacion(ruta_archivo, tipo_archivo)
    crear_nuevo_archivo(datos, nombre_centro, codigo_centro, ruta_destino)

def extraer_informacion(archivo, tipo_archivo):
    libro = openpyxl.load_workbook(archivo, data_only=True)
    datos = []
    hoja1 = libro.worksheets[0]

    if tipo_archivo == "replanteo":
        codigo_celda = 'C9'
        nombre_celda = 'F9'
        primera_celda = 'C16'
        segunda_celda = 'K17'
    elif tipo_archivo == "instalacion":
        codigo_celda = 'C13'
        nombre_celda = 'F13'
        primera_celda = 'C19'
        segunda_celda = 'M19'

    codigo_centro = hoja1[codigo_celda].value
    nombre_centro = hoja1[nombre_celda].value

    for hoja in libro.worksheets[1:]:
        datos.append((hoja[primera_celda].value, hoja[segunda_celda].value))

    return datos, nombre_centro, codigo_centro

def crear_nuevo_archivo(datos, nombre_centro, codigo_centro, destino):
    nuevo_libro = openpyxl.Workbook()
    nueva_hoja = nuevo_libro.active
    nueva_hoja.title = "Datos Extraídos"

    nueva_hoja['B2'] = "Aula"
    nueva_hoja['C2'] = "Alias"

    for index, (b2, c4) in enumerate(datos, start=3):
        nueva_hoja[f'B{index}'] = b2
        nueva_hoja[f'C{index}'] = c4

    nombre_archivo = os.path.join(destino, f"{codigo_centro}_{nombre_centro}.xlsx")
    nuevo_libro.save(nombre_archivo)
    messagebox.showinfo("Éxito", f"Nuevo archivo creado como {nombre_archivo}.")

    try:
        os.startfile(nombre_archivo)
    except AttributeError:
        os.system(f"open {nombre_archivo}")

def main():
    root = tk.Tk()
    root.title("Procesamiento de Archivos Excel")
    root.geometry("600x400")
    root.resizable(False, False)

    mostrar_menu_principal(root)

    root.mainloop()

if __name__ == "__main__":
    main()