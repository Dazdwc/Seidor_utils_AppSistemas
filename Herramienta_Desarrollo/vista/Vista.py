import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.scrolledtext import ScrolledText

tamano_main = ""
tamano_herramientas = ""


class MainView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Herramientas Para Actas")
        self.geometry(tamano_main)
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
        title_label = ttk.Label(main_frame, text="Herramientas para actas", style='TLabel')
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))

        # Configurar la cuadrícula para centrar los botones
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.columnconfigure(3, weight=1)

        # Botones con colores pastel
        button_styles = [
            {'text': "Herramientas para Replanteo", 'command': self.controller.open_tool1, 'background': "#c8e78b"},
            {'text': "Herramientas para Instalación", 'command': self.controller.open_tool2, 'background': "#fcccdb"},
            {'text': "Cambiar formato de imagen masivo", 'command': self.controller.formatear_imagen, 'background': "#ffda9e"},
            #{'text': "Completar y firmar", 'command': self.controller.check_acta, 'background': "#F231F2"},
            {'text': "Automatizar Teclas", 'command': self.controller.automatizar_teclas, 'background': "#ffcaaf"},
            {'text': "Generar Comentario acta", 'command': self.controller.comentarios, 'background': "#d8edf9"}
        ]

        for i, style in enumerate(button_styles, start=1):
            button = tk.Button(main_frame, text=style['text'], command=style['command'],
                               bg=style['background'], fg='#000000', font=('Helvetica', 12), bd=0, relief='solid')
            button.grid(row=i, column=1, pady=10, padx=20, sticky='ew')

        # Expandir el espacio vacío para centrar los botones
        main_frame.grid_rowconfigure(4, weight=1)


class HerramientasReplanteo(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Herramientas para replanteo")
        self.geometry(tamano_herramientas)
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

        boton_para_todo = tk.Button(
            tool_frame,
            text="Firmar y Comentar Replanteo 📝",
            command=lambda: self.controller.boton_para_todo(replanteo=True),
            bg="#89a850",  # Color de fondo
            fg="#f8f9fa",  # Color de texto blanco
            font=('Helvetica', 14, 'bold'),  # Fuente más grande y en negrita
        )
        boton_para_todo.pack(pady=20)

        separator = ttk.Separator(tool_frame, orient='horizontal')
        separator.pack(fill='x', pady=10)

        boton_extractor = tk.Button(
            tool_frame,
            text="Relacion Alias/Aula",
            command=self.controller.relacion_nombre_aula_replanteo,
            bg="#def8a9",  # Color de fondo
        )
        boton_extractor.pack(pady=20)

        # Botón para seleccionar archivo
        # boton_seleccionar = tk.Button(
        #     tool_frame,
        #     text="Firmar documento",
        #     command=self.controller.firmar_documento
        # )
        # boton_seleccionar.pack(pady=20)
        #
        # boton_comentario = tk.Button(
        #     tool_frame,
        #     text="Comentarios automáticos",
        #     command=lambda: self.controller.comentarios_automatiocs_replanteo(True)
        # )
        # boton_comentario.pack(pady=20)


class HerramientasInstalacion(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Herramientas para Instalación")
        self.geometry(tamano_herramientas)
        self.resizable(False, False)

        # Estilo de la nueva ventana
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', font=('Helvetica', 12))

        # Marco de la nueva ventana
        tool_frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='TFrame')
        tool_frame.pack(expand=True, fill='both')

        # Etiqueta con el mensaje
        label = ttk.Label(tool_frame, text="Bienvenido a las herramientas para Instalación.", style='TLabel', wraplength=350)
        label.pack(pady=20, padx=20)

        boton_para_todo = tk.Button(
            tool_frame,
            text="Firmar y Comentar Instalación 📝",
            command=lambda: self.controller.boton_para_todo(False),
            bg="#e690af",  # Color de fondo
            fg="#f8f9fa",  # Color de texto blanco
            font=('Helvetica', 14, 'bold'),  # Fuente más grande y en negrita
        )
        boton_para_todo.pack(pady=20)

        boton_extractor = tk.Button(
            tool_frame,
            text="Relacion Alias/Aula",
            command=self.controller.relacion_nombre_aula_instalacion,
            bg="#fdc9d9",  # Color de fondo
        )
        boton_extractor.pack(pady=20)

        #boton_seleccionar = tk.Button(
        #    tool_frame,
        #    text="Validar y firmar",
        #    command=self.controller.validar_y_firmar)
        #boton_seleccionar.pack(pady=20)

        #boton_comentario = tk.Button(
        #    tool_frame,
        #    text="Comentarios automáticos",
        #    command=lambda: self.controller.comentarios_automatiocs_replanteo(False)
        #)
        #boton_comentario.pack(pady=20)


class FormateadorImagenView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Cambiar formato de imagen masivo")
        self.geometry(tamano_herramientas)
        self.resizable(False, False)
        self.directorio_seleccionado = None  # Inicializar el atributo aquí

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
        self.geometry(tamano_herramientas)
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


class CrearComentarioView(tk.Toplevel):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Generar Comentario")
        self.geometry("")
        self.resizable(True, True)

        # Estilo de la nueva ventana
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#f0f0f0')
        self.style.configure('TLabel', font=('Helvetica', 12))

        # Marco de la nueva ventana
        tool_frame = ttk.Frame(self, padding=(20, 10, 20, 10), style='TFrame')
        tool_frame.pack(expand=True, fill='both')

        # Variables para el tipo de acta
        self.tipo_acta = tk.StringVar(value="replanteo")

        # Botones de radio para seleccionar el tipo de acta
        acta_frame = ttk.Frame(tool_frame, style='TFrame')
        acta_frame.pack(anchor='w', pady=5)

        #ttk.Radiobutton(acta_frame, text="Acta de replanteo", variable=self.tipo_acta, value="replanteo",
                        #style='TRadiobutton').pack(side='left')
        #ttk.Radiobutton(acta_frame, text="Acta de instalación", variable=self.tipo_acta, value="instalacion",
                        #style='TRadiobutton').pack(side='left')

        # Variable para la opción "soporte con rodes"
        self.soporte_con_ruedas = tk.BooleanVar()
        self.soporte_con_ruedas_cb = tk.Checkbutton(tool_frame, text="Soporte con rodes",
                                                    variable=self.soporte_con_ruedas, bg='#f0f0f0',
                                                    font=('Helvetica', 12), command=self.toggle_soporte_con_ruedas)
        self.soporte_con_ruedas_cb.pack(anchor='w', pady=2)

        # Posibles comentarios adicionales
        self.extra_comments = {
            "Cambio de soporte de ruedas a pared fijo": "Canvi a suport fixe de paret (ja preautoritzat) a petició del centre.",
            "Cambio de soporte de pared a con patas": "Canvi a suport amb potes per paret inconsistent (pladur o altres materials no segurs).",
            "Cambio de soporte por imposibilidad de instalación (elementos sanitarios o aulas modulares)": "Canvi de suport a rodes per impossibilitat tècnica a l'aula (motiu: radiador, pica, mòdul...)."
        }
        self.extra_comment_vars = {comment: tk.BooleanVar() for comment in self.extra_comments.keys()}
        self.extra_checkbuttons = {}

        for comment, var in self.extra_comment_vars.items():
            cb = tk.Checkbutton(tool_frame, text=comment, variable=var, bg='#f0f0f0', font=('Helvetica', 12),
                                command=self.toggle_extra_comments)
            cb.pack(anchor='w', pady=2)
            self.extra_checkbuttons[comment] = cb

            if comment == "Cambio de soporte por imposibilidad de instalación (elementos sanitarios o aulas modulares)":
                self.motivo_entry = ttk.Entry(tool_frame, state='disabled')
                self.motivo_entry.pack(anchor='w', padx=20, pady=2)

        # Elementos a seleccionar
        self.items = {
            "Kit de projecció (projector i caixa de connexions)": tk.BooleanVar(),
            "Altaveus": tk.BooleanVar(),
            "PDI": tk.BooleanVar(),
            "Panell digital antic": tk.BooleanVar(),
            "Pissarra blanca": tk.BooleanVar(),
            "Pissarra verda de guix": tk.BooleanVar(),
            "Suro": tk.BooleanVar(),
            "Mobiliari genèric (prestatges, armaris, taula...)": tk.BooleanVar()
        }

        # Crear checkboxes y campos de entrada para cada elemento
        self.checkbuttons = []
        self.entries = {}
        self.pantalla_enrollable_var = tk.BooleanVar()

        for item, var in self.items.items():
            cb = tk.Checkbutton(tool_frame, text=item, variable=var, bg='#f0f0f0', font=('Helvetica', 12),
                                command=self.toggle_entries)
            cb.pack(anchor='w', pady=2)
            self.checkbuttons.append(cb)

            if item == "Kit de projecció (projector i caixa de connexions)":
                self.pantalla_cb = tk.Checkbutton(tool_frame, text="Pantalla enrotllable",
                                                  variable=self.pantalla_enrollable_var, bg='#f0f0f0',
                                                  font=('Helvetica', 12))
                self.pantalla_cb.pack(anchor='w', padx=20, pady=2)
                self.pantalla_cb.config(state='disabled')

                entry_frame = ttk.Frame(tool_frame, style='TFrame')
                entry_frame.pack(anchor='w', pady=2, padx=20)

                ttk.Label(entry_frame, text="Sace:", style='TLabel').pack(side='left')
                sace_entry = ttk.Entry(entry_frame, state='disabled')
                sace_entry.pack(side='left', padx=5)

                ttk.Label(entry_frame, text="SN:", style='TLabel').pack(side='left')
                sn_entry = ttk.Entry(entry_frame, state='disabled')
                sn_entry.pack(side='left', padx=5)

                self.entries[item] = (sace_entry, sn_entry)

            elif item in ["Altaveus", "PDI", "Panell digital antic"]:
                entry_frame = ttk.Frame(tool_frame, style='TFrame')
                entry_frame.pack(anchor='w', pady=2, padx=20)

                ttk.Label(entry_frame, text="Sace:", style='TLabel').pack(side='left')
                sace_entry = ttk.Entry(entry_frame, state='disabled')
                sace_entry.pack(side='left', padx=5)

                ttk.Label(entry_frame, text="SN:", style='TLabel').pack(side='left')
                sn_entry = ttk.Entry(entry_frame, state='disabled')
                sn_entry.pack(side='left', padx=5)

                self.entries[item] = (sace_entry, sn_entry)

        # Botón para generar el comentario
        generate_button = ttk.Button(tool_frame, text="Generar Comentario", command=self.generate_comment)
        generate_button.pack(pady=10)

        # Etiqueta para mostrar aviso
        self.label_aviso = tk.Label(tool_frame, text="", bg='#f0f0f0', fg='green', font=('Helvetica', 12))
        self.label_aviso.pack(pady=5)

        # Area de texto con scroll para mostrar el comentario
        self.text_area = ScrolledText(tool_frame, wrap=tk.WORD, width=50, height=10, font=('Helvetica', 12))
        self.text_area.pack(pady=10, expand=True, fill='both')

        self.update_idletasks()  # Actualiza la ventana para ajustar el tamaño al contenido

    def toggle_soporte_con_ruedas(self):
        if self.soporte_con_ruedas.get():
            for cb in self.checkbuttons:
                cb.config(state='disabled')
            for entries in self.entries.values():
                for entry in entries:
                    entry.config(state='disabled')
            self.pantalla_cb.config(state='disabled')
        else:
            for cb in self.checkbuttons:
                cb.config(state='normal')
            self.toggle_entries()

    def toggle_entries(self):
        for item, (sace_entry, sn_entry) in self.entries.items():
            if self.items[item].get():
                sace_entry.config(state='normal')
                sn_entry.config(state='normal')
                if item == "Kit de projecció (projector i caixa de connexions)":
                    self.pantalla_cb.config(state='normal')
            else:
                sace_entry.config(state='disabled')
                sn_entry.config(state='disabled')
                if item == "Kit de projecció (projector i caixa de connexions)":
                    self.pantalla_cb.config(state='disabled')

    def toggle_extra_comments(self):
        selected_var = None
        for comment, var in self.extra_comment_vars.items():
            if var.get():
                selected_var = var
                if comment == "Cambio de soporte por imposibilidad de instalación (elementos sanitarios o aulas modulares)":
                    self.motivo_entry.config(state='normal')
                else:
                    self.motivo_entry.config(state='disabled')
                    self.motivo_entry.delete(0, tk.END)
            else:
                self.extra_checkbuttons[comment].config(state='normal')

        if selected_var:
            for comment, var in self.extra_comment_vars.items():
                if var != selected_var:
                    self.extra_checkbuttons[comment].config(state='disabled')

    def generate_comment(self):
        acta_text = "Resum del material a retirar:" if self.tipo_acta.get() == "replanteo" else "Resum del material retirat:"

        if self.soporte_con_ruedas.get():
            comment1 = f"{acta_text} No es fa retirada perquè es monta suport amb rodes."
            comment2 = ""
        else:
            selected_items = []
            for item, var in self.items.items():
                if var.get():
                    sace, sn = self.entries.get(item, (None, None))
                    sace_text = f" Sace( {sace.get()})" if sace and sace.get() else ""
                    sn_text = f" SN( {sn.get()})" if sn and sn.get() else ""
                    item_text = f"{item}{sace_text}{sn_text}"
                    if item == "Kit de projecció (projector i caixa de connexions)" and self.pantalla_enrollable_var.get():
                        item_text = "Kit de projecció (projector, pantalla enrotllable i caixa de connexions)"
                    selected_items.append(item_text)
            if selected_items:
                comment1 = f"{acta_text} " + ", ".join(selected_items) + "."
                comment2 = "La destinació de tots els elements a retirar és CENTRE (SENSE TRASLLAT)."
            else:
                comment1 = "No hay elementos seleccionados."
                comment2 = ""

        # Añadir comentarios adicionales si están seleccionados
        additional_comments = []
        for comment, var in self.extra_comment_vars.items():
            if var.get():
                if comment == "Cambio de soporte por imposibilidad de instalación (elementos sanitarios o aulas modulares)":
                    motivo = self.motivo_entry.get().strip()
                    additional_comments.append(
                        f"{self.extra_comments[comment]} {motivo}" if motivo else self.extra_comments[comment])
                else:
                    additional_comments.append(self.extra_comments[comment])

        full_comment = comment1 + "\n\n" + comment2 + "\n\n" + "\n\n".join(additional_comments)
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, full_comment)

        # Copiar solo la parte del resumen del material
        self.clipboard_clear()
        self.clipboard_append(comment1)

        # Mostrar aviso de copiado
        self.label_aviso.config(text="Resumen del material copiado al portapapeles")


class AutomatizarTeclasView(tk.Toplevel):
    def __init__(self, controller, datos):
        super().__init__()
        self.controller = controller
        self.datos = datos
        self.title("Automatizar Teclas")
        self.geometry(tamano_herramientas)
        self.resizable(True, True)

        self.create_widgets()

    def create_widgets(self):
        columns = [
            'codigo_centro', 'nombre_centro', 'codigo_nombre_centro', 'nombre_aula',
            'numero_edificio', 'planta', 'etapa', 'edificio_con_modulos',
            'panel', 'tipo_soporte', 'el_soporte_es_diferente', 'tipo_pared',
            'presa_electrica', 'red', 'Activar Macro', 'Realizada'
        ]

        self.tree = ttk.Treeview(self, columns=columns, show='headings')
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)

        for dato in self.datos:
            values = [dato[col] for col in columns[:-2]]  # Exclude 'Activar Macro' and 'Realizada' columns
            values.append("▶️")
            values.append("")  # Initially, the 'Realizada' column is empty
            self.tree.insert('', 'end', values=values)

        self.tree.pack(expand=True, fill=tk.BOTH)

        # Añadir un botón de Play
        self.tree.bind('<Double-1>', self.on_double_click)

    def on_double_click(self, event):
        item = self.tree.selection()[0]
        values = self.tree.item(item, 'values')
        dato = {col: values[idx] for idx, col in enumerate(self.tree['columns'][:-2])}
        self.controller.ejecutar_macro(dato, item, self)


def show_error_message(message):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showerror("Error de Licencia", message)
    root.destroy()