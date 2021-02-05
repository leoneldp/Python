# -*- coding: utf-8 -*-

import random
salir = False
while salir == False:
    primer_numero = random.choice([1,2,3,4,5,6])
    print("Primer Número:", primer_numero)
    segundo_numero = random.choice([1,2,3,4,5,6])
    print("Segundo Número:", segundo_numero)
    suma = primer_numero + segundo_numero
    print("La suma es:", suma)
        
    nuevamente = input("¿Desea tirar los dados nuevamente?")
    if nuevamente in ("s", "S", "si", "Si", "SI"):
        salir = False
    if nuevamente in ("n", "N", "no", "No", "NO"):
        print("Gracias por utilizar nuestros dados")
        salir = True














