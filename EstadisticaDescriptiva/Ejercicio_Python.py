import pandas as pd

import matplotlib.pyplot as plt

df = pd.read_csv('./EstadisticaDescriptiva/housing.csv')

media_housing_median_age = df["housing_median_age"].mean()
mediana_housing_median_age = df["housing_median_age"].median()
moda_housing_median_age = df["housing_median_age"].mode()

rango_housing_median_age = df["housing_median_age"]