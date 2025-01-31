# 🖥️ Controlador - Seidor Utils AppSistemas

Este módulo contiene el **Controlador Principal** de la aplicación, el cual se encarga de gestionar la interacción entre la interfaz gráfica y la lógica del negocio. Implementa la conexión con distintos servicios y maneja los eventos generados por el usuario en la interfaz de usuario.

## 📌 Índice

- ⚙️ [Descripción General](#-descripción-general)
- 🔧 [Funciones del Controlador](#-funciones-del-controlador)
- 🚀 [Ejemplo de Uso](#-ejemplo-de-uso)
- 📂 [Estructura del Código](#-estructura-del-código)

---

## ⚙️ Descripción General

El **MainController** es la pieza central que coordina la ejecución de las herramientas dentro del sistema. Gestiona la carga de vistas, la ejecución de procesos y la comunicación entre los servicios que automatizan las tareas de conversión de imágenes, manipulación de archivos Excel y automatización de procesos repetitivos.

Principales responsabilidades:

- Cargar y gestionar las vistas de usuario.
- Interactuar con los servicios lógicos de la aplicación.
- Manejar eventos y llamadas desde la interfaz gráfica.
- Controlar el flujo de ejecución de las herramientas disponibles.

---

## 🔧 Funciones del Controlador

El **MainController** cuenta con múltiples métodos para interactuar con las diferentes herramientas de la aplicación:

- `run()`: Inicia la aplicación y muestra la ventana principal.
- `open_tool1() / open_tool2()`: Abre las herramientas de **Replanteo** e **Instalación**.
- `formatear_imagen()`: Activa la herramienta de **conversión de imágenes**.
- `check_acta()`: Ejecuta la validación de actas en archivos Excel.
- `comentarios()`: Inicia el módulo de **creación automática de comentarios**.
- `seleccionar_directorio()`: Permite al usuario elegir una carpeta en la interfaz.
- `convertir_imagenes()`: Ejecuta la conversión de imágenes en el directorio seleccionado.
- `validar_checks()`: Comprueba las casillas requeridas en un archivo Excel.
- `firmar_documento()`: Agrega una firma digital en las actas.
- `validar_y_firmar()`: Realiza validación y firma del documento en una sola acción.
- `relacion_nombre_aula_instalacion() / relacion_nombre_aula_replanteo()`: Extrae información de Excel y la procesa.
- `automatizar_teclas()`: Ejecuta automatizaciones de teclado para tareas repetitivas.
- `ejecutar_macro()`: Ejecuta macros predefinidas en la interfaz gráfica.

---

## 🚀 Ejemplo de Uso

Para iniciar la aplicación, simplemente ejecuta el controlador principal:

```python
from controlador import MainController

if __name__ == "__main__":
    controlador = MainController()
    controlador.run()
```

Este código cargará la interfaz gráfica y permitirá al usuario interactuar con todas las herramientas.

---

## 📂 Estructura del Código

```
Herramienta_Desarrollo/
│── controlador/
│   ├── MainController.py  # Controlador principal de la aplicación
│── modelo/
│   ├── ImageConverterService.py  # Servicio de conversión de imágenes
│   ├── ExcelService.py  # Manipulación de archivos Excel
│   ├── ExtractorService.py  # Extracción de datos
│   ├── AutomationService.py  # Automatización de teclas y procesos
│── vista/
│   ├── MainView.py  # Interfaz gráfica principal
│   ├── FormateadorImagenView.py  # Herramienta de conversión de imágenes
│   ├── CheckActaView.py  # Validación de actas en Excel
│   ├── CrearComentarioView.py  # Generación automática de comentarios
│   ├── AutomatizarTeclasView.py  # Automatización de teclado
```

---
