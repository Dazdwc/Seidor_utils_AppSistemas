import time

import pandas as pd
import matplotlib.pyplot as plt
import os


def generate_image(file_path, sheet_name, search_value, output_directory=None):
    # Leer la hoja completa para buscar el valor en la primera fila
    df_full = pd.read_excel(file_path, sheet_name=sheet_name)

    # Extraer la leyenda (B1:B16)
    legend = df_full.iloc[1:17, 0]  # Columna A1:A17

    # Buscar la columna donde coincida el valor en la primera fila (fila 0 en pandas)
    match_column = None
    for col in df_full.columns[1:]:  # Empezar desde la segunda columna (B)
        if df_full[col].iloc[0] == int(search_value):  # Verifica en la fila 2 (índice 1 en pandas)
            match_column = col
            break

    if match_column is None:
        print(f"No se encontró una coincidencia para el valor {search_value} en la segunda fila.")
        return

    # Extraer los datos coincidentes en la columna encontrada (filas 1 a 16)
    matching_data = df_full.loc[1:16, match_column]

    # Combinar la leyenda y los datos coincidentes
    combined_df = pd.DataFrame({
        'Codi Centre': legend,
        f'{search_value}': matching_data
    })

    # Crear la figura con una mayor resolución
    fig, ax = plt.subplots(figsize=(5, 8))  # Ajusta el tamaño de la figura según necesites

    # Ocultar los ejes
    ax.axis('tight')
    ax.axis('off')

    # Crear la tabla y añadirla a la figura
    table = ax.table(cellText=combined_df.values, colLabels=combined_df.columns, cellLoc='center', loc='center')

    # Ajustar el tamaño de la fuente de las celdas
    table.auto_set_font_size(True)
    table.set_fontsize(12)  # Ajusta el tamaño de la fuente según necesites
    table.scale(1, 1)  # Escalar la tabla para que se vea mejor

    # Pintar de verde las celdas que contienen un valor superior a 1 (excepto el título)
    for i in range(1, len(combined_df)):  # Empieza desde 1 para excluir la fila de títulos
        for j in range(1, len(combined_df.columns)):  # Empieza desde 1 para excluir la columna de leyenda
            value = combined_df.iat[i, j]
            if pd.notna(value) and value > 1:  # Verifica si la celda tiene un valor mayor a 1
                table[(i + 1, j)].set_facecolor('#98FB98')  # Color verde claro para las celdas con valor superior a 1

    # Determinar la ruta de guardado
    output_file_name = f'{search_value}_demanda.png'

    # Si no se especifica un directorio, guardar en el directorio actual
    if output_directory is None:
        output_directory = os.getcwd()

    # Combinar el directorio y el nombre del archivo
    output_file_path = os.path.join(output_directory, output_file_name)

    # Guardar la imagen en formato PNG con alta resolución
    plt.savefig(output_file_path, dpi=300, bbox_inches='tight')
    plt.close()

    print(
        f"La imagen se ha guardado como '{output_file_path}' con los datos de la leyenda y la columna coincidente con {search_value}.")


def process_excel(file_path, sheet_name):
    # Leer el archivo Excel
    df = pd.read_excel(file_path, sheet_name=sheet_name)

    # Iterar sobre las columnas desde la columna B
    for col in df.columns[1:]:
        # Obtener los valores de las celdas B1, B2, C1, C2, etc.
        value1 = str(df.iloc[0, df.columns.get_loc(col)])  # Valor de la primera fila (B1, C1, ...)
        value2 = str(df.iloc[1, df.columns.get_loc(col)])  # Valor de la segunda fila (B2, C2, ...)

        # Crear el nombre del directorio
        directory_name = f"{value1}_{value2}"
        directory_path = os.path.join(os.getcwd(), directory_name)

        # Crear el directorio si no existe
        if not os.path.exists(directory_path):
            os.makedirs(directory_path)

        # Llamar a la función generate_image con el valor de B1, C1, etc., y guardar la imagen en la carpeta creada
        generate_image(file_path, sheet_name, value1, directory_path)
        time.sleep(1)  # Esperar 1 segundo para evitar problemas con la generación de imágenes
        print(f"Imagen generada y guardada en {directory_path}")


# Ejemplo de uso
file_path = 'test.xlsx'
sheet_name = 'Sheet1'  # Cambia esto si tu hoja se llama de otra forma

process_excel(file_path, sheet_name)