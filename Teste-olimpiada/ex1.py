import math
ent=input()
a,b,c=ent.split()
a=float(a)
b=float(b)
c=float(c)
delta=(b**2)-(4*a*c)
if delta<0:
    print("Impossivel calcular")
    exit()
else:
    if a==0:
        print("Impossivel calcular")
        exit()
    raiz_delta=math.sqrt(delta)
    x1=(-b+raiz_delta)/(2*a)
    x2=(-b-raiz_delta)/(2*a)
    print("R1 = %.5f" %(x1))
    print("R2 = %.5f" %(x2))

