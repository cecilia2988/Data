import csv
import os.path
from os import path
import os


def CargarDiccionario():
    archivo=open("Emision.csv","r", encoding="ISO-8859-1")
    linea1= archivo.readline()
    dicc_emisiones = {  'cod_pais' : [],
                    'nom_pais' : [],
                    'region' : [],
                    'anio' : [],
                    'co2' : [],
                    'co2_percapita' : []
                    
    }
    for fila in archivo.readlines():
        lista= fila.split("|")
        dicc_emisiones['cod_pais'].append(lista[0])
        dicc_emisiones['nom_pais'].append(lista[1])
        dicc_emisiones['region'].append(lista[2])
        dicc_emisiones['anio'].append(lista[3])
        if lista[4]!="":
            dicc_emisiones['co2'].append(float(lista[4].replace('.', '').replace(',', '.')))
        else:
            dicc_emisiones['co2'].append(0.0)
        if lista[5]!="\n":
            dicc_emisiones['co2_percapita'].append(float(lista[5].replace("\n", "").replace('.', '').replace(',', '.')))
        else:
            dicc_emisiones['co2_percapita'].append(0.0)


    return dicc_emisiones
            
        
    




def run():
    # variable = os.getcwd()
    # print(variable)
    
    diccionario=CargarDiccionario()
    acum=0
    for j,i in enumerate (diccionario["region"]):
        if i=="América Latina y Caribe":
            if diccionario["anio"][j]=="2010":
                acum=acum + diccionario["co2"][j]
    print(acum)



if __name__=='__main__':
    run()