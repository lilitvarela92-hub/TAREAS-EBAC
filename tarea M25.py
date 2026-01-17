# %% [markdown]
# ### **PRÁCTICA M25**
# 
# #### **Objetivo:** Generar el código Python sin la función estudiada y además generar el código utilizando la funcíon vista. Incluir un ejemplo por cada una.
# ##### 
# - a. Función lambda para obtener la raíz cuadrada de un número.
# - b. Función map, para obtener el largo de una cadena de palabras. 
# - Tip! La cadena tiene que ser dividida en palabras antes de empezar. 
# - c. Función reduce, que sirva para calcular el producto de una lista 
# - d. Función filter que sirva para encontrar palabras que contengan mayúsculas o números en un listado 

# %% [markdown]
# ##### **Ejercicio a:** Función lambda para obtener la raíz cuadrada de un número

# %%
# Sin función lambda
import math

def raiz_cuadrada(numero):
    return math.sqrt(numero)

# Ejemplo
numero_raiz = 100
resultado = raiz_cuadrada(numero_raiz)
print(resultado)

# %%
# Con función lambda 
import math 

# raiz_cuadrada_lambda = lambda x: math.sqrt(x)

# numero_raiz = 25
# resultado = raiz_cuadrada_lambda(numero_raiz)
# print(resultado)

print((lambda x: math.sqrt(x))(100))

# %% [markdown]
# ##### **Ejercicio b:** Función map, para obtener el largo de una cadena de palabras.

# %%
# Sin función map

cadena_original = "Práctica 25 de Python avanzado"

# Dividir la cadena en una lista de palabras
lista_palabras = cadena_original.split()

# Crear una lista vacía para almacenar los largos de las palabras
largo_palabras = []

# Iterar sobre la lista de palabras para obtener su largo
for palabra in lista_palabras:
    largo_palabras.append(len(palabra))

print(lista_palabras)
print(largo_palabras)

# %%
# Con función map

cadena_original = "Práctica 25 de Python avanzado"
lista_palabras = cadena_original.split()

largo_palabras_map = list(map(lambda palabra: len(palabra), lista_palabras))

print(lista_palabras)
print(largo_palabras_map)

# %% [markdown]
# ##### **Ejercicio c:** Función reduce, que sirva para calcular el producto de una lista 

# %%
# Sin reduce

numeros = [1, 2, 3, 4]

calcular_producto = 1

for numero in numeros:
    calcular_producto *= numero

print(numeros)
print(calcular_producto)

# %%
# Con reduce

from functools import reduce

numeros = [1, 2, 3, 4]
calculo_producto = reduce(lambda x, y: x * y, numeros)

print(calculo_producto)

# %% [markdown]
# ##### **Ejercicio d:** Función filter que sirva para encontrar palabras que contengan mayúsculas o números en un listado

# %%
# Sin función filter

listado_palabras = ["Python", "EBAC", "avanzado", "filter", "01-Sep"]

palabras_filtradas = []

# Iterar sobre lista de palabras y verificar si son mayúsculas o números según sea el caso 
for palabra in listado_palabras:
    if any(c.isupper() or c.isdigit() for c in palabra):
        palabras_filtradas.append(palabra)

# Imprimir el listado de palabras que contienen mayúscula o números 
print(palabras_filtradas)

# %%
# Con la función filter
listado_palabras = ["Python", "EBAC", "avanzado", "filter", "01-Sep"]
list(filter(lambda palabra: any(c.isupper() or c.isdigit() for c in palabra), listado_palabras))


