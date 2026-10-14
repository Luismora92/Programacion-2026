#Datos del producto
producto = ["Cafe", 5000, 20]
porcentaje_aumento = 20
#Descuento
descuento = producto[1] * 15 / 100
precio_promocional = producto[1] - descuento

#calculamos el ingreso actual
ingreso_actual = producto[1] * producto[2]

aumento = producto[2] * porcentaje_aumento / 100

unidades_proyectadas = aumento + producto[2]

ingreso_proyectado = precio_promocional * unidades_proyectadas

ingreso_final = ingreso_proyectado - ingreso_actual

if ingreso_final > 0:
    recomendacion = "Lanzar"
else:
    recomendacion = "No Lanzar"

print ("  Analisis de Promocion  ")
print ("Producto: ", producto[0])
print ("Precio actual:", producto[1])
print ("Unidades actuales: ", producto[2])
print ("Ingreso actual: ", ingreso_actual)
print ("Descuento:", descuento)
print (f"Precio Promocional: $ {int(precio_promocional)}")
print ("Aumento (supuesto +20%): {int(unidades_proyectadas)}")
print (f"Ingreso con promoción: ${int(ingreso_proyectado)}")
print ("Diferencia:", ingreso_final)
print (f"RECOMENDACIÓN: {recomendacion}")