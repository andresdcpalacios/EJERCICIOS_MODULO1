# -*- coding: utf-8 -*-
"""EJERCICIOS MODULO1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12HlZ9PD7HHN3a8QMICO147Z8o4_BIQ6I

1.   Imprime “Hello world” 73 veces.
"""

for _ in range(73):
    print("Hello world")

"""2 . Crea un programa en python que devuelva el valor del septuagésimo tercer (73º) número de la serie de Fibonacci."""

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Obtener el 73º número de Fibonacci
print(fibonacci(73))

"""3 Crea un data frame en pandas con 201 filas y las siguientes columnas:"""

import pandas as pd
import numpy as np

# Crear la columna 't' con valores entre 0 y 4 separados por intervalos de 0.02
t = np.arange(0, 4.02, 0.02)[:201]  # Limitamos a 201 valores

# Crear el DataFrame con las columnas especificadas
df = pd.DataFrame({
    't': t,
    's': np.sin(t),
})

# Crear la columna 's10' desplazando 's' en 10 posiciones
df['s10'] = df['s'].shift(-10)

# Crear la columna 'd' como la diferencia entre 's' y 's10'
df['d'] = df['s'] - df['s10']

# Crear la columna 'p' donde el valor es 1 si 'd' es positivo y 0 si es negativo
df['p'] = df['d'].apply(lambda x: 1 if x > 0 else 0)

# Guardar el DataFrame en un archivo CSV separado por ";"
df.to_csv('big_bang_theory_dataset.csv', sep=';', index=False)

"""4 . Carga el archivo creado en un nuevo programa.
a. La última columna m será la media de los valores positivos si p es 1 y la media de los valores negativos si p es 0. Sugerencia: los métodos groupby y transform pueden encadenarse. Documentación método transform
b. Crea finalmente un data frame de solo dos filas con el sumatorio de los valores negativos de la columna d y el sumatorio de los valores positivos de la columna d. Sugerencia: El método groupby será suficiente

a. Calcular la media de valores positivos y negativos de 'd' basado en la columna 'p'.
python
Copy code
"""

# Cargar el archivo CSV
df = pd.read_csv('big_bang_theory_dataset.csv', sep=';')

# Crear la columna 'm' usando groupby y transform
df['m'] = df.groupby('p')['d'].transform(lambda x: x[x > 0].mean() if x.name == 1 else x[x <= 0].mean())

"""b. Crear un DataFrame de solo dos filas con el sumatorio de valores positivos y negativos de 'd'.
python
Copy code

"""

# Crear un DataFrame con el sumatorio de los valores positivos y negativos de 'd'
df_sum = df.groupby(df['d'] > 0)['d'].sum().reset_index(name='sum_d')
df_sum.columns = ['EsPositivo', 'Sumatorio_d']
print(df_sum)

"""6. Calcular el septuagésimo tercer (73º) número primo.

"""

from sympy import primerange

# Generar una lista de los primeros 73 primos y obtener el último
primos = list(primerange(1, 400))  # Usamos un rango suficientemente amplio
print(primos[72])  # Imprimir el 73º número primo (índice 72 porque es 0-indexado)

"""7. Sube a un repositorio de git hub un programa que encuentre un intervalo que tenga 73 números no primos seguidos y compártelo a través de su link en Git Hub."""

from sympy import isprime

def encontrar_intervalo():
    consecutivos = 0
    numero = 2
    while consecutivos < 73:
        if not isprime(numero):
            consecutivos += 1
        else:
            consecutivos = 0
        numero += 1
    return numero - 73

print("Primer número del intervalo de 73 números no primos consecutivos:", encontrar_intervalo())