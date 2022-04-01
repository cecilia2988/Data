#transformar un numero en numero binario


def binario(num):
    lista=[]
    resto=0
    
    while(num>0):
        resto=num%2
        lista.insert(0,resto)
        num=int(num/2)

    return lista

def run():
    bandera=False
    while bandera==False:
        num=input("Ingrese numero: ")
        try:
            assert num.isnumeric and int(num)>=1
            num=int(num)
            print(binario(num))
            bandera=True
        except AssertionError:
            print("Debe ingresar un numero positivo")



if __name__=='__main__':
    run()