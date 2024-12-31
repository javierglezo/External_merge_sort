import heapq
import os
import csv


def external_sort_sales(input_file, output_file, chunk_size):
    """
    Ordena un archivo grande de registros de ventas por importe utilizando External Sorting.

    :param input_file: Ruta del archivo CSV de entrada.
    :param output_file: Ruta del archivo CSV de salida ordenado.
    :param chunk_size: Número de registros que caben en memoria (bloque).
    """
    temp_files = []

    # Paso 1: Dividir el archivo en bloques ordenados
    with open(input_file, 'r') as infile:
        csv_reader = csv.reader(infile)
        header = next(csv_reader)  # Leer la cabecera
        while True:
            lines = list(next(csv_reader, None) for _ in range(chunk_size))
            lines = [line for line in lines if line]  # Filtrar líneas vacías
            if not lines:
                break

            # Ordenar el bloque en memoria por el segundo campo (importe)
            lines.sort(key=lambda x: int(x[1]))

            # Guardar el bloque en un archivo temporal
            temp_file_name = f"temp_sales_{len(temp_files)}.csv"
            with open(temp_file_name, 'w', newline='') as temp_file:
                writer = csv.writer(temp_file)
                writer.writerows(lines)
            temp_files.append(temp_file_name)

    # Paso 2: Mezclar los bloques ordenados
    with open(output_file, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        csv_writer.writerow(header)  # Escribir la cabecera al archivo de salida

        # Abrir los archivos temporales
        open_files = [open(file, 'r') for file in temp_files]
        csv_readers = [csv.reader(f) for f in open_files]

        # Usar un heap para mezclar los archivos
        heap = []
        for idx, reader in enumerate(csv_readers):
            row = next(reader, None)
            if row:
                heapq.heappush(heap, (int(row[1]), idx, row))

        while heap:
            _, idx, row = heapq.heappop(heap)
            csv_writer.writerow(row)  # Escribir al archivo de salida
            next_row = next(csv_readers[idx], None)
            if next_row:
                heapq.heappush(heap, (int(next_row[1]), idx, next_row))

    # Paso 3: Limpiar archivos temporales
    for f in open_files:
        f.close()
    for file in temp_files:
        os.remove(file)


# Ejemplo de uso
if __name__ == "__main__":
    # Crear un archivo de ejemplo
    input_file = "ventas.csv"
    output_file = "ventas_ordenadas.csv"
    chunk_size = 3  # Registros por bloque

    # Datos de ejemplo
    with open(input_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Fecha", "Importe"])
        writer.writerows([
            ["2024-01-01", "500"],
            ["2024-01-02", "300"],
            ["2024-01-03", "400"],
            ["2024-01-04", "200"],
            ["2024-01-05", "100"],
            ["2024-01-06", "700"],
            ["2024-01-07", "600"],
        ])

    # Ejecutar el algoritmo de External Sorting
    external_sort_sales(input_file, output_file, chunk_size)

    # Mostrar el resultado
    with open(output_file, 'r') as f:
        print("Archivo ordenado por importe:")
        print(f.read())
