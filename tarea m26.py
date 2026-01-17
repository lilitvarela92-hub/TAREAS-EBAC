# %% [markdown]
# ## **TAREA M26-CD-Liliana Tamalatzi Varela**

# %% [markdown]
# #### **Objetivo:** Generar un archivo tipo Notebook en Python que contenga el código fuente de varios ejercicios aplicados a los conceptos vistos

# %%
# --- Importar librerías ---
import csv
import os
import numpy as np
from statistics import mean

# %% [markdown]
# ##### 1. Cambiar directorio a un directorio de su preferencia

# %%
# get the current working directory
cwd =os.getcwd()
# Print the current working directory
print("Current working directory: {0}".format(cwd))

# Cambiar el directorio actual con chdir
os.chdir("c:/Users/LILO/AppData/Local/Programs/Microsoft VS Code")

# Print the current workig directory
print("Current working directory: {0}".format(cwd))

# %% [markdown]
# #### 2. Leer el archivo csv mencionado

# %%
# Abre el archivo de lectura
file = open(r'C:\Users\LILO\Desktop\Height of Male and Female by Country 2022.csv',encoding='utf-8')

# Lee el archivo con el objeto csvreader
csvreader = csv.reader(file)

# Extraer los datos del DataFrame
rows = []
for row in csvreader:
    rows.append(row)

print(rows[:1])

# %% [markdown]
# #### 3. Imprimir las primeras 50 lineas

# %%
# Imprimir las primeras 50 filas del DataFrame 
rows[1:51]

# %%
# Generar los objetos necesarios 

male_height_cm = np.array(rows)
female_height_cm = np.array(rows)
male_height_ft = np.array(rows)
female_height_ft = np.array(rows)
country = np.array(rows)

type(male_height_cm[1,2])
type(female_height_cm[1,3])
type(male_height_ft[1,4])
type(female_height_ft[1,5])
type(country[1,1])

# %%
MH_cm = male_height_cm[1:,2]
FH_cm = female_height_cm[1:,3]
MH_ft = male_height_ft [1:,4]
FH_ft = female_height_ft[1:,5]
country_data = country[1:,1]

country_data

# %%
# Convertir los datos "string" a "float"
Male_Hcm = [float(numeric_string)for numeric_string in MH_cm]
Female_Hcm = [float(numeric_string)for numeric_string in FH_cm]
Male_Hft = [float(numeric_string)for numeric_string in MH_ft]
Female_Hft = [float(numeric_string)for numeric_string in FH_ft]

Female_Hft [1:10]

# %% [markdown]
# #### 4. Calcular la media, mínima y máxima altura de hombres y mujeres del data set completo 

# %%
male_mean_cm = mean(Male_Hcm)
male_min_cm = min(Male_Hcm)
male_max_cm = max(Male_Hcm)

print(f"\nAltura Masculina en cm:")
print(f"  - Media (Promedio): {male_mean_cm:.2f} cm")
print(f"  - Mínima: {male_min_cm:.2f} cm")
print(f"  - Máxima: {male_max_cm:.2f} cm")

female_mean_cm = mean(Female_Hcm)
female_min_cm = min(Female_Hcm)
female_max_cm = max(Female_Hcm)

print(f"\nAltura Femenina en ft:")
print(f"  - Media (Promedio): {female_mean_cm:.2f} cm")
print(f"  - Mínima: {female_min_cm:.2f} cm")
print(f"  - Máxima: {female_max_cm:.2f} cm")

male_mean_ft = mean(Male_Hft)
male_min_ft = min(Male_Hft)
male_max_ft = max(Male_Hft)

print(f"\nAltura Masculina en ft:")
print(f"  - Media (Promedio): {male_mean_ft:.2f} ft")
print(f"  - Mínima: {male_min_ft:.2f} ft")
print(f"  - Máxima: {male_max_ft:.2f} ft")

female_mean_ft = mean(Female_Hft)
female_min_ft = min(Female_Hft)
female_max_ft = max(Female_Hft)

print(f"\nAltura Masculina en ft:")
print(f"  - Media (Promedio): {female_mean_ft:.2f} ft")
print(f"  - Mínima: {female_min_ft:.2f} ft")
print(f"  - Máxima: {female_max_ft:.2f} ft")

# %% [markdown]
# #### 5. Obtener la data de alturas de su país de origen

# %%
country_origin = "Mexico" 

for i, pais in enumerate(country_data):
    if pais.lower() == country_origin.lower(): 
        print(f"\nAlturas en {country_origin}:") 
        print(f"Hombres: {Male_Hcm[i]} cm ({Male_Hft[i]} ft)") 
        print(f"Mujeres: {Female_Hcm[i]} cm ({Female_Hft[i]} ft)") 
        break


