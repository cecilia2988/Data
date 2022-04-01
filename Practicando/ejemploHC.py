from functools import reduce
from functools import reduce

Data = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
        'offline':True,
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
        'offline':False,
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
        'offline':True,
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
        'offline':False,
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
        'offline':True,
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
        'offline':False,
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
        'offline':True,
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
        'offline':False,
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
        'offline':True,
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
        'offline':False,
    },
]

diccionarioprueba={
    "uno": 1,
    "dos":2
}

def sumaTodosImpares(lista):
    suma=0
    for elemento in lista:
        if(elemento%2!=0):
            suma=suma+elemento
    
    return suma


def stringMasLarga(cadena):
    palabra=""
    listadepalabras=[]
    for i in range (0,len(cadena)):
        if (cadena[i].isspace()):
            listadepalabras.append(palabra)
            palabra=""
        elif (i==len(cadena)-1):
            palabra=palabra+ cadena[i]
            listadepalabras.append(palabra)
        palabra=palabra+cadena[i]
    listadepalabras.sort(key=len,reverse=True)
    return listadepalabras[0]



def estaOffline(Data, nombre):
    rta= False
    for elemento in Data:
        if(elemento['name']==nombre):
            rta=elemento['offline']
            break
    return rta



def actividadesEnComun(persona1, persona2):
    listacoincidencias=[]
    for n in persona1:
        if n in persona2:
            listacoincidencias.append(n)
    return listacoincidencias



def buscaDestruye(arreglo,num):
    listaauxiliar=[]
    for j in arreglo:
        if j!=num:
            listaauxiliar.append(j)
    arreglo=listaauxiliar
    return arreglo



def sumardiccionario(diccionario,x):
    if x in diccionario.keys():
        diccionario[x]=diccionario[x]+1
    else:
        diccionario[x]=1
    return diccionario
       


def sumarElTipo(arreglo):
    midic={}
    midic= reduce(sumardiccionario,arreglo,midic)
    return midic


def run():
    pass



if __name__=='__main__':
    # listanumeros=[1,2,3,4,5,6,7,8,9,10]
    # print(sumaTodosImpares(listanumeros.copy()))
    # palabralarga=stringMasLarga("Hola mundo , este es un mensaje de prueba")
    # print(palabralarga)
    # print(estaOffline(Data,"Lorena"))
    # p1=["pescar","nadar","bailar","cantar","jugar futbol","ir al cine"]
    # p2=["nadar","jugar futbol","ir al cine"]
    # lista=actividadesEnComun(p1.copy(),p2.copy())
    # print(lista)
    # numeros=[1,2,3,4,5,6,7,6,8,6,6]
    # print(buscaDestruye(numeros,6))
    # if "pepe" in diccionarioprueba.keys():
    #     print("Si")
    # else:
    #     print("No")
    # arreglo=["auto","moto","auto"]
    # dic = sumarElTipo(arreglo.copy())
    # print(dic)

    run()
