''' Haga un algoritmo para una función que reciba dos parámetros N y K y que 
retorne los K dígitos más a la izquierda de N. Por ejemplo, extraerDigitos
(542207, 2) debe retornar 54'''

def lista_requerida(listadigitos,k):
    milista=[]
    for i in range(0,k):
        milista.append(listadigitos[i])
    return milista   
    


def extraer_digitos(n,k):
    lista=[]
    lista_devolver=[]
    while(n>=1):
        resto=n%10
        lista.insert(0,resto)
        n=int(n/10)
    lista_devolver= lista_requerida(lista.copy(),k)
    return lista_devolver


def run():
     n=int(input("Ingrese numero "))
     k=int(input("Ingrese cantidad de digitos"))
     print(extraer_digitos(n,k))





if __name__=='__main__':
    run()