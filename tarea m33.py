# %% [markdown]
# # **TAREA M33-AD- Liliana Tamalatzi Varela**

# %% [markdown]
# ### **Objetivos:**
# - Aplicar principios básicos de EDA usando un ejemplo de kaggle de dominio público.
# - Realizar transformaciones y visualizaciones aprendidas en el módulo, enfocandose en datos seleccionados de videojuegos para simular un análisis de mercado para una nueva plataforma.

# %% [markdown]
# ### **Paso a paso:**
# Generar un análisis completo de EDA aplicado al archivo que contenga:
# - **Fase 1:** Lectura del archivo, head, tail, sample, describe. Validación de columnas numéricas para que funcione con todas
# 
# - **Fase 2:** Obtencion de Elementos mínimos:
#     - **Totales:**
#     1) Total de videojuegos analizados
#     2) Total de géneros analizados
#     3) Plataformas analizadas
# 
#     - **Ventas** ( Todos estos números desglosados por ingreso: NA, EU, JP, Otros y el Global):
#     1) Total de ventas por año
#     2) Juegos más vendidos por año
#     3) Plataformas con más ingresos por año
#     4) Gráfico de comparación de ventas entre géneros por año, 
#         
#     - **Insights:** 2 Gráficos adicionales interesantes
# 
# - **Fase 3:** Revisar el EDA del ejercicio anterior y añadir siguientes elementos, basados en los últimos 4 años
#     - **Crecimiento**
#     1) Género con mayor y menor crecimiento
#     2) Plataforma con mayor y menor crecimiento
#     3) Videojuego con mayor y menor crecimiento
# 
#     - **2 Elementos adicionales:** que muestren oportunidades de mercado
# ----------------------------

# %%
# Importar librerías necesarias
import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt

# %% [markdown]
# ### **Fase 1**
# - Lectura del archivo, head, tail, sample, describe.

# %%
# 1. Leer el archivo .csv

# Cambiar el directorio actual con chdir
os.chdir('C:/Users/LILO/Downloads')

# Usar la función read_csv para leer el archivo .csv
df = pd.read_csv('vgsales.csv')

# %%
# Para obtener los primeros rows del dataframe
df.head()

# %%
# Para obtener los ultimos rows del dataframe
df.tail()

# %%
# Para obtener un sample de 5 rows
df.sample(5)

# %%
# Para obtener el numero de rows y columnas
df.shape

# %%
df.describe()

# %%
# Para obtener la información del DataFrame
df.info()

# %% [markdown]
# - Validación de columnas numéricas para que funcione con todas

# %%
# Elección de columnas que deben ser numéricas
numeric_cols = ['Year','NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

# Conversión y validación
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# %% [markdown]
# - Masajeo de datos

# %%
# Cambiamos el tipo de dato de "Year", de float a entero
df['Year'] = df['Year'].astype('Int64')

# %%
df.info()

# %%
# Número de datos vacíos por columna
missing_values_count = df.isnull().sum()
missing_values_count[0:11]

# %%
# Obtención del porcentaje de datos vacios 
total_cells = np.product(df.shape)
total_missing = missing_values_count.sum()
# Calculo del porcentaje
percent_missing = (total_missing / total_cells) * 100
print(f'Porcentaje de Datos que no existe: {percent_missing:.2f}%')

# %%
# Eliminamos solo las filas que no tienen año
df.dropna(subset=['Year'], inplace=True)

# %%
# Para el caso de publisher, rellenamos los datos faltantes
df['Publisher'] = df['Publisher'].fillna('Unknown')

# %%
df.info()

# %% [markdown]
# -----------------
# ### **Fase 2:**
# - Obtención de Elementos mínimos (Totales)

# %%
# 1) Total de videojuegos analizados
# 2) Total de géneros analizados
# 3) Plataformas analizadas

total_juegos = df['Name'].nunique()
total_generos = df['Genre'].nunique()
total_plataformas = df['Platform'].nunique()

print ('Totales')
print ('----------------')
print(f'Juegos = {total_juegos}')
print(f'Géneros = {total_generos}')
print(f'Plataformas = {total_plataformas}')

# %% [markdown]
# - Obtención de Elementos mínimos (Ventas)

# %%
# Definimos las columnas de ventas por región
ventas_columnas = ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']

# ---------VENTAS TOTALES POR AÑO Y REGIÓN ------------
# Agrupamos por ventas por año
ventas_por_año = df.groupby('Year')[ventas_columnas].sum()
ventas_por_año

# %%
# --- JUEGOS MÁS VENDIDOS POR AÑO ---
# Usamos idxmax para encontrar el índice del máximo Global_Sales por año
idx_max_juego = df.groupby('Year')['Global_Sales'].idxmax()
juegos_top_año = df.loc[idx_max_juego, ['Year', 'Name', 'NA_Sales', 'EU_Sales',
                                         'JP_Sales', 'Other_Sales', 'Global_Sales']
                                         ].sort_values('Year', ascending=False)
juegos_top_año

# %%
# --- PLATAFORMAS CON MÁS INGRESOS POR AÑO ---
plataforma_top_año = df.groupby(['Year', 'Platform'])['Global_Sales'].sum().reset_index()
plataforma_top_año = plataforma_top_año.sort_values('Year', ascending=False).drop_duplicates('Year')
plataforma_top_año

# %%
# 1. Identificar los 7 géneros con mayores ventas globales históricas
top_7_generos = df.groupby('Genre')['Global_Sales'].sum().nlargest(7).index

# 2. Filtrar el dataframe original para quedarnos solo con esos 7
df_top = df[df['Genre'].isin(top_7_generos)]

# 3. Crear la tabla pivote para el gráfico de área
# Usamos fillna(0) para que no haya huecos en el gráfico
area_data = df_top.groupby(['Year', 'Genre'])['Global_Sales'].sum().unstack().fillna(0)

# 4. Graficar con estilo profesional y fondo transparente
fig, ax = plt.subplots(figsize=(12, 6))

# Usamos una paleta de colores más armónica (Spectral o Viridis)
area_data.plot(kind='area', stacked=True, ax=ax, colormap='Spectral', alpha=0.8)

# Configuración estética para que brille en la diapositiva
plt.title('Evolución del Mercado: Top 7 Géneros más Vendidos', fontsize=16, fontweight='bold', pad=20)
plt.ylabel('Ventas Globales (Millones)', fontsize=12)
plt.xlabel('Año de Lanzamiento', fontsize=12)

# Colocamos la leyenda fuera para no saturar el área de dibujo
plt.legend(title='Géneros Líderes', bbox_to_anchor=(1.02, 1), loc='upper left', frameon=False)

plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()

# Guardar con alta resolución y transparencia
# plt.savefig('top_7_generos_area.png', transparent=True, dpi=300)
plt.show()

# %% [markdown]
# - Insights Adicionales

# %%
# Insight 1: Pie Chart de Ventas Totales por Región
regiones_sum = df[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()
regiones_sum

# %%
# Configuración del gráfico
plt.figure(figsize=(8, 8))
plt.pie(
    regiones_sum, 
    labels=regiones_sum.index, 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=sns.color_palette('colorblind'),
    pctdistance=0.75,    # Mueve el porcentaje (%) hacia adentro
    labeldistance=1.1,   # Mantiene el nombre de la región justo afuera o en el borde
    textprops={'fontsize': 12, 'color': 'black'} # Estilo de letra
)

plt.title('Participación de Mercado Histórica por Región', fontsize=14, pad=20, color= 'black', fontweight= 'bold')

# Para que al guardar no tenga fondo blanco:
# plt.savefig('pie_chart.png', transparent=True) 

plt.show()

# %%


# %% [markdown]
# ---------------------
# ### **Fase 3:**
# - Añadir elementos de los últimos 4 años: Crecimiento

# %%
# Definir los últimos 4 años disponibles
ultimos_años = sorted(df['Year'].unique())[-4:]
df_reciente = df[df['Year'].isin(ultimos_años)]

# Función para calcular crecimiento (Diferencia entre el último año y el primero del rango)
def calcular_crecimiento(columna_grupo):
    pivot = df_reciente.pivot_table(index=columna_grupo, columns='Year', values='Global_Sales', aggfunc='sum').fillna(0)
    pivot['Crecimiento'] = pivot[ultimos_años[-1]] - pivot[ultimos_años[0]]
    return pivot.sort_values('Crecimiento', ascending=False).head(5)

# 1. Crecimiento por Género
crec_genero = calcular_crecimiento('Genre')
# 2. Crecimiento por Plataforma
crec_plat = calcular_crecimiento('Platform')
# 3. Crecimiento por Videojuego
crec_juego = calcular_crecimiento('Name')

# Reutilizamos la lógica de la Fase 3
def obtener_extremos(df_pivote, concepto):
    mayor = df_pivote.sort_values('Crecimiento', ascending=False).head(1)
    menor = df_pivote.sort_values('Crecimiento', ascending=True).head(1)
    
    print(f"--- {concepto} ---")
    print(f"Mayor Crecimiento: {mayor.index[0]} ({mayor['Crecimiento'].values[0]:.2f}M)")
    print(f"Menor Crecimiento (Caída): {menor.index[0]} ({menor['Crecimiento'].values[0]:.2f}M)")
    print("-" * 30)

# Aplicar a Género, Plataforma y Videojuego
obtener_extremos(crec_genero, "GÉNERO")
obtener_extremos(crec_plat, "PLATAFORMA")
obtener_extremos(crec_juego, "VIDEOJUEGO")

# %%
# 1. Configurar la figura con 3 sub-gráficos
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

datos_top = [crec_genero, crec_plat, crec_juego]
titulos = ['Top Géneros', 'Top Plataformas', 'Top Videojuegos']
paletas = ['Greens_r', 'Blues_r', 'YlGn_r'] 

for i in range(3):
    df_plot = datos_top[i]
    
    # Creamos el gráfico en el eje correspondiente
    sns.barplot(
        x='Crecimiento', 
        y=df_plot.index, 
        data=df_plot, 
        ax=axes[i], 
        palette=paletas[i]
    )
    
    # AGREGAR ETIQUETAS A CADA EJE INDIVIDUAL
    # Accedemos al contenedor de barras del eje actual (axes[i])
    for container in axes[i].containers:
        axes[i].bar_label(container, fmt='%.2f', padding=3, fontweight='bold', fontsize=10)
    
    # Estética
    axes[i].set_title(titulos[i], fontsize=14, fontweight='bold')
    axes[i].set_xlabel('Crecimiento (Millones)', fontsize = 12)
    axes[i].set_ylabel('', fontsize = 12)
    axes[i].set_facecolor('none')
    axes[i].grid(axis='x', linestyle='--', alpha=0.3)
    
    # Ajuste dinámico del límite X para que quepan los números
    # Para valores negativos, extendemos hacia la izquierda; para positivos, hacia la derecha
    xmin, xmax = axes[i].get_xlim()
    axes[i].set_xlim(xmin * 1.15 if xmin < 0 else xmin, xmax * 1.15 if xmax > 0 else xmax)

plt.suptitle(f'Líderes de Crecimiento del Mercado ({ultimos_años[0]} - {ultimos_años[-1]})', 
             fontsize=18, fontweight='bold', y=1.05)
plt.tight_layout()
plt.show()

# %% [markdown]
# - **2 Elementos adicionales:** que muestren oportunidades de mercado

# %%
# ------ Oportunidad 1: Para obtener las oportunidades de eficiencia por género ------

# 1. Agrupar datos para ver eficiencia
oportunidades = df_reciente.groupby('Genre').agg({'Global_Sales': 'sum',
                                                  'Name': 'count'}).rename(columns={'Name': 'Cantidad_Juegos'})

# 2. Calcular el Retorno Promedio (Ventas totales / Número de juegos)
oportunidades['Ventas_Promedio'] = oportunidades['Global_Sales'] / oportunidades['Cantidad_Juegos']
oportunidades

# %%
# 3. Graficar
plt.figure(figsize=(12, 7), facecolor='none')
plt.scatter(oportunidades['Cantidad_Juegos'], oportunidades['Ventas_Promedio'], 
            s=oportunidades['Global_Sales']*50, # El tamaño de la burbuja es la venta total
            alpha=0.6, c=oportunidades['Ventas_Promedio'], cmap='viridis')

# Añadir etiquetas a cada burbuja
for i, txt in enumerate(oportunidades.index):
    plt.annotate(txt, (oportunidades['Cantidad_Juegos'].iat[i], oportunidades['Ventas_Promedio'].iat[i]), 
                 xytext=(5,5), textcoords='offset points', fontsize=10, fontweight='bold')

plt.title('Mapa de Oportunidades: Eficiencia por Género (2015-2020)', fontsize=15, fontweight='bold')
plt.xlabel('Saturación de Mercado (Número de Lanzamientos)', fontsize=12)
plt.ylabel('Potencial de Éxito (Ventas Promedio por Título)', fontsize=12)
plt.gca().set_facecolor('none')
plt.grid(linestyle='--', alpha=0.3)

plt.show()

# %%
# 1. Agrupar ventas por Género y Región
regiones_gen = df_reciente.groupby('Genre')[['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']].sum()

# 2. Convertir a porcentajes (Normalizar al 100%)
# Esto nos dice: "Del total de juegos de X género, ¿qué % se vende en cada región?"
regiones_perc = regiones_gen.div(regiones_gen.sum(axis=1), axis=0) * 100
regiones_perc

# %%
# 3. Graficar
ax = regiones_perc.plot(kind='barh', stacked=True, figsize=(14, 8), 
                        color=['#4285F4', '#EA4335', '#FBBC05', '#34A853'], alpha=0.8)

# Añadir etiquetas de porcentaje dentro de las barras
for p in ax.patches:
    width, height = p.get_width(), p.get_height()
    if width > 5: # Solo mostrar si el segmento es lo suficientemente grande
        ax.annotate(f'{width:.1f}%', (p.get_x() + width/2, p.get_y() + height/2), 
                    ha='center', va='center', fontsize=9, color='white', fontweight='bold')

plt.title('Oportunidades Regionales: Composición del Mercado por Género (2015-2020)', fontsize=16, fontweight='bold')
plt.xlabel('Porcentaje de Ventas Globales')
plt.ylabel('Género')
plt.legend(title='Regiones', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.gca().set_facecolor('none')

plt.show()

# %%



