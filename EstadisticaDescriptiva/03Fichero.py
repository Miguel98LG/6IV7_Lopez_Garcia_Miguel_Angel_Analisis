import pandas as pd

#vamos hacer un


def cotizacion(fichero):
    df = pd.read_csv(fichero, sep=';', decimal=',', thousands='.',
    index_col=0)