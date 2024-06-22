import tkinter as tk
from tkinter import filedialog, messagebox
import openpyxl
import os
from tkinter import font as tkfont


def solicitar_archivo():
    archivo = filedialog.askopenfilename(
        title="Selecciona el archivo Excel",
        filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
    )
    return archivo


def solicitar_destino():
    # Obtener el directorio actual
    directorio_actual = os.getcwd()

    destino = filedialog.askdirectory(title="Selecciona la carpeta de destino", initialdir=directorio_actual)
    return destino


def main():
    # Creamos la instancia de la ventana principal
    root = tk.Tk()
    root.title("Extractor de Datos de Excel")
    root.geometry("800x600")  # Ancho x Alto

    # Configuración del fondo y otros parámetros
    root.configure(
        background='#f0f0f0',  # Color de fondo suave
        highlightbackground='#c0c0c0',  # Color del borde cuando no tiene foco
        highlightcolor='#80c0c0',  # Color del borde cuando tiene foco
        highlightthickness=1,  # Grosor del borde
        relief='flat'  # Estilo del borde discreto
    )

    # Configurar el icono de la ventana (asegúrate de tener un icono en la ruta especificada)
    try:
        root.iconbitmap('icono.ico')
    except:
        pass

    # Configuración de la fuente por defecto
    default_font = tkfont.nametofont("TkDefaultFont")
    default_font.configure(size=11)

    # Ejemplo de agregar widgets con un diseño profesional
    frame = tk.Frame(root, bg='#ffffff', padx=20, pady=20, relief='groove', bd=2)
    frame.pack(pady=20)

    label = tk.Label(frame, text="Bienvenido a Extracción de datos, Seleccione un modo:", font=("Helvetica", 16), bg='#ffffff')
    label.pack(pady=10)

    button = tk.Button(frame, text="Personalizado", font=("Helvetica", 12), bg='#007acc', fg='#ffffff', relief='raised')
    button.pack(pady=10)

    # Mostramos la ventana principal
    root.mainloop()


if __name__ == "__main__":
    main()