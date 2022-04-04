import random
from re import S


class Estructura_Pila(object):
     def __init__(self):
         self.__list = []

    # Agregar un elemento a la Pila
     def push(self, item):
        self.__list.append(item)

    # Quitar un elemento de la Pila
     def pop(self):
        return self.__list.pop()
 
    # Obtener el elemento superior de la pila
     def peek(self):
        if self.__list:
            return self.__list[-1]
        else:
             return None
 
    # Determinar si la Pila está vacía
     def is_empty(self):
         return self.__list == []
 
     # Devuelve el número de elementos en la Pila
     def size(self):
         return len(self.__list)

     def imprimir(self):
         for i in self.__list:
             print(i)

def cargar_Pila():
    lista=[]
    lista_final= Estructura_Pila()
    index_aleatorio=0
    for i in range (1,21):
        lista.append(i)
    while(len(lista)>0):
        n=len(lista)-1
        index_aleatorio=random.randint(0,n)
        lista_final.push(lista[index_aleatorio])       
        lista.remove(lista[index_aleatorio])
    return lista_final  
    
 
def jugar(lista,cantidad):
     suma=0
     puntaje=10
     cant_falante=0
     while(cantidad>0):
         bolilla=lista.pop()
         suma=suma + bolilla
         print("Elemento ", bolilla)
         cantidad-=1
     print("Su suma fue de: ", suma)    
     if suma<=50:
        while(suma<=50):
              suma=suma + lista.pop()
              cant_falante+=1
        puntaje=puntaje-cant_falante
        print("Gano!, su puntaje fue de : " , puntaje)
     else:
         print("Perdio")


    

def run():
    s=cargar_Pila()
    bandera=False
    while(bandera==False):
        cantidad=input("Ingrese cantidad de numeros a sacar ")
        try:
            assert cantidad.isnumeric()
            jugar(s,int(cantidad))
            bandera=True
        except AssertionError:
            print("Debes ingresar un numero")

    


if __name__ == '__main__':
    run()

