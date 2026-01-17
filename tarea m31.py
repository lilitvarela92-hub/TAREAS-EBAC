# %% [markdown]
# # **PRÁCTICA 31: Data Massaging II**
# 
# ### **Objetivos:**
# - Iniciar el uso de la estructura del DataFrame
# - Uso de la librería Pandas para combinar datos
# - Obtener estadísticas básicas
# - Filtrar por condiciones y agruparlos
# - Uso de funciones **lambda**
# ---------------------------

# %%
# Importar librerías necesarias 
import pandas as pd
import numpy as np
import os

# %% [markdown]
# 1. Generar un archivo tipo Notebook de Python que contenga el código fuente de varios ejercicios aplicados a los conceptos vistos (leer archivo fifa_eda.csv)
# -----

# %%
# Cambiar el directorio actual con chdir
os.chdir('C:/Users/LILO/Downloads')

# Leer el archivo csv
df = pd.read_csv('fifa_eda.csv')

# %% [markdown]
# 2. Visualización de una muestra de 20 líneas
# -------

# %%
df.head(21)

# %% [markdown]
# 3. Generar la media, mínimo y máximo de los jugadores en total, y por país (groupby)
# -------

# %%
# Para obtener las estadísticas globales
df.describe()

# %%
# Para obtener solo la media, el mínimo y el máximo de los jugadores en total
estadisticas = df['Overall'].agg(['mean', 'min', 'max'])
estadisticas

# %%
# Para obtener la media, el mínimo y el máximo por país (groupby)
estadisticas_pais = df.groupby('Nationality')['Overall'].agg(['mean', 'min', 'max'])
estadisticas_pais.head(100)

# %% [markdown]
# 4. Generar 2 jugadores ficticios con todos los campos del dataset y añadirlos al mismo.  Visualizarlos con .tail().  Correr nuevamente las estadísticas y compararlas.
# ------

# %%
df.tail(20)

# %%
# Crear dos jugadores nuevos
jugadores_nuevos = pd.DataFrame([
    {
        'ID': 246270, 'Name': 'Sanluis Pedro', 'Age': 25, 'Nationality': 'Ireland', 
        'Overall': 45, 'Potential': 96, 'Club': 'FC Ficticio', 'Value': 150000.0, 
        'Wage': 500.0, 'Preferred Foot': 'Right', 'International Reputation': 5.0, 
        'Skill Moves': 5.0, 'Position': 'ST', 'Joined': 2023, 'Contract Valid Until': '2025-01-01', 
        'Height': 6.0, 'Weight': 170.0, 'Release Clause': 300000.0
    },
    {
        'ID': 246271, 'Name': 'Monreal Erick', 'Age': 20, 'Nationality': 'Mexico', 
        'Overall': 98, 'Potential': 92, 'Club': 'Real Ejemplo', 'Value': 80000.0, 
        'Wage': 200.0, 'Preferred Foot': 'Left', 'International Reputation': 3.0, 
        'Skill Moves': 4.0, 'Position': 'CM', 'Joined': 2024, 'Contract Valid Until': '2025-03-01', 
        'Height': 5.9, 'Weight': 160.0, 'Release Clause': 150000.0
    }
])

# Añadirlos al DataFrame original
df_nuevo = pd.concat([df, jugadores_nuevos], ignore_index=True)

# %%
df_nuevo.tail(2)

# %%
# Correr nuevamente las estadísticas
nuevas_estadisticas = df_nuevo['Overall'].agg(['mean', 'min', 'max'])
nuevas_estadisticas

# %% [markdown]
# 5. Generar una lambda que añada la zona horaria y la capital del país de nacionalidad
# ----

# %%
# Importar librerías necesarias
from countryinfo import CountryInfo
import pycountry
import pytz

# %%
get_country_info = lambda country: (
    CountryInfo(country).capital(),
    CountryInfo(country).timezones()[0]
) if country else (None, None)

# Procesar solo países únicos
unique_countries = df["Nationality"].unique()

country_map = {}
for c in unique_countries:
    try:
        country_map[c] = get_country_info(c)
    except:
        country_map[c] = (None, None)

# Aplicar al DataFrame
df["Capital"] = df["Nationality"].map(lambda x: country_map[x][0])
df["Timezone"] = df["Nationality"].map(lambda x: country_map[x][1])

df[['Name', 'Nationality', 'Capital', 'TimeZone']].head()

# %% [markdown]
# 6. Generar una lambda que en base al potencial, añada una columna “Candidato” o “Next Year”, para el premio para el balón de oro. Jugadores con más de 85, son candidatos.
# --------

# %%
# Lambda para el premio del balón de oro
df['Candidato'] = df['Potential'].apply(lambda x: 'Candidato' if x > 85 else 'Next Year')

# Visualización final
df[['Name', 'Potential', 'Candidato']].head(10)

# %%



