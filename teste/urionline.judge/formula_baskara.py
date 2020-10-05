import math
valor=input()
a,b,c=valor.split()
delta=b**2-4*a*c
if (delta<0):
    print("Impossível calcular.")
else:
    if delta==0:
        delta=0
    x1=((-b)+(math.sqrt(delta)))/(2*a)
    x2=((-b)-(math.sqrt(delta)))/(2*a)
    print("R1 = %.5f" %(x1))
    print("R2 = %.5f" %(x2))