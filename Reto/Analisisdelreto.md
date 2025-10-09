# Ejercicio de analisis

En esta reto de la unidad 4 vamos a utilizar el problema #1  de el reto de la unidad anterior donde nos dice que tenemos una aeronave con unas especificaciones que nos piden al inicio de el codigo las cuales son: el peso del aeronave($kg$), la superficie alar del aeronave($m^2$) y el coeficiente de sustentacion(adimensional). Haremos uso de las listas y diccionario para dar mayor coherencia al codigo y generar un mejor orden con los datos que encontramos a medida que avanza el codigo.

# Uso de las listas 

El uso de las listas es importante para organizar los datos encontrados mediante el codigo, en este caso las listas seran importantes para expresar los datos que obtuvimos mediante el flujo de el codigo, como lo son: las diferentes sustentaciones, las diversas velocidades y la decision que toma el piloto.

estas listas se implementaros al inicio del codigo para organizar cada uno de los datos resusltantes de nuestra simulacion,haciendo al final un print con cada una de las listas al final de el ejercicio 

# Uso de los diccionarios

Para los diccionarios se definen y guardan todos los parametros que tiene el aeronave como: la masa($kg$), la superficie alar($m^2$), el coeficiente de sustentacion maximo(adimensional), el valor de la gravedad($m/s^2$) y la densidad del aire($kg/m^3$).

esto nos sirve para parametrizar desde un inicio los valores de nuestra aeronave, en este casi ese fue el unico proposito que le dimos en nuestro codigo 

# cambios en el codigo original 

los princiaples cambios en nuestro codigo realmente fueron pocos al inicio unicamente se creo el diccionario con los parametros de el avion al igual que las listas vacioas de deciciones, sustantacion y velocidad. otro cambio importante que se hizo al inicio fue el import random para poder aleatorizar la decion dentro de nuestro codigo, ya que decicidimos dentro del bucle cambiar el print de la decicios preguntale al usuario a un random.choice. al final ya los cambios fue elos print de las listas y sus respectivos promedios.
