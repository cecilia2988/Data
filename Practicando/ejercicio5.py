''' Escribir un programa que solicite el ingreso de una cantidad indeterminada 
de números mayores que 1, finalizando cuando se reciba un cero. Imprimir 
la cantidad de números primos ingresados.
'''



def primo(num):
    primo=True
    for i in range (2,num):
        if(num%i==0):
            primo=False
            break
    return primo

def run():
    n=0
    num=-1
    lista=[]
    while(num!=0):
        try:
            num=input("Ingrese numero: ")
            if num.isnumeric()==False or int(num)<0:
                raise ValueError("se debe ingresar un numero mayor a 1")
                
            num=int(num)
            if(num!=0):
                lista.append(num)
        except ValueError as ve:
            print(ve)
            break
    print(lista)
    for elemento in lista:
        if primo(elemento)==True:
            n+=1
    print("En la lista hay ", n, "cantidad de primos")        

if __name__=='__main__':
    run()