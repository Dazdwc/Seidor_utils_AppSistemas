import time
import tkinter as tk
from AppSistemas.Herramienta_Desarrollo.modelo.Modelo import ImageConverterService, ExcelService, ExtractorService, AutomationService
from AppSistemas.Herramienta_Desarrollo.vista.Vista import MainView, HerramientasReplanteo, HerramientasInstalacion, \
    FormateadorImagenView, CheckActaView, CrearComentarioView, AutomatizarTeclasView
from tkinter import filedialog, messagebox

class MainController:
    def __init__(self):
        self.image_converter_service = ImageConverterService()
        self.excel_service = ExcelService()
        self.extractor_service = ExtractorService()
        self.automation_service = AutomationService()
        self.main_view = MainView(self)

        self.tool1_view = None
        self.tool2_view = None
        self.formateador_imagen_view = None
        self.check_acta_view = None
        self.firmar_documento_view = None
        self.validar_y_firmar_view = None
        self.check_comentarios_view = None
        self.automatizar_teclas_view = None

    def run(self):
        self.main_view.mainloop()

    def open_tool1(self):
        if self.tool1_view is None or not self.tool1_view.winfo_exists():
            self.tool1_view = HerramientasReplanteo(self)
        else:
            self.tool1_view.lift()

    def open_tool2(self):
        if self.tool2_view is None or not self.tool2_view.winfo_exists():
            self.tool2_view = HerramientasInstalacion(self)
        else:
            self.tool2_view.lift()

    def formatear_imagen(self):
        if self.formateador_imagen_view is None or not self.formateador_imagen_view.winfo_exists():
            self.formateador_imagen_view = FormateadorImagenView(self)
        else:
            self.formateador_imagen_view.lift()

    def check_acta(self):
        if self.check_acta_view is None or not self.check_acta_view.winfo_exists():
            self.check_acta_view = CheckActaView(self)
        else:
            self.check_acta_view.lift()
    def comentarios(self):
        if self.check_comentarios_view is None or not self.check_comentarios_view.winfo_exists():
            self.check_comentarios_view = CrearComentarioView(self)
        else:
            self.check_comentarios_view.lift()

    def seleccionar_directorio(self):
        directorio_seleccionado = filedialog.askdirectory()
        if self.formateador_imagen_view and directorio_seleccionado:
            self.formateador_imagen_view.barra_directorio.configure(state='normal')
            self.formateador_imagen_view.barra_directorio.delete(0, tk.END)
            self.formateador_imagen_view.barra_directorio.insert(0, directorio_seleccionado)
            self.formateador_imagen_view.barra_directorio.configure(state='readonly')
            self.formateador_imagen_view.directorio_seleccionado = directorio_seleccionado  # Actualiza el atributo

    def convertir_imagenes(self):
        if self.formateador_imagen_view and hasattr(self.formateador_imagen_view, 'directorio_seleccionado') and self.formateador_imagen_view.directorio_seleccionado:
            self.image_converter_service.convertir_imagenes_en_directorio(
                self.formateador_imagen_view.directorio_seleccionado,
                self.formateador_imagen_view.formato_seleccionado.get(),
                self.formateador_imagen_view.barra_progreso,
                self.formateador_imagen_view
            )
        else:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un directorio primero.")

    def validar_checks(self, ruta_archivo=None):
        if not ruta_archivo:
            ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo Excel")
        estado_ok = 2
        celdas = ['D28', 'D29', 'D31', 'D32', 'I28', 'I29', 'O28', 'O29']

        if ruta_archivo:
            self.excel_service.completar_check(ruta_archivo, celdas, estado_ok)
            if self.check_acta_view:
                self.check_acta_view.label_aviso.config(text="¡Proceso completado con éxito! 😊")
        return True

    def firmar_documento(self, ruta_archivo=None):
        importa_ruta = True
        if not ruta_archivo:
            ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo Excel")
            importa_ruta = False

        if ruta_archivo:
            celdas = self.excel_service.encontrar_celdas_para_firmar_en_acta(ruta_archivo)
            firmado = self.excel_service.firmar_acta(ruta_archivo, celdas)

            if firmado and not importa_ruta:
                messagebox.showinfo(message="¡Documento firmado! 📝")
            elif importa_ruta:
                return True
            else:
                messagebox.showwarning(message="Error al firmar el documento. 😞")
        return True

    def validar_y_firmar(self):
        ruta_archivo = filedialog.askopenfilename(title="Selecciona un archivo Excel")

        if ruta_archivo:
            if self.validar_checks(ruta_archivo) and self.firmar_documento(ruta_archivo):
                messagebox.showinfo("Información", "📝 ¡Documento validado y firmado con éxito! 📝")
            else:
                messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo Excel primero.")


    def relacion_nombre_aula_instalacion(self):
        ruta_destino = False
        ruta_archivo = ExtractorService.solicitar_archivo(self)
        tipo = "instalación"
        if ruta_archivo:
            ruta_destino = ExtractorService.solicitar_destino(self)
            if ruta_destino:
                datos, nombre_centro, codigo_centro, tipo = ExtractorService.extraer_informacion(self, ruta_archivo, tipo)
                if datos:
                    ExtractorService.crear_nuevo_archivo(self, datos, nombre_centro, codigo_centro, ruta_destino, tipo)
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos para extraer.")
        if not ruta_archivo or not ruta_destino:
            messagebox.showerror("Error", "El archivo no existe. Inténtalo de nuevo.")
            return

    def relacion_nombre_aula_replanteo(self):
        ruta_destino = False
        ruta_archivo = ExtractorService.solicitar_archivo(self)
        tipo = "replanteo"
        if ruta_archivo:
            ruta_destino = ExtractorService.solicitar_destino(self)
            if ruta_destino:
                datos, nombre_centro, codigo_centro, tipo = ExtractorService.extraer_informacion(self, ruta_archivo, tipo)
                if datos:
                    ExtractorService.crear_nuevo_archivo(self, datos, nombre_centro, codigo_centro, ruta_destino, tipo)
                else:
                    messagebox.showwarning("Advertencia", "No se encontraron datos para extraer.")
        if not ruta_archivo or not ruta_destino:
            messagebox.showerror("Error", "El archivo no existe. Inténtalo de nuevo.")
            return

    def comentarios_automatiocs_replanteo(self, replanteo=False):
        if replanteo:
            ruta_archivo = filedialog.askopenfilename(title="Selecciona un acta de replanteo")
        else:
            ruta_archivo = filedialog.askopenfilename(title="Selecciona un acta de instalación")

        if ruta_archivo:
            comentado = self.excel_service.comentario_automatico(ruta_archivo, replanteo)
            if comentado:
                messagebox.showinfo("Información", "📝 Comentarios Puestos con éxito 📝")
            else:
                messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo Excel primero.")
        return ruta_archivo, True

    def boton_para_todo(self, replanteo=False):
        if replanteo:
            ruta, ok = self.comentarios_automatiocs_replanteo(True)

            if self.firmar_documento(ruta) and ok:
                messagebox.showinfo("Información", "📝 ¡Documento validado y firmado con éxito! 📝")
            else:
                messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo Excel primero.")

        else:
            ruta, ok = self.comentarios_automatiocs_replanteo(False)
            if self.validar_checks(ruta) and self.firmar_documento(ruta) and ok:
                messagebox.showinfo("Información", "📝 ¡Documento validado y firmado con éxito! 📝")
            else:
                messagebox.showwarning("Advertencia", "Por favor, seleccione un archivo Excel primero.")

    def automatizar_teclas(self):
        datos = self.automation_service.automatizar_teclas()
        if datos:
            self.automatizar_teclas_view = AutomatizarTeclasView(self, datos)
            self.automatizar_teclas_view.lift()

    def ejecutar_macro(self, dato, item_id, view):
        if view.tree.set(item_id, 'Realizada') == '✓':
            respuesta = messagebox.askyesno(
                "Confirmación",
                "La macro ya se ha ejecutado para esta fila. ¿Desea volver a aplicarla?"
            )
            if not respuesta:
                return

        aviso = messagebox.showinfo(
            "Aviso",
            "Tienes 5 segundos para situarte en la pantalla adecuada después de aceptar este mensaje."
        )
        time.sleep(2)  # Pausa de 5 segundos para que el usuario se sitúe en la pantalla

        self.automation_service.procesar_datos(dato)
        # Actualizar la vista para mostrar que la macro se ha ejecutado
        view.tree.set(item_id, 'Realizada', '✓')