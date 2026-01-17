# %% [markdown]
# ## **MÓDULO 32: VISUALIZACIÓN DE DATOS PARA ANALYTICS**

# %% [markdown]
# ## **Objetivo**
# - Generación de wireframe (Miro, Slides) sobre 1 reporte con 5 elementos 
# - Generar un archivo tipo Notebook de Python que contenga el código fuente de:
#     - Leer archivo fifa_eda.csv  
#     - Elemento 1: Obtener matriz de correlación y dejarla como heat map 
#     - Elemento 2: Gráfico de Correlación que responda – “Cuál es la relación entre la edad y el overall?” – explicar la salida
#     - Elemento 3: Generar un gráfico de barras por club que indique el número de jugadores 
#     - Elemento 4: Hacer un gráfico multipanel que indique la relación altura (height) vs skill moves, siendo la variable del panel si es zurdo o derecho 
#     - Elemento 5: Un gráfico que crea importante para mostrar a los potenciales cracks
# ------------

# %% [markdown]
# Leer el archivo fifa_eda.csv

# %%
# Paleta de colores FIFA
FIFA_DBLUE = "#000D48"    # Azul oscuro
FIFA_GRAY = "#95969A"    # Gris
FIFA_CBLUE = "#005391"    # Cian brillante
FIFA_WHITE = "#FFFFFF"   # Blanco puro
FIFA_RED = "#D81E05"     # Rojo acento

# %%
# Importar librerías
import pandas as pd
import numpy as np
import os

# Cambiar el directorio actual con chdir
os.chdir('C:/Users/LILO/Downloads')

# Leer el archivo .csv
df = pd.read_csv('fifa_eda.csv')

# %% [markdown]
# Elemento 1: Obtener matriz de correlación y dejarla como heat map 

# %%
# Importar librerías necesarias
import plotly.express as px

# %%
# Se obtiene la matriz de correlación
df.corr(numeric_only=True)

# %%
# Heatmap
fig1 = px.imshow(df.corr(numeric_only=True), 
                text_auto = True, aspect= 'auto', 
                color_continuous_scale=[FIFA_WHITE, FIFA_CBLUE, FIFA_DBLUE],
                title= 'Elemento 1: Matriz de Correlación de Atributos')
fig1.show()

# %% [markdown]
# Elemento 2: Gráfico de Correlación que responda – “Cuál es la relación entre la edad y el overall?” – explicar la salida

# %%
fig2= px.scatter(df, x='Age', y= 'Overall', 
                 trendline= 'ols',
                title = 'Elemento 2: Relación entre la edad y el Overall',
                color = 'Overall',
                color_continuous_scale=[FIFA_DBLUE, FIFA_RED],
                )
fig2.show()

# %%
# Como se puede observar en el gráfico, el overall tiende a subir con la edad hasta llegar a
# un pico (26 a 29 años), luego empieza a descender levemente
# La linea de tendencia muestra una correlación positiva general, sin embargo presenta una moderada dispersión

# %% [markdown]
#  Elemento 3: Generar un gráfico de barras por club que indique el número de jugadores 

# %%
# Hacemos un groupby de los clubes y contamos los nombres de los jugadores
club_data = df.groupby('Club')['Name'].count().reset_index()

# Renombramos las columnas 
club_data.columns = ['Club', 'Cantidad Jugadores'] 

# Ya que son un número significativo de clubes, traemos los primeros 20
club_data = club_data.sort_values(by='Cantidad Jugadores', ascending=False).head(20)
club_data


# %%
fig3 = px.bar(club_data, x='Club', y='Cantidad Jugadores',
             title="Elemento 3: Cantidad de Jugadores por Club (Top 20)",
             color_discrete_sequence=[FIFA_CBLUE],
             labels={'Cantidad Jugadores': 'Número de Jugadores'},
             text_auto=True) 
fig3.show()

# %% [markdown]
# Elemento 4: Hacer un gráfico multipanel que indique la relación altura (height) vs skill moves, siendo la variable del panel si es zurdo o derecho 

# %%
fig4 = px.scatter(df, x="Height", y="Skill Moves", 
                 facet_col="Preferred Foot", 
                 color = 'Skill Moves',
                 color_continuous_scale= [FIFA_DBLUE, FIFA_GRAY],
                 title="Elemento 4: Relación Altura vs Skill Moves (Zurdo vs Diestro)",
                 opacity=0.5,
                 trendline="lowess")
fig4.show()

# %% [markdown]
# Elemento 5: Un gráfico que crea importante para mostrar a los potenciales cracks

# %%
# Definimos "Crack" como alguien joven (<22 años) con alto potencial y valor de mercado bajo/medio
cracks = df[(df['Age'] <= 22) & (df['Potential'] > 85)]
cracks

# %%
fig5 = px.scatter(cracks, x="Age", y="Potential", 
                 size="Value", color="Overall",
                 hover_name="Name",
                 title="Elemento 5: Mapa de Futuras Estrellas (Jóvenes con Potencial > 85)",
                 color_continuous_scale=[FIFA_DBLUE, FIFA_CBLUE],
                 labels={"Value": "Valor de Mercado (K)"})
fig5.show()

# %%



