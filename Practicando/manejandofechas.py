'''Haga una función que reciba como entrada un mes del año y determine el 
número de días transcurridos desde el comienzo del año hasta el primer día 
del mes'''

import datetime
from sqlite3 import Date
from xmlrpc.client import DateTime

def contar_dias(mes):
    date= datetime.datetime.now()
    year= int(date.strftime("%Y"))
    fecha=Date(year,mes,1)
    dias_transcurridos=fecha- Date(year,1,1)
    return dias_transcurridos


def run():
    mes=int(input("Ingrese un mes "))
    print("Dias transcurridos: ", contar_dias(mes))




if __name__=='__main__':
    run()