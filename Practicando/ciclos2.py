'''Escribir un programa que pida al usuario un número entero y muestre por 
pantalla si es un número primo o no'''

def run():
    num = input( "Ingrese nunmero entero y positivo: ")
    primo=True
    try:
        assert num.isnumeric() and int(num)>0
        num=int(num)
        for i in range (2,num):
            if(num%i == 0):
                primo=False
                break
        if (primo):
            print("El numero ", num , " es primo")
        else:
            print("El numero ", num , "No es primo")
    except AssertionError:
        print( "Debe ingresar un numero positivo entero")                    


if __name__=='__main__':
    run()