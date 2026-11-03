"""Caso 2: asistencia por bloques. Complete el análisis con un ciclo for."""

asistencias = [120, 180, 210, 250, 230]
capacidad = 300

# TODO: Recorra asistencias con for para acumular el total y contar los bloques
#       que SUPERAN el 70 % de la capacidad (210 no cuenta).
total_asistencia = 0
bloques_superan = 0
for asistencia in asistencias:
    total_asistencia += asistencia
    if asistencia > (capacidad * 0.70):  # 70% de 300 es 210 (estrictamente mayor)
        bloques_superan += 1
# TODO: Calcule el promedio y su porcentaje de ocupación.
cantidad_bloques = len(asistencias)
promedio_asistencia = total_asistencia / cantidad_bloques
porcentaje_ocupacion = (promedio_asistencia / capacidad) * 100
# TODO: Clasifique el promedio: >=80 % alta; >=50 % media; si no, baja.
if porcentaje_ocupacion >= 80:
    clasificacion = "ocupación alta"
elif porcentaje_ocupacion >= 50:
    clasificacion = "ocupación media"
else:
    clasificacion = "ocupación baja"
# TODO: Muestre total, promedio, porcentaje, cantidad de bloques y estado.
print("Total asistencia:", total_asistencia)
print("Promedio de asistencia:", promedio_asistencia)
print("Porcentaje de ocupación:", f"{porcentaje_ocupacion:.0f} %")
print("Cantidad de bloques que superan el 70%:", bloques_superan)
print("Estado / Clasificación:", clasificacion)
# Con los datos base: total 990, promedio 198, 66 %, 2 bloques, ocupación media.
# Prueba de código: use temporalmente cinco bloques con 240 asistentes cada uno
# para comprobar el límite del 80 %. Después restaure la lista.
