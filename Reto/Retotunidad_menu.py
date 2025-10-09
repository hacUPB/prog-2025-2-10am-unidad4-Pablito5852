print("Recuerde que en el menu para obtener la opcion 2 primero debe ejecutar la opcion 1")

masa = float(input("Ingrese la masa del avión (kg): "))
S = float(input("Ingrese el área alar S (m^2): "))
CL_max = float(input("Ingrese el CL_max: "))

avion = {
    "masa": masa,
    "S": S,
    "CL_max": CL_max,
    "g": 9.81,
    "rho": 1.225
}

decisiones = []
velocidades = []
sustentaciones = []
repuesta = [0,1]
import random
control = True
while control == True:
    option = int(input("1. Entrar a la simulacion\n2. Imprimir las listas y el diccionario\n3. Salir"))
    match option:

        case 1:

            #Peso del avión
            W = avion["masa"] * avion["g"]

            # Variables iniciales
            velocidad = 0
            distancia = 0
            a = 6.3
            tiempo_total = 10

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

        case 2:
            print("La lista desiciones contiene: ")
            for desicion in decisiones:
                print(decision)
            print("la lista velocidades contiene: ")
            for velocidad in velocidades:
                print(velocidad)
            print("la lista sustentaciones contiene: ")
            for sustentacion in sustentaciones:
                print(sustentacion)
            print("EL diccionario contiene:")
            for clave, valor in avion.items():
                print(f"{clave}: {valor}")

        case 3: 
            print("Saliendo del programa... ")

        case _:
            print("opcion no valida")
    
