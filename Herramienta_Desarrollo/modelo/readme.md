# 📊 Modelo - Seidor Utils AppSistemas

Este módulo contiene la lógica del negocio de la aplicación, proporcionando servicios para la manipulación de imágenes, procesamiento de archivos Excel y automatización de tareas.

## 📌 Índice

- ⚙️ [Descripción General](#-descripción-general)
- 🖼️ [ImageConverterService](#-imageconverterservice)
- 📑 [ExcelService](#-excelservice)
- 📋 [ExtractorService](#-extractorservice)
- ⌨️ [AutomationService](#-automationservice)
- 🔤 [StringService](#-stringservice)

---

## ⚙️ Descripción General

Desarrollé este módulo para implementar la funcionalidad principal de mi aplicación. Me enfoqué en:

- Conversión de imágenes en distintos formatos.
- Manipulación y procesamiento de datos en archivos Excel.
- Extracción de información relevante desde documentos.
- **Automatización de tareas mediante simulación de teclado**, una solución que ideé para sortear la falta de acceso a APIs proporcionadas por el cliente.

---

## 🖼️ ImageConverterService

Este servicio lo creé para la **conversión de imágenes** dentro de un directorio especificado.

🔹 **Funciones:**

- Buscar imágenes en un directorio.
- Convertir imágenes de formato HEIC, PNG, JPG y JPEG.
- Manejo de errores en la conversión.

⚙️ **Uso:**

```python
image_converter = ImageConverterService()
image_converter.convertir_imagenes_en_directorio("ruta/directorio", "PNG", barra_progreso, ventana)
```

---

## 📑 ExcelService

Este servicio lo diseñé para gestionar la manipulación de archivos **Excel** y automatizar la validación y firma de documentos.

🔹 **Funciones:**

- Completar casillas específicas de los archivos Excel.
- Firmar documentos automáticamente.
- Generar comentarios automáticos basados en condiciones predefinidas.

⚙️ **Uso:**

```python
excel_service = ExcelService()
excel_service.completar_check("archivo.xlsx", ["D28", "D29"], estado_ok=2)
```

---

## 📋 ExtractorService

Desarrollé este servicio para extraer información clave desde archivos Excel y estructurarla de manera más organizada.

🔹 **Funciones:**

- Solicitar archivos y directorios de destino.
- Extraer datos relevantes de las hojas de Excel.
- Crear un nuevo archivo Excel con la información estructurada.

⚙️ **Uso:**

```python
extractor_service = ExtractorService()
datos, nombre_centro, codigo_centro, tipo = extractor_service.extraer_informacion("archivo.xlsx", "instalación")
```

---

## ⌨️ AutomationService

**Este módulo nació como una solución ingeniosa que desarrollé cuando el cliente se negó a proporcionarme acceso a sus APIs.**

Dado que la API oficial estaba restringida, ideé una forma de **automatizar el ingreso de datos simulando la interacción humana con el teclado.**

🔹 **Funciones:**

- Simulación de escritura y navegación en la interfaz del cliente mediante **PyAutoGUI**.
- Extracción de datos desde archivos Excel.
- Automatización de macros para la gestión de aulas y equipos.

⚙️ **Uso:**

```python
automation_service = AutomationService()
automation_service.automatizar_teclas()
```

⚠️ **Nota:** Gracias a esta solución, logré completar el proyecto sin depender de integraciones bloqueadas por el cliente.

---

## 🔤 StringService

Este servicio auxiliar lo creé para manejar y limpiar datos de texto.

🔹 **Funciones:**

- Extraer solo los números de un string.

⚙️ **Uso:**

```python
StringService.solo_numeros("Metros de cable: 25m")  # Retorna "25"
```

---

📩 **¿Tienes preguntas o comentarios?** No dudes en abrir una issue en el repositorio.

