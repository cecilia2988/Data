from re import S


class Nodo():
    def __init__(self,valor) -> None:
        self.dato=valor
        self.sig =None

class ListaEnlazada():
    def __init__(self) -> None:
        self.cabezal=None

    def insertar (self,valor):
        n=Nodo(valor)
        puntero=self.cabezal
        bandera=True
        
        if puntero==None:
            self.cabezal=n
        else:
            while(bandera==True):
                if puntero.sig==None:
                    puntero.sig=n
                    bandera=False
                else:
                    puntero=puntero.sig

    def Pop (self):
        puntero=self.cabezal
        auxvalor=None
        if(puntero==None):
            return None
        elif (puntero.sig ==None):
            self.cabezal=None
            return puntero.dato
        while(True):
            if(puntero.sig.sig==None):
                auxvalor=puntero.sig.dato
                puntero.sig=None
                return auxvalor
            else:
                puntero=puntero.sig
    
    def mostrar(self):
        puntero=self.cabezal
        while(puntero !=None):
            print(puntero.dato)
            puntero=puntero.sig
    
    def contar(self):
        c=0
        puntero=self.cabezal
        while(puntero !=None):
            c+=1
            puntero=puntero.sig
        return c

    def buscar(self,valor):
        puntero=self.cabezal
        while(puntero !=None):
            if(puntero.dato==valor):
                return True
            puntero=puntero.sig
        return False

    def BuscarMax(self):
        max=self.cabezal.dato
        puntero=self.cabezal
        while(puntero!=None):
            if(puntero.dato>max):
                max=puntero.dato
            puntero=puntero.sig
        return max

    def BuscarMin(self):
        min=self.cabezal.dato
        puntero=self.cabezal
        while(puntero!=None):
            if(puntero.dato<min):
                min=puntero.dato
            puntero=puntero.sig
        return max
    

            

def run():
    lista=ListaEnlazada()
    lista.insertar(3)
    lista.insertar(5)
    lista.insertar(10)
    lista.Pop()
    lista.insertar(1)
    lista.mostrar()
    print(lista.BuscarMax())



if __name__=='__main__':
    run()