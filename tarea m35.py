# %% [markdown]
# ## **PRÁCTICA M35: PAQUETE NUMPY Y PROBLEMAS ESTADÍSTICOS**

# %% [markdown]
# ### **Objetivo:**
# - Usar la librería numpy para: 
#     - Ejecutar funciones estadísticas descriptivas básicas
#     - Ejecutar ejemplos de ordenamiento y posición
#     - Realizar cálculos de correlación
# ------

# %% [markdown]
# ### **Paso a paso:**
# Generar archivo tipo Notebook de Python que contenga el código fuente de:
# - Importar el archivo supermarket_sales.csv
# - importar Numpy. Generar estadística descriptiva básica en las columnas unit_price y quantity: Cálculo de la media, mediana y moda
# - Obtener el ticket promedio:
#     1. Por ciudad
#     2. Por product line y ciudad
#     3. Por género
#     4. Por género y product line
# - Usar el método rank para generar top 5 de:
#     1. Ventas por ciudad
#     2. Ventas por member
#     3. Ventas por payment. Obtener además el % de aporte de cada categoría
# - Cálculo de una matríz de correlación entre la hora(sin minutos) y el total, y otra que correlacione el unit_price con el raiting de la transacción, para validar si los productos más caros son lo que dejan más margen
# -----------

# %% [markdown]
# **- Importar el archivo csv**

# %%
# ---- Importar el archivo supermarket_sales.csv ----
import pandas as pd
import os

os.chdir('C:/Users/LILO/Downloads')

# Se usa la función read_csv para leer el archivo .csv
# Se ingesta en la variable df
df = pd.read_csv('supermarket_sales.csv')

# %%
df.sample(5)

# %% [markdown]
# ----------
# **- Importar Numpy.Generar estadística descriptiva básica en columnas unit_price y quantity**

# %%
import numpy as np

# Primero transformar en array tipo Numpy las columnas numéricas
unitprice_np = df[['Unit price']].to_numpy()
quantity_np = df[['Quantity']].to_numpy()
tax5_np = df[['Tax 5%']].to_numpy()
total_np = df[['Total']].to_numpy()
cogs_np = df[['cogs']].to_numpy()
grossmp_np = df[['gross margin percentage']].to_numpy()
groosi_np = df[['gross income']].to_numpy()
raiting_np = df[['Rating']].to_numpy()

# %%
type(quantity_np)

# %%
np.shape(unitprice_np)

# %%
np.count_nonzero(unitprice_np)

# %%
# Para calcular la media de *unit_price*
media_up = unitprice_np.mean()
format_up = '{:.2f}'.format(media_up)
print(f'La media del precio unitario de los productos es =',format_up, 'dls.')

# %%
# Para calcula la moda de *unit_price*
# -- 1. Generamos un array con valores únicos de Precio unitario
vals, counts = np.unique(unitprice_np, return_counts = True)
index_up = np.argmax(counts)
moda_up = vals[index_up]
print(f'La moda del precio unitario es = ', moda_up, 'dls.')

# %%
vals[763:770]

# %%
counts[763:770]

# %%
# Para calcula la mediana de unit_price
mediana_up = np.median(unitprice_np)
format_up = '{:.2f}'.format(mediana_up)
print(f'La mediana del precio unitario es =', format_up, 'dls.')

# %%
# Se grafica la media, mediana y moda del Precio unitario
import seaborn as sns
import matplotlib.pyplot as plt 

sns.set_style('darkgrid')
sns.displot(unitprice_np)
plt.xlabel('Precio unitario (dls $)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Precio Unitario')
plt.axvline(x=unitprice_np.mean(), color='red', ls='--')
plt.axvline(x=mediana_up, color='blue', ls='--')
plt.axvline(x=moda_up, color='green', ls='--')

# %%
# ---- Para calcular la media de quantity
media_qu = quantity_np.mean()
print(f'La media de la cantidad de los productos es =',media_qu, 'pzas.')

# %%
# ---- Para calcula la moda de quantity
# Generamos un array con valores únicos de las cantidades
vals, counts = np.unique(quantity_np, return_counts = True)
index_qu = np.argmax(counts)
moda_qu = vals[index_qu]
print(f'La moda de la cantidad de los productos es = ', moda_qu, 'pzas.')

# %%
vals

# %%
counts

# %%
# Para calcula la mediana de unit_price
mediana_qu = np.median(quantity_np)
print(f'La mediana de la cantidad de productos es =', mediana_qu, 'pzas.')

# %%
# Se grafica la media, mediana y moda del Precio unitario
import seaborn as sns
import matplotlib.pyplot as plt 

sns.set_style('darkgrid')
sns.displot(quantity_np)
plt.xlabel('Piezas')
plt.ylabel('Frecuencia')
plt.title('Histograma de Cantidad de Productos')
plt.axvline(x=media_qu.mean(), color='red', ls='--')
plt.axvline(x=mediana_qu, color='blue', ls='--')
plt.axvline(x=moda_qu, color='green', ls='--')

# %% [markdown]
# ------------
# #### - Obtener el ticket promedio:
#         1. Por ciudad
#         2. Por product line y ciudad
#         3. Por genero
#         4. Por genero y product line

# %%
df.sample()

# %%
# ---- 1. Obtener ticket promedio por ciudad
ticket_ciudad = df.groupby('City')['Total'].mean()
ticket_ciudad

# %%
# ---- Obtener ticket promedio por product line y ciudad
ticket_pl_ciudad = df.groupby(['Product line', 'City'])['Total'].mean()
ticket_pl_ciudad

# %%
# ---- 3. Obtener ticket promedio por genero
ticket_genero = df.groupby('Gender')['Total'].mean()
ticket_genero

# %%
# ---- 4. Obtener ticket promedio por genero y product line
ticket_pl_genero = df.groupby(['Gender', 'Product line'])['Total'].mean()
ticket_pl_genero

# %% [markdown]
# -----
# ### - Usar el método rank para generar top 5 y obtener el % de cada categoría de:
#         1. Ventas por ciudad
#         2. Ventas por member
#         3. Ventas por payment

# %%
df.sample()

# %%
def generar_ranking (columna_agrupar):
    ventas = df.groupby(columna_agrupar)['Total'].sum().reset_index()
    total_global = ventas['Total'].sum()

    # Calcular % de aporte
    ventas['% Aporte']= (ventas['Total'] / total_global) * 100

    # Aplicar ranking
    ventas['Rank'] = ventas['Total'].rank(ascending=False, method='min')
    return ventas.sort_values(by='Rank').head(5)

print('----- Ranking Top 5 -----')
print('Top 5 ventas por Ciudad:\n', generar_ranking('City'), '\n')
print('Top 5 ventas por Miembro:\n', generar_ranking('Customer type'), '\n')
print('Top 5 ventas por Metodo de Pago:\n', generar_ranking('Payment'), '\n')

# %% [markdown]
# -------
# - Cálculo de una matríz de correlación:
#     - Una entre la hora(sin minutos) y el total
#     - Otra que correlacione el unit_price con el raiting de la transacción, para validar si los productos más caros son lo que dejan más margen.

# %%
# ----- Matríz de correlación entre la hora (sin minutos) y el total
Hour = df['Hour']= pd.to_datetime(df['Time']).dt.hour
corr_hora_total = np.corrcoef(df['Hour'], df['Total'])[0,1]
print(f'Correlación entre la Hora vs el Total:{corr_hora_total:.4f}')

# %%
# ---- Matríz de correlación entre el unit_price con el raiting de transacción
corr_unitprice_rating = np.corrcoef(df['Unit price'], df['Rating'])[0,1]
print(f'Correlación Precio Unitario vs Rating: {corr_unitprice_rating:.4f}')

# %%
# Se realiza un Heatmap
columnas_interes = ['Unit price', 'Quantity', 'Total', 'Rating', 'Hour']
matriz_corr = df[columnas_interes].corr().round(2)

# Crear el HeatMap
plt.figure(figsize=(8, 6))
sns.heatmap(matriz_corr,
            annot=True,
            cmap='BrBG',
            fmt='.2f',
            linewidths=0.5)
plt.title('Matríz de correlación: Ventas y Satisfacción')
plt.show()

# %%
# Gráfico de tríangulo de correlación
plt.figure(figsize=(8,8))
mask = np.triu(np.ones_like(matriz_corr, dtype=bool))
heatmap = sns.heatmap(matriz_corr, mask=mask, vmin=-1, vmax=1, annot=True, cmap='BrBG')
heatmap.set_title('Mapa de Calor de Tríangulo de Correlación', fontdict={'fontsize':18},pad=16)

# %%



