'''Escribir una función que calcule el área de un círculo y otra que calcule el 
volumen de un cilindro usando la primera función'''

import math

def area_circulo(radio):
    area= math.pi * radio**2
    return area

def volumen_cilindro(radio, altura):
    volumen = altura* area_circulo(radio)
    return volumen

def run():
    radio=5
    altura=4
    print(area_circulo(radio))
    print(volumen_cilindro(radio,altura))



if __name__=='__main__':
    run()