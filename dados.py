# -*- coding: utf-8 -*-

import random
def tirar_dados():
    """Lanza los dados.

    Lanza un primer dado e imprime en pantalla
    el 1º número. Lanza un segundo dado e imprime
    en pantalla el 2º número. Suma ambos dados e 
    imprime en pantalla el resultado y pregunta si
    se quiere volver a tirar los dados.
    """
    primer_numero = random.choice([1,2,3,4,5,6])
    print("Primer Número:", primer_numero)
    segundo_numero = random.choice([1,2,3,4,5,6])
    print("Segundo Número:", segundo_numero)
    suma = primer_numero + segundo_numero
    print("La suma es:", suma)
    nuevamente = input("¿Desea tirar los dados nuevamente?")
    if nuevamente in ("s", "S", "si", "Si", "SI"):
        tirar_dados()
    if nuevamente in ("n", "N", "no", "No", "NO"):
        print("Gracias por utilizar nuestros dados.")
        return

tirar_dados()



