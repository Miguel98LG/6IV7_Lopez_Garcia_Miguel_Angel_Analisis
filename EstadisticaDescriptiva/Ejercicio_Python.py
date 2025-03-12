import pandas as pd
<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np
=======

import matplotlib.pyplot as plt
>>>>>>> 3b75450b61d7f278a0a0dc83bc5f6570ae1acda5

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

media_median_house_value = df["median_house_value"].mean()
<<<<<<< HEAD
print("\nMedia de median_house_value:", media_median_house_value)

mediana_median_house_value = df["median_house_value"].median()
print("Mediana de median_house_value:", mediana_median_house_value)

moda_median_house_value = df["median_house_value"].mode()[0]
print("Moda de median_house_value:", moda_median_house_value)

rango_median_house_value = df["median_house_value"].max() - df["median_house_value"].min()
print("Rango de median_house_value:", rango_median_house_value)

varianza_median_house_value = df["median_house_value"].var()
print("Varianza de median_house_value:", varianza_median_house_value)

desviacion_median_house_value = df["median_house_value"].std()
print("Desviación estándar de median_house_value:", desviacion_median_house_value)

# Tabla de frecuencias
frecuencias = df["median_house_value"].value_counts().sort_index()
print("\nTabla de frecuencias de median_house_value:")
print(frecuencias)

# Crear bins para agrupar la población en intervalos
bins = np.linspace(df["population"].min(), df["population"].max(), 30)
df["pop_bin"] = pd.cut(df["population"], bins)

# Calcular la media del median_house_value en cada grupo de población
grouped = df.groupby("pop_bin")["median_house_value"].mean()

# Graficar la relación entre median_house_value y Population
plt.figure(figsize=(12, 6))
plt.bar(grouped.index.astype(str), grouped, color='blue', alpha=0.7)
plt.xticks(rotation=90, fontsize=8)
plt.xlabel('Rango de Población')
plt.ylabel('Valor Medio de la Casa')
plt.title('Relación entre Valor Medio de la Casa y Popularidad')
plt.show()

# Graficar la relación entre median_house_value y su promedio
plt.figure(figsize=(12, 6))
plt.bar(grouped.index.astype(str), grouped, color='green', alpha=0.7)
plt.axhline(media_median_house_value, color='red', linestyle='dashed', linewidth=2, label=f'Promedio: {int(media_median_house_value)}')
plt.xticks(rotation=90, fontsize=8)
plt.xlabel('Rango de Población')
plt.ylabel('Valor Promedio de la Casa')
plt.title('Comparación entre Valor Medio de la Casa y su Promedio')
plt.legend()
plt.show()
=======
mediana_median_house_value = df["median_house_value"].median()
moda_median_house_value = df["median_house_value"].mode()

rango_housing_median_age = df["housing_median_age"].std()

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

# Mostrar las primeras 5 filas
print("Primeras 5 filas del dataset:")
print(df.head())

# Las últimas 5 filas
print("\nÚltimas 5 filas del dataset:")
print(df.tail())

# Estadísticas descriptivas
# Media
media_value = df["median_house_value"].mean()
print("\nMedia de median_house_value:", media_value)

# Mediana
mediana_value = df["median_house_value"].median()
print("Mediana de median_house_value:", mediana_value)

# Moda
moda_value = df["median_house_value"].mode()[0]
print("Moda de median_house_value:", moda_value)

# Rango
rango_value = df["median_house_value"].max() - df["median_house_value"].min()
print("Rango de median_house_value:", rango_value)

# Varianza
varianza_value = df["median_house_value"].var()
print("Varianza de median_house_value:", varianza_value)

# Desviación estándar
desviacion_value = df["median_house_value"].std()
print("Desviación estándar de median_house_value:", desviacion_value)

# Tabla de frecuencias de "median_house_value"
frequencies = df["median_house_value"].value_counts().sort_index()
print("\nTabla de frecuencias de median_house_value:")
print(frequencies)

# Graficar la relación entre "median_house_value" y "population"
plt.figure(figsize=(10,6))
plt.bar(df["population"], df["median_house_value"], color='blue', alpha=0.7)
plt.xlabel('Población')
plt.ylabel('Valor Medio de la Casa')
plt.title('Relación entre Valor Medio de la Casa y Población')
plt.show()

# Graficar la relación entre "median_house_value" y el promedio de "median_house_value"
average_house_value = df["median_house_value"].mean()
plt.figure(figsize=(10,6))
plt.bar(df["population"], df["median_house_value"], color='green', alpha=0.7)
plt.axhline(average_house_value, color='red', linestyle='dashed', linewidth=2, label=f'Promedio: {average_house_value}')
plt.xlabel('Población')
plt.ylabel('Valor Medio de la Casa')
plt.title('Comparación entre median_house_value y su Promedio')
plt.legend()
plt.show()


>>>>>>> 3b75450b61d7f278a0a0dc83bc5f6570ae1acda5
