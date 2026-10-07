"""Microreto: el portero del café."""

energia = int(input("Cuanta energia tienes de 0-100?: ")) 
trae_cafe = input("¿Traes café? (si/no): ").lower().strip() == "si"

if energia < 30 and not (trae_cafe):
    mensaje = "No tiene suficiente energia ni cafe. !No pasa!"
elif energia >= 30 or trae_cafe:
    mensaje = "!Bienvenido! Cumple con la Energia y el cafe para pasar."
else:
    mensaje = "Portero confundido, revisar respuestas"
print(mensaje)

# TODO: usa and para detectar energía baja sin café.
# TODO: usa or para permitir energía suficiente o café.
# TODO: escribe mensajes claros para cada resultado.
