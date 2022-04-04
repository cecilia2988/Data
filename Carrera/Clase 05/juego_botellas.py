"""2) Implementar un juego donde constas de 2 jarras, de capacidad 5 y 3 litros respectivamente, y debes colocar 4 litros en la jarra de 5L.
Las opciones posibles son:
* Llenar la jarra de 3 litros
* Llenar la jarra de 5 litros
* Vaciar la jarra de 3 litros
* Vaciar la jarra de 5 litros
* Verter el contenido de la jarra de 3 litros en la de 5 litros
* Verter el contenido de la jarra de 5 litros en la de 3 litros"""

from os import system


class Botellas():
     def __init__(self):
        self.jarra5 = 0
        self.jarra3 = 0

     def llenar_jarra5 (self):
        self.jarra5=5


     def llenar_jarra3(self):
         self.jarra3=3
         
     
     def _verificar(self):
         if(self.jarra5==4):
             return True

         return False

     def de_jarra5_a_jarra3(self):
          resto=3-self.jarra3
          self.jarra3=self.jarra3+ self.jarra5
          if self.jarra3>3:
              self.jarra3=3
          self.jarra5=self.jarra5-resto
          
     def de_jarra3_a_jarra5(self):
          resto=5-self.jarra5
          self.jarra5=self.jarra5+ self.jarra3
          if self.jarra5>5:
              self.jarra5=5
          if(resto<3):
            self.jarra3=self.jarra3-resto
          else:
             self.jarra3=0

     def vaciar_jarra5(self):
         self.jarra5=0
        
     def vaciar_jarra3(self):
         self.jarra3=0
     
     def mostrar_estados(self):
         cadena3="*"
         cadena3=cadena3* self.jarra3
         cadena3=cadena3 + (" "*(3-self.jarra3))
         print("               Botella 3lts","[",cadena3, "]", self.jarra3, "litros")

         cadena5="*"
         cadena5=cadena5* self.jarra5
         cadena5=cadena5 + (" "*(5-self.jarra5))
         print("               Botella 5lts", "[",cadena5, "]" , self.jarra5, "litros")

def imprimir_menu():
    print("---------------------------------------------------")
    print("OPCIONES: \n")
    print(" 1 - Llenar botella de 5 litros") 
    print(" 2 - Llenar botella de 3 litros") 
    print(" 3 - Vaciar botella de 5 litros") 
    print(" 4 - Vaciar botella de 3 litros") 
    print(" 5 - Pasar contenido de  botella de 5 litros a botella de 3 litros") 
    print(" 6 - Pasar contenido de  botella de 3 litros a botella de 5 litros") 
    print(" 7 - Terminar Juego")
    print("---------------------------------------------------")


def run():
    misbotellas= Botellas()
    dejardejugar=False
    gano= False
    
    print("Bienvenido al juego de las botellas objetivo lograr juntar 4 litros en botella de 5 litros: ")
 

    while(dejardejugar==False):
        misbotellas.mostrar_estados()
        
        imprimir_menu()
        menu=["1","2","3","4","5","6","7"]
        opcion=input("Ingrese opcion: ")
        band=False
        while(band==False):
            if(opcion in menu):
                band=True
                if(opcion=="1"):
                    misbotellas.llenar_jarra5()
                if(opcion=="2"):
                    misbotellas.llenar_jarra3()
                if(opcion=="3"):
                    misbotellas.vaciar_jarra5()
                if(opcion=="4"):
                    misbotellas.vaciar_jarra3()     
                if(opcion=="5"):
                    misbotellas.de_jarra5_a_jarra3()    
                if(opcion=="6"):
                    misbotellas.de_jarra3_a_jarra5() 
                if(opcion=="7"):
                    dejardejugar=True   
                
                
            else:
                opcion=input("Ingrese opcion: ")
        
        
        
        system("cls")
        gano=misbotellas._verificar()
        if gano==True:
            print("GANO!!!!!")
            misbotellas.mostrar_estados()
            dejardejugar=True

if __name__=='__main__':
    run()
