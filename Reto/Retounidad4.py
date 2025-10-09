import random
# Datos del avión (entrada del usuario)
masa = float(input("Ingrese la masa del avión (kg): "))
S = float(input("Ingrese el área alar S (m^2): "))
CL_max = float(input("Ingrese el CL_max: "))

# Diccionario con los datos del avión
avion = {
    "masa": masa,
    "S": S,
    "CL_max": CL_max,
    "g": 9.81,
    "rho": 1.225
}

# Peso del avión
W = avion["masa"] * avion["g"]

# Variables iniciales
velocidad = 0
distancia = 0
a = 6.3
tiempo_total = 10

# Listas para guardar los valores de cada segundo
decisiones = []
velocidades = []
sustentaciones = []
repuesta = [0,1]

# Bucle del tiempo (simulación)
for t in range(1, tiempo_total + 1):
    decision = random.choice(repuesta) # int(input(f"Segundo {t}: ¿Acelerar? (1 = sí, 0 = no): "))
    decisiones.append(decision)

    if decision == 1:
        velocidad += a

    # Calcular sustentación
    L = 0.5 * avion["rho"] * (velocidad ** 2) * avion["S"] * avion["CL_max"]
    sustentaciones.append(L)
    velocidades.append(velocidad)

    distancia += velocidad
    print(f"Segundo {t}: velocidad = {velocidad:.2f} m/s, sustentación = {L:.2f} N")

    if L >= W:
        print(f"\nEl avión despega en el segundo {t}")
        print(f"Distancia recorrida = {distancia:.2f} m")
        break
else:
    print("\nEl avión no despegó en 10 segundos")

# Mostrar los datos guardados
print("\n--- Datos guardados ---")
print("Decisiones:", decisiones)
print("Velocidades:", velocidades)
print("Sustentaciones:", sustentaciones)

promedio_decisiones = sum(decisiones)/ len(decisiones)
print(F"El promedio de las decisiones es igual a  {promedio_decisiones}")
maximo_decisiones= max(decisiones)
print(f"el maximo de las decisiones es {maximo_decisiones}")
minimo_decisiones = min(decisiones)
print(f"el minimo de las decisiones es {minimo_decisiones}")


promedio_velocidades = sum(velocidades) / len(velocidades)
print(f"el promedio de las velocidades es igual a {promedio_velocidades} ")
maximo_velocidades = max(velocidades)
print(f"la velocidad maxima es igual a {maximo_velocidades}")
minimio_velocidades = min(velocidades)
print(f"la velocidad minima es {minimio_velocidades}")


Promedio_sustentaciones = sum(sustentaciones) / len(sustentaciones)
print(f"el promedio de las sustentaciones es {Promedio_sustentaciones}")
maximo_sustentaciones = max(sustentaciones)
print(f"la sustentacion maxima fue de {maximo_sustentaciones}")
minimo_sustentaciones = min(sustentaciones)
print(f"la sustentacion minima fue de {minimo_sustentaciones}")