# %% [markdown]
# ## **PRÁCTICA 29: INTERACCIÓN CON DATOS DE LA WEB**

# %% [markdown]
# ### **Objetivo:** 
# - Descargar datos de fuentes públicas en la web, hacer scrapping de los mismos y además "parsearlos" para incluirlos en estructuras internas.
# - Utilizar un API pública para obtener información.
# ------------------

# %% [markdown]
# #### 1. Importación de librerías

# %%
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import numpy as np

# %% [markdown]
# #### 2. Importación del sitio web con requests

# %%
url = 'https://books.toscrape.com/catalogue/category/books/psychology_26/index.html'

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

response = requests.get(url, headers=headers)

print('Código de respuesta HHTP:', response.status_code)
print('---------------------')
pprint(response.content[0:1000])

# %% [markdown]
# #### 3. Uso de BeautifulSoup y parseo de datos

# %%
html = BeautifulSoup(response.text, 'lxml')

for item in html.select('.product_pod'):
    try:
        print('--------------------------')
        title = item.select('h3')[0].get_text()

        print(title)

    except Exception as e:
        #raise e
        print('')

# %%
# Genera las listas para la información del sitio web
arr_title = []
arr_price = []
arr_avail = []

for item in html.select('.product_pod'):
    try:

        title = item.select_one('h3 > a').get('title')
        price= item.select_one('.price_color').get_text().strip()
        avail= item.select_one('.availability').get_text().strip()
        
        # Añadir a las listas
        arr_title.append(title)
        arr_price.append(price)
        arr_avail.append(avail)
        
    except Exception as e:
        #raise e
        print(" ")

# %%
len(arr_title)

# %%
arr_title

# %%
# Guardar el archivo 
import os
import csv
os.chdir('C:/Users/LILO/Downloads')

resultFile = open("phsicology_books.csv", "w", encoding = 'utf-8')

writer = csv.writer(resultFile)

writer.writerow(['Titulo', 'Precio', 'Disponibilidad'])

for i in range(0, len(arr_avail)):
    resultFile.write(arr_title[i] + "," + arr_price[i] + "," + arr_avail[i] + "\n")
resultFile.close()

# %% [markdown]
# ### Uso de APIS Públicas
# -----------------

# %%
import requests

url_api = 'https://dog.ceo/api/breeds/image/random'

response_api = requests.get(url_api).json()

print("URL de la imagen")
print(response_api["message"])

# %%
# Obtener las razas disponibles en la API
url = "https://dog.ceo/api/breeds/list/all"
data = requests.get(url).json()

print("Razas disponibles:")
for raza in data["message"].keys():
    print("- ", raza)

# %%
# Para obtener una raza en concreto
raza = "brabancon" 
url = f"https://dog.ceo/api/breed/{raza}/images/random"

response_api1 = requests.get(url).json()

print(f"Imagen aleatoria de la raza {raza}:")
print(response_api1["message"])

# Obtener la imagen de la raza en concreto 
from IPython.display import Image, display

url_img = requests.get(f"https://dog.ceo/api/breed/{raza}/images/random").json()["message"]
display(Image(url_img))

# %%



