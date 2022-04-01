'''Dada una secuencia de números terminada en cero, elaborar un algoritmo 
para calcular el porcentaje y la suma de los números impares, el porcentaje 
y la suma de los números pares, y la suma de todos los números, y cuántos 
números fueron ingresados.'''

def run():
    pares=0
    impares=0
    cp=0
    ci=0
    num=input("Ingrese numero ")
    num=int(num)
    lista=[]
    while num!=0:
        lista.append(num)
        num=input("Ingrese numero ")
        num=int(num)
    for elemento in lista:
        if elemento%2==0:
            cp+=1
            pares=pares+elemento
        else:
            ci+=1
            impares=impares+elemento
    print("Cantidad de pares ", cp)
    print("Suma de pares: ",pares)
    print("Cantidad de impares :", ci)
    print("Suma de impares: ",impares)
    print("total de elementos: ",cp+ci)
    print("La suma de todos los elementos es: ", pares+impares)




if __name__=='__main__':
    run()