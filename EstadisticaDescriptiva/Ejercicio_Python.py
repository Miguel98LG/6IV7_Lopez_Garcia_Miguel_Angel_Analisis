import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

media_median_house_value = df["median_house_value"].mean()
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


