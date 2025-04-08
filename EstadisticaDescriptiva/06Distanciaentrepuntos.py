import numpy as np
import pandas as pd
from scipy.spatial import distance

#Definimos las coordenadas de nuestro sistema de tiendas

tiendas = {
    ' Tienda A ': (1,1),
    'Tienda B ' : (1,5),
    'Tienda C ' : (7,1),
    'Tienda D ' : (3,3),
    'Tienda E ' : (4,8)
}

#Necesitamos convertir las coordenadas en un Frame para facilitar el calculo

df_tiendas = pd.DataFrame(tiendas).T
df_tiendas.columns = ['X','Y']
print('Coordenadas de las tiendas: ')
print(df_tiendas)

#Inicializamos los dataframes de lo que vamos a obtener para el calculo de distancias

distancias_punto1 = pd.DataFrame(index=df_tiendas.
index, columns=df_tiendas.index)

distancias_punto2 = pd.DataFrame(index=df_tiendas.
index, columns=df_tiendas.index)

distancias_punto3 = pd.DataFrame(index=df_tiendas.
index, columns=df_tiendas.index)

#vamos a calcular las distancias
for i in df_tiendas.index:
    for j in df_tiendas.index:
        #Defino la distancia euclidiana del primer punto
        distancias_punto1.loc[i,j] = distance.euclidean(df_tiendas.loc[i],df_tiendas.loc[j])
        
        distancias_punto2.loc[i,j] = distance.cityblock(df_tiendas.loc[i],df_tiendas.loc[j])
        
        distancias_punto3.loc[i,j] = distance.chebyshev(df_tiendas.loc[i],df_tiendas.loc[j])
        
#Mostrar resultados 
print('/n DIstancia euclidiana entre cada una de las tiendas: ')
print(distancias_punto1)
print('/n DIstancia Manhattan entre cada una de las tiendas: ')
print(distancias_punto2)
print('/n DIstancia Chevyshev entre cada una de las tiendas: ')
print(distancias_punto1)

#Calcularemos las distancias entre todos los pares de puntos y determinaremos cuáles están más alejados entre sí y cuáles están más cercanos, utilizando las distancias Euclidiana, Manhattan y Chebyshev.
#Ejercicio: Determinación de Distancias entre Puntos
#Puntos en el Plano

#Los puntos en el plano son los siguientes:

#    Punto A: (2, 3)
#   Punto B: (5, 4)
#    Punto C: (1, 1)
#    Punto D: (6, 7)
#    Punto E: (3, 5)
#    Punto F: (8, 2)
#    Punto G: (4, 6)
#    Punto H: (2, 1)

# Definimos las coordenadas de los puntos en el plano
puntos = {
    'Punto A': (2, 3),
    'Punto B': (5, 4),
    'Punto C': (1, 1),
    'Punto D': (6, 7),
    'Punto E': (3, 5),
    'Punto F': (8, 2),
    'Punto G': (4, 6),
    'Punto H': (2, 1)
}

# Convertimos las coordenadas en un DataFrame para facilitar el cálculo
df_puntos = pd.DataFrame(puntos).T
df_puntos.columns = ['X', 'Y']
print('Coordenadas de los puntos en el plano:')
print(df_puntos)

# Inicializamos los DataFrames para almacenar las distancias
distancias_euclidiana = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_manhattan = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)
distancias_chebyshev = pd.DataFrame(index=df_puntos.index, columns=df_puntos.index)

# Calculamos las distancias
for i in df_puntos.index:
    for j in df_puntos.index:
        distancias_euclidiana.loc[i, j] = distance.euclidean(df_puntos.loc[i], df_puntos.loc[j])
        distancias_manhattan.loc[i, j] = distance.cityblock(df_puntos.loc[i], df_puntos.loc[j])
        distancias_chebyshev.loc[i, j] = distance.chebyshev(df_puntos.loc[i], df_puntos.loc[j])

# Mostramos los resultados
print('\nDistancia Euclidiana entre cada par de puntos:')
print(distancias_euclidiana)
print('\nDistancia Manhattan entre cada par de puntos:')
print(distancias_manhattan)
print('\nDistancia Chebyshev entre cada par de puntos:')
print(distancias_chebyshev)

# Convertir todos los valores a float
distancias_euclidiana = distancias_euclidiana.astype(float)
distancias_manhattan = distancias_manhattan.astype(float)
distancias_chebyshev = distancias_chebyshev.astype(float)

# Eliminar las distancias de un punto consigo mismo (0s en la diagonal)
euclidiana_stack = distancias_euclidiana.stack()
manhattan_stack = distancias_manhattan.stack()
chebyshev_stack = distancias_chebyshev.stack()

# Filtrar valores iguales a 0 (misma coordenada)
euclidiana_stack = euclidiana_stack[euclidiana_stack != 0]
manhattan_stack = manhattan_stack[manhattan_stack != 0]
chebyshev_stack = chebyshev_stack[chebyshev_stack != 0]

# Obtener máximos y mínimos
print(f'\nPuntos más alejados (Euclidiana): {euclidiana_stack.idxmax()} - Distancia: {euclidiana_stack.max()}')
print(f'Puntos más cercanos (Euclidiana): {euclidiana_stack.idxmin()} - Distancia: {euclidiana_stack.min()}')
print(f'\nPuntos más alejados (Manhattan): {manhattan_stack.idxmax()} - Distancia: {manhattan_stack.max()}')
print(f'Puntos más cercanos (Manhattan): {manhattan_stack.idxmin()} - Distancia: {manhattan_stack.min()}')
print(f'\nPuntos más alejados (Chebyshev): {chebyshev_stack.idxmax()} - Distancia: {chebyshev_stack.max()}')
print(f'Puntos más cercanos (Chebyshev): {chebyshev_stack.idxmin()} - Distancia: {chebyshev_stack.min()}')
