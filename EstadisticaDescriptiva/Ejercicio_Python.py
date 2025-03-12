import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

media_median_house_value = df["median_house_value"].mean()
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
