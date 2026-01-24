# %% [markdown]
# ## **PRÁCTICA M26: SIMULACIÓN - APLICACIÓN PRÁCTICA**

# %% [markdown]
# #### **Objetivo:**
# - Definir diferentes tipos de distribuciones para las variables del modelo
# - Generar análisis de sensibilidad
# - Programar un proceso de simulación 
# - Visualizar los resultados
# - Aplicar los conceptos vistos a la realidad empresarial

# %% [markdown]
# #### **Paso a paso:**
# - Generar un archivo tipo Notebook de Python que contenga:
#     - La definición de un modelo determinístico de un cálculo de costos: presupuesto siemple con ítems, suma uno a uno
#     - La definción de distribuciones de probabilidad a las variables del modelo
#     - La ejecución de simulación aplicada al modelo con 5000 iteraciones
#     - Lectura e interpretación de resultados
#     - Visualización básica y conclusiones
#     - Análisis de sensibilidad con dos tipos de distribuciones diferentes
#     - Conclusiones finales
# ----------

# %% [markdown]
# **Contexto empresarial:**
# - Una empresa planea lanzar un nuevo producto al mercado. Antes de invertir en producción y marketing, desea estimar:
#     - La demanda esperada
#     - Los ingresos probables
#     - El riesgo de pérdidas
#     - La probabilidad de obtener utilidad 
# 
# - Supuestos 
#     - Precio de venta unitario: 100 pesos
#     - Demanda mensual esperada: 2,000 unidades
#     - Costo unitario de producción: 50 pesos
#     - Costos fijos mensuales: 20,000 pesos

# %%
# Importar paquetes necesarios
import random
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# %% [markdown]
# --------
# 1. Definición de un modelo determinístico de un calculo de costos: presupuesto simple con ítems, suma uno a uno
# --------

# %%
# Supuestos determinísticos
precio = 100
demanda = 2000
costo_unitario = 50
costos_fijos = 20000

# Cálculos determinísticos para sacar la utilidad
ingresos = precio * demanda
costos = costo_unitario * demanda + costos_fijos
utilidad = ingresos - costos
print('La utilidad es de', utilidad, 'dls si s vendieran 2000 unidades del producto.')

# Este módelo se supone debería ser lo que se espera, sin embargo en la vida real esto no es así

# %% [markdown]
# --------
# 2. La definción de distribuciones de probabilidad a las variables del modelo
# --------

# %%
# Para reflejar la realidad del mercado, introducimos incertidumbre
# Demanda - Distribución normal -> Por la variación en la aceptación del mercado
# Precio - Distribución uniforme -> Puede haber promociones y descuentos
# Costo unitario - Distribución normal -> Pueden existir variaciones en los insumos
# Costos fijos - Distribución constante -> Normalmente los costos mantienen un precio fijo

# %%
# Generación de muestras simuladas
def simular_mercado():
    demanda_sim = np.random.triangular(1000, 2000, 3000)
    precio_sim = np.random.uniform(95, 105)
    costo_unitario_sim = np.random.normal(50, 5)
    costos_fijos_sim = 20000

    ingresos = precio_sim * demanda_sim
    costos = costo_unitario_sim * demanda_sim + costos_fijos_sim
    utilidad = ingresos - costos

    return utilidad

# %% [markdown]
# --------
# 3. La ejecución de simulación aplicada al modelo con 5000 iteraciones
# --------

# %%
iteraciones = 5000

utilidad_esperada = []

for i in range (iteraciones):
    utilidad = simular_mercado()
    utilidad_esperada.append(utilidad)

utilidad_esperada[:10]

# %% [markdown]
# ------
# 4. Interpretación de resultados
# ------

# %%
# Para sacar el promedio de la ganancia esperada del mercado ()
np.mean(utilidad_esperada)

# %%
# Riesgo -> variabilidad esperada de los resultados
np.std(utilidad_esperada)

# %%
# Percentiles
np.percentile(utilidad_esperada,[5, 50, 95])

# Esto quiere decir las utilidades que podemos tener en:
# un escenario catastrofico del 5%, de un escenario medio del 50% y de un escenario optimista del 95%

# %%
# Probabilidad de exito del producto
np.mean(np.array(utilidad_esperada) >0)

# El modelo muestra que el producto es rentable en todos los escenarios simulados, el riesgo de pérdidas es muy bajo

# %% [markdown]
# -------
# 5. Visualización básica y conclusiones
# -------

# %%
# Gragicamos los resultados

plt.hist(utilidad_esperada, bins=50, density=True, color='skyblue')
plt.axvline(np.mean(utilidad_esperada), color='red', linestyle='--', label=f'Promedio: {np.mean(utilidad_esperada):.2f}')

per_5, per_95 = np.percentile(utilidad_esperada, [5, 95])

plt.axvline(per_5, color='orange', linestyle=':', label=f'Escenario 5% (Riesgo): {per_5:.2f}')
plt.axvline(per_95, color='green', linestyle=':', label=f'Escenario 95% (Optimista): {per_95:.2f}')
plt.xlabel('Utilidad mensual')
plt.ylabel('Densidad')
plt.legend()
plt.show()

# Observación: Como se muestra en la gráfica, este es un escenario muy optimista. Incluso en condiciones dificiles
# (percentil 5), el negocio es rentable y la probabilidad de perder dinero es practicamente 0

# %% [markdown]
# ------
# 6. Análisis de sensibilidad con dos tipos de distribuciones diferentes
# ------

# %%
# Supongamos que se espera una demanda de 3000 productos
def simular_mercado():
    demanda_sim = np.random.triangular(2000, 2500, 3000 )
    precio_sim = np.random.normal(95, 105)
    costo_unitario_sim = np.random.normal(50, 5)
    costos_fijos_sim = 20000

    ingresos = precio_sim * demanda_sim
    costos = costo_unitario_sim * demanda_sim + costos_fijos_sim
    utilidad = ingresos - costos

    return utilidad

# %%
iteraciones = 5000

utilidad_esperada2 = []

for i in range (iteraciones):
    utilidad2 = simular_mercado()
    utilidad_esperada2.append(utilidad2)

utilidad_esperada2[:10]

# %%
# Para sacar el promedio de la ganancia esperada del mercado
np.mean(utilidad_esperada2)

# %%
# Riesgo - variabilidad esperada de los resultados
np.std(utilidad_esperada2)

# %%
# Percentiles
np.percentile(utilidad_esperada2,[5, 50, 95])

# Esto quiere decir las utilidades que podemos tener en:
# un escenario catastrofico del 5%, de un escenario medio del 50% y de un escenario muy bueno del 95%

# %%
# Probabilidad de exito del producto
np.mean(np.array(utilidad_esperada2) >0)

# El modelo muestra que el producto no es rentable en todos los escenarios simulados, el riesgo de pérdidas es alto

# %%
# Gragicamos ambos resultados
plt.figure(figsize=(12,6))
plt.hist(utilidad_esperada, bins=50, density=True, alpha=0.5,
         label='Resultado 1(Menor Demanda)', color='skyblue')
plt.hist(utilidad_esperada2, bins=50, density=True, alpha=0.5,
         label='Resultado 2(Mayor Demanda)', color='orange')
plt.axvline(np.mean(utilidad_esperada), color='blue', linestyle= '--', linewidth=2,
            label=f'Media R1  {np.mean(utilidad_esperada):,.0f}')
plt.axvline(np.mean(utilidad_esperada2), color='red', linestyle= '--', linewidth=2,
            label=f'Media R2  {np.mean(utilidad_esperada2):,.0f}')

plt.title('Análisis de Sensibilidad: Comparación de Escenarios de Utilidad')
plt.xlabel('Utilidad Mensual ($)')
plt.ylabel('Densidad de Probabilidad')
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()

# Observaciones:Como se muestra en el gráfico, El resultado 1 representa un escenario de bajo riesgo,
# siempre vas a ganar cifras cercanas a 80,237 que es la media, mientras que en el resultado 2, representa un escenario
# de alto riesgo o alta volatilidad, aunque el promedio es más alto, tambien podrias estar ganando mucho menos o mucho mas
# de lo esperado.
# Aunque en el escenario 2 la ganancia es mayor, no representa una ganancia tan grande como lo es el enorme aumento de
# incertidumbre

# %% [markdown]
# ------
# 7. Conclusiones finales
# ------

# %% [markdown]
# **Sobre la práctica**
# - Tal y como se muestra en este ejercicio, como se observa en la primera parte, la empresa desea conocer la utilidad de un producto que desea lanzar al mercado y da como resultado el ideal de las utilidades que se tendrian si se vendieran las unidades esperadas, sin embargo en la vida real no es así, puesto que existen varios factores que influyen en la demanda de un producto.
# Para esto es que es importante utilizar estos métodos, e introducir diferentes variables y posibilidades, para ver si el producto en el peor, medio y optimista caso nos representará utilidades o pérdidas, y con base a esto tomar mejores decisiones.

# %%



