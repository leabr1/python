
#Calcula a largura de um rio (b) sabendo os outros dois lados (a) e (c)
from math import sqrt
a=float(input("Insira o valor do cateto A do rio: "))
h=float(input("Insira o valor da hipotenusa do rio: "))
while a>0 and h>0:
    if a==0 and h==0:
        exit()
    b=sqrt(h**2-a**2)
    #b=(h**2)-(a**2)
    #b=b**0.5
    #Calcula a raiz quadrada, pois encontra o número que ao multiplica-lo por si mesmo resulta no número da variável
    print("A largura do rio é: %5.2f" %(b))
    a=float(input("Insira o valor do cateto A, ou digite 0 para sair: "))
    h=float(input("Inisra o valor da hipotenusa ou digite 0 para sair: "))