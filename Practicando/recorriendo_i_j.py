def suma_diez(numeros):
    arreglo=[]
    for i in numeros:
        for j in numeros:
            if(j+i==10 and j!=i):
                if not [j,i] in arreglo and not [i,j] in arreglo:
                    arreglo.append([i,j])
    return arreglo


def run():
    num=[0,1,2,3,4,5,6,7,10]
    print(suma_diez(num.copy()))




if __name__=='__main__':
    
    run()