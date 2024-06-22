import tkinter as tk
from tkinter import ttk, filedialog, messagebox


class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Herramientas Para Actas")
        self.geometry("330x400")
        self.resizable(False, False)

        # Estilo de la aplicación
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Helvetica', 12), padding=10)
        self.style.configure('TLabel', font=('Helvetica', 14, 'bold'))
        self.style.configure('TFrame', background='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        # Marco principal
        main_frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='TFrame')
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Título principal
        title_label = ttk.Label(main_frame, text="Herramientas Para Actas", style='TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Configurar la cuadrícula para centrar los botones
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.columnconfigure(3, weight=1)

        # Botones con colores pastel
        button_styles = [
            {'text': "Herramientas para replanteo", 'command': self.controller.open_tool1, 'background': "#AEC6CF"},
            {'text': "Herramientas para Instalación", 'command': self.controller.open_tool2, 'background': "#77DD77"},
            {'text': "Cambiar formato de imagen masivo", 'command': self.controller.formatear_imagen, 'background': "#FFB347"},
            {'text': "Completar y firmar", 'command': self.controller.check_acta, 'background': "#F231F2"}
        ]

        for i, style in enumerate(button_styles, start=1):
            button = tk.Button(main_frame, text=style['text'], command=style['command'],
                               bg=style['background'], fg='#000000', font=('Helvetica', 12), bd=0, relief='solid')
            button.grid(row=i, column=1, pady=10, padx=20, sticky='ew')

        # Expandir el espacio vacío para centrar los botones
        main_frame.grid_rowconfigure(4, weight=1)


class Tool1View(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Herramientas para replanteo")
        self.geometry("400x300")
        self.resizable(False, False)

        # Estilo de la nueva ventana
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', font=('Helvetica', 12))

        # Marco de la nueva ventana
        tool_frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='TFrame')
        tool_frame.pack(expand=True, fill='both')

        # Etiqueta con el mensaje
        label = ttk.Label(tool_frame, text="Bienvenido a las herramientas para replanteo.", style='TLabel', wraplength=350)
        label.pack(pady=20, padx=20)


class Tool2View(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Herramientas para Instalación")
        self.geometry("400x300")
        self.resizable(False, False)

        # Estilo de la nueva ventana
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', font=('Helvetica', 12))

        # Marco de la nueva ventana
        tool_frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='TFrame')
        tool_frame.pack(expand=True, fill='both')

        # Etiqueta con el mensaje
        label = ttk.Label(tool_frame, text="Bienvenido a las herramientas para instalación.", style='TLabel', wraplength=350)
        label.pack(pady=20, padx=20)


class FormateadorImagenView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Cambiar formato de imagen masivo")
        self.geometry("600x400")
        self.resizable(False, False)

        # Etiqueta de título
        self.etiqueta_titulo = tk.Label(self, text="Conversor de Imágenes", font=("Arial", 18), bg="#f0f0f0",
                                        fg="#333333")
        self.etiqueta_titulo.pack(pady=10)

        # Etiqueta de descripción
        self.etiqueta_descripcion = tk.Label(self, text="Seleccione un directorio para convertir imágenes",
                                             font=("Arial", 12), bg="#f0f0f0", fg="#666666")
        self.etiqueta_descripcion.pack(pady=10)

        # Barra de texto para mostrar el directorio seleccionado
        self.barra_directorio = tk.Entry(self, font=("Arial", 12), width=50, state='readonly')
        self.barra_directorio.pack(pady=10)

        # Botón para seleccionar directorio
        self.boton_seleccionar_directorio = tk.Button(self, text="Seleccionar Directorio",
                                                      command=self.controller.seleccionar_directorio, font=("Arial", 12),
                                                      bg="#007BFF", fg="#ffffff", padx=10, pady=5)
        self.boton_seleccionar_directorio.pack(pady=10)

        # Etiqueta para seleccionar formato
        self.etiqueta_formato = tk.Label(self, text="Seleccione el formato de salida", font=("Arial", 12),
                                         bg="#f0f0f0", fg="#666666")
        self.etiqueta_formato.pack(pady=10)

        # Menú desplegable para seleccionar formato
        self.formato_seleccionado = tk.StringVar(value="JPEG")
        self.opciones_formato = ["JPEG", "PNG", "BMP", "TIFF"]
        self.menu_formato = tk.OptionMenu(self, self.formato_seleccionado, *self.opciones_formato)
        self.menu_formato.pack(pady=10)

        # Botón para convertir imágenes
        self.boton_convertir = tk.Button(self, text=f"¡Convertir a {self.formato_seleccionado.get()}!",
                                         command=self.controller.convertir_imagenes, font=("Arial", 12), bg="#28a745",
                                         fg="#ffffff", padx=10, pady=5)
        self.boton_convertir.pack(pady=10)

        # Barra de progreso
        self.barra_progreso = ttk.Progressbar(self, orient="horizontal", length=400, mode="determinate")
        self.barra_progreso.pack(pady=20)

        # Etiqueta de estado
        self.etiqueta_estado = tk.Label(self, text="", font=("Arial", 12), bg="#f0f0f0", fg="#666666")
        self.etiqueta_estado.pack(pady=10)

        # Actualiza el texto del botón cuando se cambia el formato
        self.formato_seleccionado.trace("w", self.actualizar_texto_boton)

    def actualizar_texto_boton(self, *args):
        self.boton_convertir.config(text=f"¡Convertir a {self.formato_seleccionado.get()}!")


class CheckActaView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Completar y firmar")
        self.geometry("400x300")
        self.resizable(False, False)

        # Estilo de la nueva ventana
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', font=('Helvetica', 12))

        # Marco de la nueva ventana
        tool_frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='TFrame')
        tool_frame.pack(expand=True, fill='both')

        # Etiqueta con el mensaje
        label = ttk.Label(tool_frame, text="Seleccione un archivo para completar y firmar.", style='TLabel', wraplength=350)
        label.pack(pady=20, padx=20)

        # Botón para seleccionar archivo
        boton_seleccionar = tk.Button(tool_frame, text="Validar checks", command=self.controller.validar_checks)
        boton_seleccionar.pack(pady=20)

        # Botón para seleccionar archivo
        boton_seleccionar = tk.Button(tool_frame, text="Firmar documento", command=self.controller.firmar_documento)
        boton_seleccionar.pack(pady=20)

        # Botón para seleccionar archivo
        boton_seleccionar = tk.Button(tool_frame, text="Validar y firmar", command=self.controller.validar_y_firmar)
        boton_seleccionar.pack(pady=20)

        # Etiqueta para mostrar aviso
        self.label_aviso = tk.Label(tool_frame, text="", bg='#f0f0f0')
        self.label_aviso.pack(pady=10)