'''
Leer números enteros positivos de teclado, hasta que el usuario ingrese el 
número cero e informar cuál fue el mayor y el menor número ingresado'''

def run():
    lista=[]
    num=-1
    max=0
    while(num!=0):
        num= input("Ingrese numero positivo, cero para terminar ")
        try:
            assert num.isnumeric() and int(num) >=0
            num=int(num)
            if(num!=0):
                lista.append(num)
        except AssertionError:
            print("Debe ingresar un numero positivo ")
    print(lista)

    lista.sort()
    print("El menor de los numero es ", lista[0])
    print("El mayor de los numero es ", lista[len(lista)-1])


if __name__=='__main__':
    run()