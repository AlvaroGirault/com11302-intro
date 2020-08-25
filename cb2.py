# -*- coding: utf-8 -*-
"""
cb2.py

Flujo: while, if

Ejercicio: for, case

"""

calificacion = [10, 7, 9]
n_calificaciones = len(calificacion)

suma = 0
i = 0 
while (i < n_calificaciones):
    suma += calificacion[i]
    i+=1
    
promedio = suma / n_calificaciones
print(promedio)

# Escribir usando for, range


calificacion = [10, 7, 5, 8, 9]
# si alguna calificacion es menor o igual a 5, promedio = 0
# usando if, break, continue


# calcula promedio descartando la calificacion mas baja 
# usando if, break, continue


