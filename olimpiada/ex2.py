entrada=input()
a,b,c=entrada.split()
a=float(a)
b=float(b)
c=float(c)
if b+c>a and b+a>c and c+a>b:
    perimetro=a+b+c
    print("Perimetro = %.1f" %(perimetro))
else:
    area=((a+b)*c)/2
    print("Area = %.1f" %(area))