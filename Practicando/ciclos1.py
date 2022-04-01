'''Escribir un programa que pida al usuario un número entero positivo y 
muestre por pantalla todos los números impares desde 1 hasta ese número'''

def run():
    num= input("Ingrese numero entero positivo: ")
    try:
        assert num.isalnum() and int(num)>0
        num= int(num)
        for i in range (1,num+1):
            print(i)
            
    except AssertionError:
        print("Debes ingresar un numero entero positivo")




if __name__=='__main__':
    run()