


import copy


def ordenar_Diccionario(dic,clave,orden):
    if(type(dic)!=dict):
            return None
    if not clave in dic.keys():
        return None

    
    lista_ordenada=sorted(dic[clave],reverse=orden)
    dic_ordenado= copy.deepcopy(dic)
    lista_indices=[]
    for i in lista_ordenada:
        lista_indices.append(dic[clave].index(i))
    for m,j in enumerate (lista_indices):
        dic_ordenado["color"][m]=dic["color"][j]
        dic_ordenado["tipo"][m]=dic["tipo"][j]
        dic_ordenado["numero"][m]=dic["numero"][j]
  
    return dic_ordenado

def run():
    dicc = {'color':['gris','negra','celeste'],
                'tipo':['auto','moto','barco'],
                'numero':[1,2,3]}
    d= ordenar_Diccionario(dicc,"color",False)


if __name__=='__main__':
    run()