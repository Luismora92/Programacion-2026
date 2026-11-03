"""Caso 3: comparación de precios de un producto en cinco ferias."""

producto = "Tomate"
precios = [900, 850, 1000, 950, 1200]

# TODO: Calcule promedio, mínimo, máximo y rango (máximo - mínimo).
suma_precios = sum(precios)
cantidad_precios = len(precios)
promedio = suma_precios / cantidad_precios
minimo = min(precios)
maximo = max(precios)
rango = maximo - minimo
# TODO: Recorra precios con while y un índice para contar los que SUPERAN
#       el promedio. Aumente el índice en cada vuelta para terminar el ciclo.
indice = 0
superan_promedio = 0

while indice < cantidad_precios:
    if precios[indice] > promedio:
        superan_promedio += 1
    indice += 1
# TODO: Clasifique el rango: >=300 variación alta; >=150 moderada; si no, baja.
if rango >= 300:
    clasificacion_rango = "variación alta"
elif rango >= 150:
    clasificacion_rango = "variación moderada"
else:
    clasificacion_rango = "variación baja"
# TODO: Muestre producto y todos los resultados.
print("Producto:", producto)
print(f"Promedio: ₡{promedio:.0f}")
print(f"Mínimo: ₡{minimo}")
print(f"Máximo: ₡{maximo}")
print(f"Rango: ₡{rango}")
print("Precios sobre el promedio:", superan_promedio)
print("Clasificación del rango:", clasificacion_rango)
# Con los datos base: promedio ₡980, mínimo ₡850, máximo ₡1200,
# rango ₡350, 2 precios sobre el promedio, variación alta.
# Prueba de código: use temporalmente cinco precios iguales y compruebe que
# el rango sea cero y ninguno supere el promedio. Restaure la lista.
