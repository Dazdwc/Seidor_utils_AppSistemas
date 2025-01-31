# Fusión de Archivos Excel 📊🔗

## Descripción 📄⚙️

Este script fue desarrollado para solucionar un problema de descuadre en la consolidación de información de múltiples archivos Excel. Permite combinar datos de distintas fuentes en un único archivo estructurado con los requisitos solicitados.

Gracias a esta herramienta, se automatiza la extracción y combinación de datos, evitando errores manuales y facilitando la organización de la información.

## Características ✨✅

- Permite seleccionar archivos Excel mediante una interfaz gráfica.
- Extrae y organiza información de múltiples archivos.
- Asocia datos de distintos archivos mediante coincidencias en los identificadores.
- Genera dos archivos Excel de salida con la información consolidada.
- Reduce el tiempo y el esfuerzo de procesar los datos manualmente.

## Requisitos ⚙️💻

- Python 3.x
- Librerías necesarias:
  - `pandas`
  - `tkinter`
  - `openpyxl`

Puedes instalar las dependencias ejecutando:

```sh
pip install pandas openpyxl
```

## Instalación 📦🔧

No es necesario realizar una instalación especial. Solo descarga el script y ejecútalo en un entorno con Python instalado.

## Uso 🚀📌

1. Ejecuta el script:
   ```sh
   python main.py
   ```
2. Selecciona los archivos requeridos mediante la interfaz gráfica.
3. Indica el directorio donde se guardarán los archivos generados.
4. Presiona el botón `Extraer` para iniciar el proceso.
5. Se generarán dos archivos Excel:
   - **Exportacion_masiva_para_telefonica.xlsx**
   - **Registro_exportacion_masiva_con_centro.xlsx**

Estos archivos contendrán la información procesada de forma estructurada.

## Estructura del Proyecto 📂🗂️

```
/
├── script_export_telefonica/
│   ├── main.py  # Script principal
├── Exportacion_masiva_para_telefonica.xlsx  # Archivo generado
├── Registro_exportacion_masiva_con_centro.xlsx  # Archivo generado
```

## Notas 📌🔍

- Si los archivos seleccionados no contienen los datos esperados, verifica que las columnas coincidan con los requisitos del script.
- Los archivos de salida se generan en el directorio especificado por el usuario.
- El script maneja errores comunes y muestra mensajes informativos en caso de problemas.

## Autor ✍️👨‍💻

Desarrollado por Daniel Zafra.

