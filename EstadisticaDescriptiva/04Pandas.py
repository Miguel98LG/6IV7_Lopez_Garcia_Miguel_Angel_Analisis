import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

#Mostrar las primeras 5 filas
print(df.head())

#Las ultimas 5 filas
print(df.tail())

#Quiero una fila en especifico
print(df.iloc[7])

#Quiero mostrar una columna por su nombre
print(df["ocean_proximity"])

#Obetenr la media de la columna de total de cuartos
mediacuartos = df["total_rooms"].mean()
print('Media de los cuartos: ', mediacuartos)

#Obtener la mediana de la columna population
medianapopularidad= df["population"].median()
print('Mediana de popularidad: ', medianapopularidad)

std_age = df["housing_median_age"].std()
print('Desviacion estandar de años: ', std_age)

#Para poder filtrar
filtrodeloceano = df[df["ocean_proximity"] == "ISLAND"]
print('Filtro de proximidad del oceano: ', filtrodeloceano)

#vamos a crear un grafico de dipsersion entre los registros
# de la proximidad del oceano vs los precios

plt.scatter(df["ocean_proximity"][:10],
df["median_house_value"][:10])

#Hay que definir a x y 
plt.xlabel('Proximidad')
plt.ylabel('Precio')

plt.title('Grafico de Dispersion de Proximidad ')
plt.show()