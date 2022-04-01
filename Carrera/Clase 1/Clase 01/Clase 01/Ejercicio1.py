def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    lista=[]
    resto=0
    num=0
    if (type(numero)==int or numero>=0):
        while(numero>0):
            num=num*10
            resto=numero%2
            num=num+resto
            numero=int(numero/2)
    
        return num
    else:
        return None

def run():
    print(NumeroBinario(5))




if __name__=='__main__':
    run()