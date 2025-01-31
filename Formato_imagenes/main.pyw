import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import imageio


class AplicacionConversorImagenes:
    def __init__(self, raiz):
        self.raiz = raiz
        self.directorio_seleccionado = ""
        self._configurar_interfaz()

    def _configurar_interfaz(self):
        self.raiz.title("Conversor de Imágenes")
        self.raiz.geometry("600x400")
        self.raiz.configure(bg="#f0f0f0")

        # Etiqueta de título
        self.etiqueta_titulo = tk.Label(self.raiz, text="Conversor de Imágenes", font=("Arial", 18), bg="#f0f0f0",
                                        fg="#333333")
        self.etiqueta_titulo.pack(pady=10)

        # Etiqueta de descripción
        self.etiqueta_descripcion = tk.Label(self.raiz, text="Seleccione un directorio para convertir imágenes",
                                             font=("Arial", 12), bg="#f0f0f0", fg="#666666")
        self.etiqueta_descripcion.pack(pady=10)

        # Barra de texto para mostrar el directorio seleccionado
        self.barra_directorio = tk.Entry(self.raiz, font=("Arial", 12), width=50, state='readonly')
        self.barra_directorio.pack(pady=10)

        # Botón para seleccionar directorio
        self.boton_seleccionar_directorio = tk.Button(self.raiz, text="Seleccionar Directorio",
                                                      command=self._seleccionar_directorio, font=("Arial", 12),
                                                      bg="#007BFF", fg="#ffffff", padx=10, pady=5)
        self.boton_seleccionar_directorio.pack(pady=10)

        # Etiqueta para seleccionar formato
        self.etiqueta_formato = tk.Label(self.raiz, text="Seleccione el formato de salida", font=("Arial", 12),
                                         bg="#f0f0f0", fg="#666666")
        self.etiqueta_formato.pack(pady=10)

        # Menú desplegable para seleccionar formato
        self.formato_seleccionado = tk.StringVar(value="JPEG")
        self.opciones_formato = ["JPEG", "PNG", "BMP", "TIFF"]
        self.menu_formato = tk.OptionMenu(self.raiz, self.formato_seleccionado, *self.opciones_formato)
        self.menu_formato.pack(pady=10)

        # Botón para convertir imágenes
        self.boton_convertir = tk.Button(self.raiz, text=f"¡Convertir a {self.formato_seleccionado.get()}!",
                                         command=self._convertir_imagenes, font=("Arial", 12), bg="#28a745",
                                         fg="#ffffff", padx=10, pady=5)
        self.boton_convertir.pack(pady=10)

        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(self.raiz, orient="horizontal", length=400, mode="determinate")
        self.barra_progreso.pack(pady=20)

        # Etiqueta de estado
        self.etiqueta_estado = tk.Label(self.raiz, text="", font=("Arial", 12), bg="#f0f0f0", fg="#666666")
        self.etiqueta_estado.pack(pady=10)

        # Actualiza el texto del botón cuando se cambia el formato
        self.formato_seleccionado.trace("w", self._actualizar_texto_boton)

    def _actualizar_texto_boton(self, *args):
        self.boton_convertir.config(text=f"¡Convertir a {self.formato_seleccionado.get()}!")

    def _seleccionar_directorio(self):
        self.directorio_seleccionado = filedialog.askdirectory()
        self.barra_directorio.configure(state='normal')
        self.barra_directorio.delete(0, tk.END)
        self.barra_directorio.insert(0, self.directorio_seleccionado)
        self.barra_directorio.configure(state='readonly')

    def _convertir_imagenes(self):
        if self.directorio_seleccionado:
            self._convertir_imagenes_en_directorio(self.directorio_seleccionado)
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un directorio primero.")

    def _convertir_imagenes_en_directorio(self, directorio):
        try:
            archivos = self._obtener_archivos_validos(directorio)
            total_archivos = len(archivos)
            self.barra_progreso["maximum"] = total_archivos

            for indice, archivo in enumerate(archivos, start=1):
                self._convertir_imagen(archivo)
                self.barra_progreso["value"] = indice
                self.raiz.update_idletasks()

            messagebox.showinfo("Completado", f"Se han convertido {total_archivos} imágenes exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al convertir imágenes: {e}")

    def _obtener_archivos_validos(self, directorio):
        archivos_validos = []
        for raiz, _, archivos in os.walk(directorio):
            for archivo in archivos:
                if archivo.lower().endswith(('.png', '.jpg', '.jpeg', '.heic', '.tiff', '.jfif', '.bmp')):
                    archivos_validos.append(os.path.join(raiz, archivo))
        return archivos_validos


    def _convertir_imagen(self, ruta_archivo):
        nombre_archivo, extension_archivo = os.path.splitext(ruta_archivo)
        formato_salida = self.formato_seleccionado.get().lower()
        ruta_salida = f"{nombre_archivo}.{formato_salida}"

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


def main():
    raiz = tk.Tk()
    AplicacionConversorImagenes(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    main()