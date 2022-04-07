def ord_por_seleccion(lista):
    aux=0
    for i in range(len(lista)-1):
        indmin=i
        cont=i+1
        while(cont<len(lista)):
            if lista[cont]<lista[indmin]:
                indmin=cont
            cont+=1
        aux=lista[i]
        lista[i]=lista[indmin]
        lista[indmin]=aux
    return lista


def run():
    lista=[5,9,3,0]
    ord_por_seleccion(lista)


if __name__=='__main__':
    run()