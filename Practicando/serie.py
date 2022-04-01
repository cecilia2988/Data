'''Escriba un programa que calcule el valor aproximado de 𝝅 usando la serie:
'''

def run():
    pi=0
    divisor=1
    for i in range (1,100):
        if(i%2==0):
            pi=pi-(4/divisor)
        else:
            pi=pi+(4/divisor)
        divisor=divisor+2
    print(pi)        




if __name__=='__main__':
    run()