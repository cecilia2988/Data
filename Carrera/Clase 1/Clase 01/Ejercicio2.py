import math

def NumeroBinario(numero):
    '''
    Esta función recibe como parámetro un número entero mayor ó igual a cero y lo devuelve en su 
    representación binaria. Debe recibir y devolver un valor de tipo entero.
    En caso de que el parámetro no sea de tipo entero y mayor a -1 retorna nulo.
    '''
    if (numero>=0):
        fraccion, entero =math.modf(numero)
        entero= int(entero)
        resto=0
        num=0
        band=True
        c=0
        resultadofraccion=""
        numerobin=0.0
        
        #Parte entera
        while(entero>0):
            num=num*10
            resto=entero%2
            num=num+resto
            entero=int(entero/2)

        #Parte fraccionaria
        while(band==True):
            fraccion=fraccion*2
            f,e=math.modf(fraccion)
            resultadofraccion=resultadofraccion + str(int(e))
            if(f==0 or c==15):
                band=False
            else:
                c=+1
                fraccion=f
        resultadofraccion="0." + resultadofraccion
        numerobin=num+float(resultadofraccion)
        return numerobin 
    else:
        return None

def run():
    print(NumeroBinario(5.3))




if __name__=='__main__':
    run()