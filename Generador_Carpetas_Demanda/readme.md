# Generador de Imágenes desde Excel 🚀📊🖼️

## Descripción 🎯📑✨

Esta aplicación fue desarrollada para resolver un problema clave en un proyecto de instalación de paneles para la Generalitat. Los técnicos necesitaban una manera rápida y visual de conocer qué debía instalarse en cada centro sin tener que buscar manualmente en un extenso archivo Excel. Gracias a esta herramienta, se generan imágenes claras y organizadas con la información exacta extraída del Excel, lo que facilita enormemente el trabajo en campo y evita errores en la planificación. 📂📋🖼️

Esta aplicación permite procesar un archivo Excel y generar imágenes con tablas extraídas de sus datos. Se busca una coincidencia en la primera fila de cada columna y, cuando se encuentra, se extraen los valores correspondientes y se generan tablas en imágenes PNG. Las imágenes se guardan en carpetas organizadas según los valores encontrados en las primeras filas, facilitando su análisis y presentación de manera visual y accesible. 📂📋🖼️

## Características 🛠️📊✅

- Lee un archivo Excel y busca coincidencias en la primera fila de cada columna.
- Extrae y organiza los datos de la columna coincidente junto con una leyenda predefinida.
- Genera una imagen de tabla con los datos extraídos.
- Resalta en verde las celdas con valores mayores a 0.
- Guarda las imágenes en carpetas organizadas con nombres derivados de los valores de la primera y segunda fila de cada columna. 📂🎨🔍

## Requisitos ⚙️🐍💾

- Python 3.x
- Librerías necesarias:
  - `pandas`
  - `matplotlib`
  - `openpyxl` (para leer archivos Excel)

Puedes instalar las dependencias ejecutando:

```sh
pip install pandas matplotlib openpyxl
```

## Uso 📂📌🚀

1. Coloca el archivo Excel en el mismo directorio que el script o proporciona su ruta.
2. Modifica `file_path` con el nombre del archivo Excel.
3. Modifica `sheet_name` con el nombre de la hoja que deseas procesar.
4. Ejecuta el script en Python:
   ```sh
   python script.py
   ```
5. Se generarán carpetas con nombres basados en los valores de la primera y segunda fila de cada columna del Excel.
6. Dentro de cada carpeta se guardará una imagen PNG con los datos extraídos. 📊🖼️📂

## Ejemplo de Código 🖥️📜⚡

```python
file_path = 'test.xlsx'
sheet_name = 'Sheet1'  # Cambia esto según el nombre de tu hoja
process_excel(file_path, sheet_name)
```

## Estructura de Archivos 📁📑📂

```
/
├── script.py
├── test.xlsx
├── [valor1 valor2]/
│   ├── [search_value]_demanda.png
│   ├── ...
│
└── ...
```

Cada carpeta generada tendrá el formato `Codigo_centro Nombre_centro`, por ejemplo, `000000 COLEGIO_test`, y dentro se almacenarán las imágenes generadas, como `000000_demanda.png` o `123456_demanda.png`. 🖼️📁📊

## Notas 📝⚠️🔍

- Si el script no encuentra coincidencias en la primera fila de la columna, no generará ninguna imagen para esa columna.
- Los archivos generados tienen una resolución de 300 dpi para asegurar buena calidad visual.
- Se recomienda revisar los valores de entrada en el Excel para asegurar que coincidan con los criterios de búsqueda del script. ✅📊📂

## Autor ✍️👨‍💻🚀

Desarrollado por Daniel Zafra. Esta herramienta nació de la necesidad de agilizar el proceso de instalación de paneles en distintos centros, ofreciendo a los técnicos una manera sencilla y visual de acceder a la información clave sin perder tiempo buscando en hojas de cálculo extensas.

