import pandas as pd
from tkinter import Tk, filedialog, Button, Label, Entry, StringVar, Frame, BOTH
from tkinter.messagebox import showinfo


def seleccionar_archivo(var, titulo):
    archivo = filedialog.askopenfilename(title=titulo, filetypes=[("Excel files", "*.xlsx;*.xls")])
    var.set(archivo)


def seleccionar_directorio(var, titulo):
    directorio = filedialog.askdirectory(title=titulo)
    var.set(directorio)


def procesar_archivos():
    primer_archivo_path = id_peticion_var.get()
    segundo_archivo_path = saces_var.get()
    directorio_guardado = directorio_var.get()

    if not primer_archivo_path or not segundo_archivo_path or not directorio_guardado:
        showinfo("Error", "Por favor seleccione ambos archivos y el directorio de guardado.")
        return

    try:
        print(f"Leyendo el primer archivo: {primer_archivo_path}")
        # Leer el primer archivo Excel incluyendo todas las filas
        primer_archivo = pd.read_excel(primer_archivo_path)
        print("Primer archivo leído con éxito.")
        print(primer_archivo.head())

        id_centro_dict = dict(zip(primer_archivo.iloc[:, 0], primer_archivo.iloc[:, 1]))
        print("Diccionario de ID de petición a código de centro creado:")
        print(id_centro_dict)

        print(f"Leyendo el segundo archivo: {segundo_archivo_path}")
        # Leer el segundo archivo Excel incluyendo todas las filas
        segundo_archivo = pd.read_excel(segundo_archivo_path)
        segundo_archivo = segundo_archivo.iloc[:, [0, 1, 2, 3]]
        print("Segundo archivo leído con éxito.")
        print(segundo_archivo.head())

        # Crear nuevas listas de filas para los nuevos archivos
        nuevas_filas_1 = []
        nuevas_filas_2 = []

        for index, row in segundo_archivo.iterrows():
            serial_number = row[0]
            sace = row[1]
            codigo_centro = row[2]
            nombre_centro = row[3]
            id_peticion = None

            if codigo_centro in id_centro_dict.values():
                id_peticion = list(id_centro_dict.keys())[list(id_centro_dict.values()).index(codigo_centro)]

            nuevas_filas_1.append([serial_number, sace, 78, 0, id_peticion])
            nuevas_filas_2.append([serial_number, sace, 78, 0, id_peticion, codigo_centro, nombre_centro])

        print("Datos preparados para nuevos archivos.")

        # Crear DataFrames con las nuevas filas
        nueva_df_1 = pd.DataFrame(nuevas_filas_1, columns=['NumeroSerie', 'SACE_IMEI', 'IDEstatTracking', 'IDMaqueta',
                                                           'ID de petición'])
        nueva_df_2 = pd.DataFrame(nuevas_filas_2,
                                  columns=['NumeroSerie', 'SACE_IMEI', 'IDEstatTracking', 'IDMaqueta', 'ID de petición',
                                           'Codigo centro', 'Nombre Centro'])

        print("DataFrames creados:")
        print(nueva_df_1.head())
        print(nueva_df_2.head())

        # Guardar los nuevos archivos Excel
        nueva_df_1.to_excel(f"{directorio_guardado}/Exportacion_masiva_para_telefonica.xlsx", index=False,
                            engine='openpyxl')
        nueva_df_2.to_excel(f"{directorio_guardado}/Registro_exportacion_masiva_con_centro.xlsx", index=False,
                            engine='openpyxl')

        print("Archivos Excel guardados.")
        showinfo("Éxito", "Los archivos se han creado exitosamente.")
    except Exception as e:
        showinfo("Error", f"Se produjo un error: {e}")
        print(f"Error: {e}")


# Crear la interfaz gráfica
ventana = Tk()
ventana.title("Procesador de Archivos Excel")
ventana.geometry("500x300")

frame = Frame(ventana, pady=20)
frame.pack(fill=BOTH, expand=True)

id_peticion_var = StringVar()
saces_var = StringVar()
directorio_var = StringVar()

# Selector del primer archivo
Label(frame, text="Archivo de ID de Petición:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
Entry(frame, textvariable=id_peticion_var, width=40).grid(row=0, column=1, padx=10, pady=10)
Button(frame, text="ID_peticion",
       command=lambda: seleccionar_archivo(id_peticion_var, "Seleccione el primer archivo Excel")).grid(row=0, column=2,
                                                                                                        padx=10,
                                                                                                        pady=10)

# Selector del segundo archivo
Label(frame, text="Archivo de SACES:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
Entry(frame, textvariable=saces_var, width=40).grid(row=1, column=1, padx=10, pady=10)
Button(frame, text="Saces", command=lambda: seleccionar_archivo(saces_var, "Seleccione el segundo archivo Excel")).grid(
    row=1, column=2, padx=10, pady=10)

# Selector del directorio de guardado
Label(frame, text="Directorio de Guardado:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
Entry(frame, textvariable=directorio_var, width=40).grid(row=2, column=1, padx=10, pady=10)
Button(frame, text="Seleccionar Directorio",
       command=lambda: seleccionar_directorio(directorio_var, "Seleccione el directorio de guardado")).grid(row=2,
                                                                                                            column=2,
                                                                                                            padx=10,
                                                                                                            pady=10)

# Botón para extraer la información
Button(frame, text="Extraer", command=procesar_archivos, bg="green", fg="white").grid(row=3, columnspan=3, pady=20)

ventana.mainloop()
