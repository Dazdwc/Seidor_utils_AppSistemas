import os
from PIL import Image
import openpyxl
import imageio
from tkinter import messagebox


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
