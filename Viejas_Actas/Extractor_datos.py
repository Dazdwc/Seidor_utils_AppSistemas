import openpyxl
from openpyxl import Workbook
import os

# Función para solicitar el archivo Excel
def solicitar_archivo():
    archivo = input("Introduce la ruta del archivo Excel: ")
    if not os.path.exists(archivo):
        print("El archivo no existe. Inténtalo de nuevo.")
        return solicitar_archivo()
    return archivo

# Función para extraer la información de las celdas B2 y C4 de todas las hojas
def extraer_informacion(ruta_archivo):
    libro = openpyxl.load_workbook(ruta_archivo, data_only=True)
    datos = []
    hoja1 = libro.worksheets[0]
    codigo_centro = hoja1['C9'].value  # Extraer el título de la primera hoja (C9)
    nombre_centro = hoja1['f9'].value

    for hoja in libro.worksheets[1:]:
        C16 = hoja['C16'].value
        k17 = hoja['k17'].value
        datos.append((C16, k17))

    print(datos,nombre_centro ,codigo_centro)
    return datos, nombre_centro, codigo_centro

# Función para crear un nuevo archivo Excel con la información extraída
def crear_nuevo_archivo(datos,nombre_centro,codigo_centro):
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

    nuevo_libro.save(f"{codigo_centro}_{nombre_centro}.xlsx")
    print(f"Nuevo archivo creado como {codigo_centro}_{nombre_centro}.xlsx.")

def main():
    ruta_archivo = solicitar_archivo()
    datos,nombre_centro,codigo_centro = extraer_informacion(ruta_archivo)
    crear_nuevo_archivo(datos, nombre_centro, codigo_centro)

if __name__ == "__main__":
    main()



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
