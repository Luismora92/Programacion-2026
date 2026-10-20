import random

# 1. Generar un número secreto al azar entre 1 y 20
numero_secreto = random.randint(1, 20)

# Inicializar la variable que contará los intentos
intentos = 0

print("¡Juego Adivina el número: frío o caliente!")

# 2 y 9. Bucle para pedir intentos hasta que acierte y romper con break
while True:
    # 3. Pedir el intento y convertirlo a entero
    intento = int(input("Intento: "))
    
    # Contar cada intento realizado
    intentos += 1
    
    # 4 y 7. Comparar el intento con el número secreto (si acierta)
    if intento == numero_secreto:
        print(f"Correcto. Adivinó en {intentos} intentos.")
        break  # Termina el ciclo con break
        
    # 5. Dar pistas de dirección (si es mayor o menor)
    if numero_secreto > intento:
        mensaje_direccion = "El número secreto es mayor."
    else:
        mensaje_direccion = "El número secreto es menor."
        
    # 6. Calcular la distancia absoluta para las pistas de temperatura
    distancia = abs(numero_secreto - intento)
    
    # Asignar pista de temperatura según la escala solicitada
    if distancia <= 2:
        mensaje_temperatura = "Hirviendo: está casi encima del número."
    elif distancia <= 5:
        mensaje_temperatura = "Caliente: está cerca."
    elif distancia <= 10:
        mensaje_temperatura = "Tibio: va por buen camino, pero falta."
    else:
        mensaje_temperatura = "Frío: está lejos."
        
    # Mostrar las pistas combinadas al usuario
    print(f"{mensaje_direccion} Pista: {mensaje_temperatura}")