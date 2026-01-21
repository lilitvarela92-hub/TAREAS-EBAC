# %% [markdown]
# ## **TAREA M27-AD-Liliana Tamalatzi Varela**

# %% [markdown]
# ##### **Objetivo:** Generar un archivo tipo Notebook de Python que contenga el código fuente de varios ejercicios aplicados a los conceptos vistos: 

# %% [markdown]
# #### 
# 1- Aplicar los tres puntos siguientes a un ejemplo donde se busca un archivo "test.txt" que NO existe en el directorio donde se está buscando-
# - Generar las excepciones y mensajes de error correspondientes
# - Excepciones y las funciones TRY/EXCEPT
# - Ejemplos con TRY/EXCEPT/FINALLY

# %%
# Búsqueda de archivo "test.txt" que NO EXISTE
archivo = 'test.txt'
fileContent = open(archivo, "r")

# %%
# Ejemplo utilizando Excepciones y funciones EXCEPT/TRY/ELSE/FINALLY
try:
    with open(archivo, 'r') as file:
        contenido = file.read
except FileNotFoundError:
    print(f"¡ERROR! El archivo {archivo} no fue encontrado.")
except Exception as e:
    print(f"¡ERROR INESPERADO!, ocurrió un error {e}")
else:
    print("El archivo fue encontrado exitosamente", archivo)
finally:
    print('Proceso finalizado')

# %% [markdown]
# #### 
# 2- Debugging de archivos Python. Generar una celda con una operación matemática simple

# %%
# Queremos sumar las letras a, b, c, y d y dividir entre 4 para sacar el promedio
a = 10
b = 10
c = 10
d = 10

# Se agrega la variable e y se modifica el promedio 
e = 10

# Se agrega la variable f
f = 8
promedio = a + b + c + d + e - f/ 4 
print("Promedio:",promedio)

# Como podemos ver, el resultado del promedio no es lo que esperamos, pues deberia salir 10
# Por lo tanto, es necesario hacer un debugging para saber en que linea del código estamos mal
