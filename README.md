# External Sorting: Ordenamiento de Archivos Grandes

Este proyecto implementa un algoritmo de **External Sorting** para ordenar grandes archivos de datos que no caben en memoria. Utiliza un enfoque basado en dividir los datos en bloques manejables, ordenarlos por separado y luego fusionarlos en un archivo final ordenado.

## **Características**

- Divide los datos en bloques de tamaño configurable.
- Ordena cada bloque en memoria utilizando Python.
- Fusiona múltiples bloques ordenados utilizando un heap (*k-way merge*).
- Soporta archivos CSV como formato de entrada y salida.
- Escalable para grandes conjuntos de datos.

## **Requisitos del Sistema**

- Python 3.7 o superior.
- Biblioteca estándar de Python (no requiere dependencias adicionales).

## **Estructura del Proyecto**

```plaintext
├── external_sort_sales.py    # Script principal con la implementación
├── ventas.csv                # Archivo de entrada de ejemplo
├── ventas_ordenadas.csv      # Archivo de salida ordenado
└── README.md                 # Este archivo
```

## **Uso**

### **1. Crear el Archivo de Entrada**
El archivo de entrada debe estar en formato CSV y contener al menos dos columnas:
- Una columna identificadora (e.g., Fecha, Nombre).
- Una columna numérica que será utilizada como clave de ordenamiento.

Ejemplo:

```csv
Fecha,Importe
2024-01-01,500
2024-01-02,300
2024-01-03,400
2024-01-04,200
2024-01-05,100
```

### **2. Configurar y Ejecutar el Script**
Ejecuta el script principal `external_sort_sales.py` para ordenar el archivo:

```bash
python external_sort_sales.py
```

Por defecto:
- El archivo de entrada es `ventas.csv`.
- El archivo de salida es `ventas_ordenadas.csv`.
- El tamaño del bloque es de 3 registros.

### **3. Consultar el Archivo de Salida**
El archivo ordenado se genera con los registros ordenados por la columna numérica:

```csv
Fecha,Importe
2024-01-05,100
2024-01-04,200
2024-01-02,300
2024-01-03,400
2024-01-01,500
```

## **Parámetros Personalizables**

Puedes ajustar los siguientes parámetros en el archivo `external_sort_sales.py`:
- **Archivo de entrada:** Cambia `input_file` por la ruta a tu archivo.
- **Archivo de salida:** Cambia `output_file` por la ruta deseada.
- **Tamaño del bloque:** Ajusta `chunk_size` según la capacidad de tu memoria.

Ejemplo de configuración personalizada:

```python
input_file = "grandes_ventas.csv"
output_file = "grandes_ventas_ordenadas.csv"
chunk_size = 1000
```

## **Cómo Funciona el Algoritmo**

1. **División de Bloques:** Se lee el archivo de entrada en bloques del tamaño especificado.
2. **Ordenamiento de Bloques:** Cada bloque se ordena en memoria y se guarda en un archivo temporal.
3. **Mezcla:** Los bloques ordenados se fusionan eficientemente utilizando un heap.
4. **Generación del Archivo Final:** El resultado final se escribe en el archivo de salida.

## **Casos de Uso**

Este algoritmo es ideal para:
- Ordenar registros financieros.
- Procesar grandes bases de datos.
- Ordenar datos de logs en sistemas distribuidos.
- Cualquier tarea que implique datos que no caben en memoria.


