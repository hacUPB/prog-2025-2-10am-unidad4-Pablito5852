'''
Generar una lista con 100 numeros aleatorios entre 100 y 1000
Calcular el promedio de los valores de la lista
Calcular el mayor y menor numero de la lista
'''
import random
numeros = []

for i in range(100):
    aleatorio = random.randint(100,1000)
    numeros.append(aleatorio)

suma = 0
for i in numeros:
    suma += i

prom = suma / len(numeros)
print(f"promedio = {prom}")

mayor = max(numeros)
menor = min(numeros)

print(f"mayor = {mayor} ,menor = {menor}")


