# 🎨 Vista - Seidor Utils AppSistemas

Este módulo define la interfaz gráfica de usuario (GUI) de la aplicación. Me enfoqué en crear una experiencia intuitiva y organizada para gestionar actas, automatizar tareas y procesar documentos.

## 📌 Índice

- ⚙️ [Descripción General](#-descripción-general)
- 🏠 [MainView](#-mainview)
- 🔧 [HerramientasReplanteo](#-herramientasreplanteo)
- 🏗️ [HerramientasInstalacion](#-herramientasinstalacion)
- 🖼️ [FormateadorImagenView](#-formateadorimagenview)
- 📝 [CheckActaView](#-checkactaview)
- 💬 [CrearComentarioView](#-crearcomentarioview)
- ⌨️ [AutomatizarTeclasView](#-automatizarteclasview)

---

## ⚙️ Descripción General

La GUI de la aplicación está diseñada con **Tkinter** y proporciona una serie de herramientas interactivas para facilitar el trabajo con actas y automatización. Utilicé un diseño modular con ventanas independientes para cada funcionalidad.

Cada ventana tiene su propia configuración y estilo para mejorar la usabilidad. Además, los botones están organizados con colores pastel para hacer la navegación más clara y agradable.

---

## 🏠 MainView

**La ventana principal de la aplicación.**

🔹 **Funciones:**
- Proporciona acceso a todas las herramientas desde un menú central.
- Usa botones de colores pastel para diferenciar cada funcionalidad.
- Implementa una interfaz limpia y sin distracciones.

---

## 🔧 HerramientasReplanteo

🔹 **Funciones:**
- Permite firmar y comentar actas de replanteo.
- Genera relaciones entre alias y aulas.
- Diseño compacto y accesible para agilizar las tareas.

---

## 🏗️ HerramientasInstalacion

🔹 **Funciones:**
- Facilita la firma y comentarios en actas de instalación.
- Genera una relación entre alias y aulas en la instalación.
- Sigue la misma estructura de la herramienta de replanteo para mantener la coherencia visual.

---

## 🖼️ FormateadorImagenView

🔹 **Funciones:**
- Permite la conversión masiva de imágenes a formatos como **JPEG, PNG, BMP y TIFF**.
- Ofrece una barra de progreso para indicar el avance del proceso.
- Facilita la selección del directorio de trabajo.

---

## 📝 CheckActaView

🔹 **Funciones:**
- Valida las actas de Excel automáticamente.
- Firma documentos con un solo clic.
- Opción para validar y firmar simultáneamente.

---

## 💬 CrearComentarioView

🔹 **Funciones:**
- Genera comentarios automáticos en actas de replanteo e instalación.
- Ofrece opciones de personalización según el contexto del acta.
- Incluye casillas de selección para añadir detalles relevantes.

---

## ⌨️ AutomatizarTeclasView

🔹 **Funciones:**
- **Permite ejecutar macros automáticamente.**
- Muestra los datos en un árbol de visualización para facilitar la interacción.
- Simula la entrada de teclado para automatizar procesos sin necesidad de acceso a API.

💡 **Importante:** Esta funcionalidad fue una solución ingeniosa que implementé para evitar la dependencia de APIs restringidas por el cliente.

---

📩 **¿Dudas o sugerencias?** No dudes en abrir una issue en el repositorio.

