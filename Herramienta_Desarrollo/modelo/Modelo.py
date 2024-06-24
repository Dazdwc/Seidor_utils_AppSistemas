from PIL import Image
import openpyxl
import imageio
from tkinter import messagebox, filedialog
import os

from openpyxl.workbook import Workbook

# Diccionario de coherencia
coherencia_dict = {
    "SENSE ADEQUACIÓ": "NO APLICA",
    "KIT PROYECCIÓ": "CENTRE (SENSE TRASLLAT)",
    "PANEL INTERACTIU": "CENTRE (SENSE TRASLLAT)",
    "PISSARRA": "CENTRE (SENSE TRASLLAT)",
    "PROYECTOR": "CENTRE (SENSE TRASLLAT)",
    "ALTRES": "CENTRE (SENSE TRASLLAT)"
}
# Diccionario de mensajes
mensaje_dict = {
    "SENSE ADEQUACIÓ": "Resum del material a retirar: No es fa retirada perquè es monta suport amb rodes.",
    "OTROS": "La destinació de tots el elements a retirar és CENTRE (SENSE TRASLLAT)."
}
class ImageConverterService:
    def convertir_imagenes_en_directorio(self, directorio, formato_salida, barra_progreso, ventana):
        try:
            archivos = self._obtener_archivos_validos(directorio)
            total_archivos = len(archivos)
            barra_progreso["maximum"] = total_archivos

            for indice, archivo in enumerate(archivos, start=1):
                self._convertir_imagen(archivo, formato_salida)
                barra_progreso["value"] = indice
                ventana.update_idletasks()

            messagebox.showinfo("Completado", f"Se han convertido {total_archivos} imágenes exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir imágenes: {e}")

    def _obtener_archivos_validos(self, directorio):
        archivos_validos = []
        for raiz, _, archivos in os.walk(directorio):
            for archivo in archivos:
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.heic')):
                    archivos_validos.append(os.path.join(raiz, archivo))
        return archivos_validos

    def _convertir_imagen(self, ruta_archivo, formato_salida):
        nombre_archivo, extension_archivo = os.path.splitext(ruta_archivo)
        ruta_salida = f"{nombre_archivo}.{formato_salida.lower()}"

        try:
            if extension_archivo.lower() == '.heic':
                # Lee el número de fotogramas en la imagen HEIC
                num_fotogramas = imageio.get_reader(ruta_archivo).get_length()
                if num_fotogramas == 0:
                    messagebox.showwarning("Advertencia", "La imagen HEIC no contiene ningún fotograma.")
                    return
                imagen = imageio.imread(ruta_archivo)
                imagen = Image.fromarray(imagen)
                imagen = imagen.convert("RGB")
            else:
                imagen = Image.open(ruta_archivo)
                imagen = imagen.convert("RGB")

            imagen.save(ruta_salida, formato_salida.upper())

            if ruta_archivo != ruta_salida:
                os.remove(ruta_archivo)

        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir la imagen: {e}")


class ExcelService:
    def completar_check(self, ruta_archivo, celdas, estado_ok):
        try:
            libro = openpyxl.load_workbook(ruta_archivo)

            # Completar las hojas con estado_ok
            for nombre_hoja in libro.sheetnames[1:]:
                hoja = libro[nombre_hoja]
                for celda in celdas:
                    hoja[celda] = estado_ok

            # Guardar el libro de Excel
            libro.save(ruta_archivo)
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar el archivo de Excel: {e}")

    def firmar_acta(self, ruta_archivo, celdas):
        try:
            libro = openpyxl.load_workbook(ruta_archivo)
            datos_instalador = {
                "DNI": "45489700R",
                "NOM": "David Quiñonero",
                "CÀRREC": "Tècnic",
                "TELÈFON": "647999633"
            }

            for celda, valor in datos_instalador.items():
                libro.active[celdas[celda]] = valor

            # Guardar el libro de Excel
            libro.save(ruta_archivo)
        except Exception as e:
            messagebox.showerror("Error", f"Error al firmar el documento: {e}")
            return False

        return True

    def encontrar_celdas_para_firmar_en_acta(self, ruta_archivo):
        palabras_clave = ["DNI", "NOM", "CÀRREC", "TELÈFON"]
        resultado = {}
        try:
            # Cargar el archivo Excel
            libro = openpyxl.load_workbook(ruta_archivo)
            hoja = libro.active

            # Recorrer las filas de la columna F
            for fila in hoja.iter_rows(min_row=1, max_row=hoja.max_row, min_col=6, max_col=6):
                for celda in fila:
                    if celda.value in palabras_clave:
                        # Obtener la referencia de la celda en la columna G de la misma fila
                        referencia_celda = f"G{celda.row}"
                        resultado[celda.value] = referencia_celda

        except Exception as e:
            print(f"Ha ocurrido un error: {e}")
        print(resultado)
        return resultado

    def comentario_automatico(self, ruta_archivo, replanteo=False):
        # Cargar el archivo Excel
        wb = openpyxl.load_workbook(ruta_archivo)

        # Si replanteo es False, agregar los textos específicos en la primera hoja
        if not replanteo:
            print("Tendría que ser Instalación")
            ws = wb[wb.sheetnames[0]]
            for row in ws.iter_rows(min_col=1, max_col=1, min_row=1, max_row=ws.max_row):
                for cell in row:
                    if cell.value == "OBSERVACIONS":
                        ws.cell(row=cell.row + 1, column=1, value="Instal·lació de punt de xarxa:")
                        ws.cell(row=cell.row + 2, column=1, value="Instal·lació de punt elèctric:")
                        break

        # Iterar sobre las hojas a partir de la segunda
        for sheet_name in wb.sheetnames[1:]:
            ws = wb[sheet_name]

            # Buscar "TIPUS" en la columna A
            for row in ws.iter_rows(min_col=1, max_col=1, min_row=1, max_row=ws.max_row):
                for cell in row:
                    if cell.value == "TIPUS":
                        tipus_fila = cell.row
                        tipus_valor = ws.cell(row=tipus_fila + 1, column=1).value
                        if replanteo:
                            desti_valor = ws.cell(row=tipus_fila + 1, column=3).value
                        else:
                            desti_valor = ws.cell(row=tipus_fila + 1, column=2).value

                        # Verificar la coherencia
                        if tipus_valor in coherencia_dict and coherencia_dict[tipus_valor] == desti_valor:
                            coherente = True
                            mensaje = mensaje_dict.get(tipus_valor, mensaje_dict["OTROS"])
                        else:
                            coherente = False
                            mensaje = "Tipus no es correspon amb destinació, revisar a INDIC"

                        # Buscar "OBSERVACIONS" en la columna A y poner el mensaje
                        for obs_row in ws.iter_rows(min_col=1, max_col=1, min_row=1, max_row=ws.max_row):
                            for obs_cell in obs_row:
                                if obs_cell.value == "OBSERVACIONS":
                                    if coherente and tipus_valor == "SENSE ADEQUACIÓ":
                                        ws.cell(row=obs_cell.row + 4, column=1, value=mensaje)
                                    elif coherente:
                                        ws.cell(row=obs_cell.row + 5, column=1, value=mensaje_dict["OTROS"])
                                    else:
                                        ws.cell(row=obs_cell.row + 5, column=1, value=mensaje)
                                    break
                        break

        # Guardar los cambios en el archivo Excel
        wb.save(ruta_archivo)
        return True

class ExtractorService:

    def solicitar_archivo(self):

        archivo = filedialog.askopenfilename(
            title="Selecciona el archivo Excel",
            filetypes=(("Archivos Excel", "*.xlsx"), ("Todos los archivos", "*.*"))
        )

        return archivo

    # Función para solicitar la ruta de destino
    def solicitar_destino(self):

        destino = filedialog.askdirectory(
            title="Selecciona la carpeta de destino",
        )
        if destino:
            return destino
        else:
            return False

    # Función para extraer la información de las celdas B2 y C4 de todas las hojas
    def extraer_informacion(self, ruta_archivo, tipo):
        libro = openpyxl.load_workbook(ruta_archivo, data_only=True)
        datos = []
        hoja1 = libro.worksheets[0]

        if tipo == "instalación":
            codigo_centro = hoja1['C13'].value  # Extraer el título de la primera hoja
            nombre_centro = hoja1['F13'].value

            for hoja in libro.worksheets[1:]:
                C16 = hoja['C19'].value
                K17 = hoja['M19'].value
                datos.append((C16, K17))

            return datos, nombre_centro, codigo_centro
        if tipo == "replanteo":
            codigo_centro = hoja1['C9'].value  # Extraer el título de la primera hoja
            nombre_centro = hoja1['F9'].value

            for hoja in libro.worksheets[1:]:
                C16 = hoja['C16'].value
                K17 = hoja['K17'].value
                datos.append((C16, K17))

            return datos, nombre_centro, codigo_centro

    # Función para crear un nuevo archivo Excel con la información extraída
    def crear_nuevo_archivo(self, datos, nombre_centro, codigo_centro, ruta_destino, tipo):
        nuevo_libro = Workbook()
        nueva_hoja = nuevo_libro.active
        nueva_hoja.title = "Datos Extraídos"

        # Escribir los títulos en las celdas B2 y C2
        nueva_hoja['B2'] = "Aula"
        nueva_hoja['C2'] = "Alias"

        if nombre_centro:
            # Escribir los datos en las celdas B1 y C1
            for index, (b2, c4) in enumerate(datos, start=3):
                nueva_hoja[f'B{index}'] = b2
                nueva_hoja[f'C{index}'] = c4

            nombre_archivo = ""
            if tipo == "instalación":
                nombre_archivo = os.path.join(ruta_destino, f"{codigo_centro}_{nombre_centro}_relación_aula_instalación.xlsx")
            if tipo == "replanteo":
                nombre_archivo = os.path.join(ruta_destino, f"{codigo_centro}_{nombre_centro}_relación_aula_replanteo.xlsx")
            if nombre_archivo == "":
                messagebox.showwarning("Advertencia", "Error Inesperado.")
                return False
            nuevo_libro.save(nombre_archivo)
            messagebox.showinfo("Éxito", f"Nuevo archivo creado como {nombre_archivo}.")

            # Abrir el archivo recién creado
            try:
                os.startfile(nombre_archivo)
            except AttributeError:
                # Para sistemas no Windows
                os.system(f"open {nombre_archivo}")
        else:
            messagebox.showwarning("Advertencia", "No se encontraron datos para extraer.")
            return False
