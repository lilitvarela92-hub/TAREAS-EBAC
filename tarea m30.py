# %% [markdown]
# ## **PRÁCTICA 30: DATA MASSAGING I**
# #### **Objetivo:** Realizar pruebas de inserción, eliminación y edición de datos
# ------------------

# %%
# Importación de librerías 
import pandas as pd
import csv
import numpy
import os
import matplotlib.pyplot as plt

# %% [markdown]
# #### 1. Importar el archivo fifa_eda.csv

# %%
# 1. Importar el archivo fifa_eda.csv

# Cambiar el directorio actual con chdir
os. chdir('C:/Users/LILO/Downloads')

# Traer el archivo 
df = pd.read_csv('fifa_eda.csv')

# %% [markdown]
# #### 2. Mostrar las primeras 20 filas del archivo, las últimas 5 y un sample de 10

# %%
# Para mostrar las primeras 20 filas del archivo
df.head(20)

# %%
# Para mostrar las últimas 5 filas
df.tail(5)

# %%
# Para ver un aleatorio de 5 registros (sample)
df.sample(5)

# %% [markdown]
# #### 3. Generar data estadística con .describe() y además los tipos de datos del dataset

# %%
df.describe().T

# %% [markdown]
# #### 4. Si es necesario, pasar a numéricas por lo menos 2 columnas que contengan números para incluirlas en .describe().

# %%
df.dtypes
# En este caso no es necesario pasar a numéricas las columnas, así que nos saltamos este paso

# %% [markdown]
# #### 5. Añadir una columna “Years Playing”, que calcule el año actual menos la columna “Joined”

# %%
from datetime import datetime

# 1. Obtener el año actual 
current_year = datetime.now().year
current_year

# %%
# Crear la nueva columna llamada "Years Playing"
df["Years Playing"] = current_year - df['Joined']

# %%
# Verificar el nuevo campo
df.head(2)

# %% [markdown]
# #### 6. Buscar y mostrar a todos los jugadores de Mexico

# %%
jugadores_mexicanos = df[df['Nationality'] == 'Mexico']

jugadores_mexicanos

# %% [markdown]
# #### 7. Ordenar y mostrar los datos por la columna ReleaseClause (sueldo)

# %%
df.groupby('Position')['Release Clause'].max()

# %% [markdown]
# #### 8. Generar un nuevo dataset que contenga el año (joined) y el número de jugadores (groupby)

# %%
# Se realiza un groupby para ver el número de jugadores de cada año
conteo_por_año = df.groupby('Joined').size()
conteo_por_año

# %%
jugadores_por_año = conteo_por_año.reset_index(name='Num_Jugadores')
jugadores_por_año.head(2)

# %% [markdown]
# #### 9. ❖Opcional❖: Generar un gráfico que contenga, por año, el número de jugadores

# %%
x_data = jugadores_por_año['Joined']
y_data = jugadores_por_año['Num_Jugadores']
plt.bar(x_data, y_data, color='skyblue')

plt.title('Número de jugadores registrados por año', fontweight = 'bold')
plt.xlabel('Año de ingreso')
plt.ylabel('No. Jugadores')

plt.grid(axis='y', linestyle='--') 
plt.tight_layout()
plt.show()

# %%



