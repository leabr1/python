import math
teste=input("Insira o valor de A B C (Apenas os números, colocar ponto em vez de virgula): ")
a,b,c= teste.split()
#Estou dividindo o texto para depois coloca-los como número, prestar atenção
a=float(a)
b=float(b)
c=float(c)
delta=(b**2)-4*a*c
if (delta<0):
    print("Impossível calcular.")
else:
    x1=((-b)+(math.sqrt(delta)))/(2*a)
    x2=((-b)-(math.sqrt(delta)))/(2*a)
    print("%.5f ou %.5f" %(x1,x2))