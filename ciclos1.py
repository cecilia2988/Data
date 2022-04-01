'''Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número'''

def run():
    num= input("Ingrese numero entero positivo")
    try:
        assert num.isalnum() and num>0
        for i in range (1,num):
            print(num)
    except AssertionError:
        print("Debes ingresar un numero entero positivo")




if __name__=='__main__':
    run()