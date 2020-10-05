entrada=input()
pedidos=input()
a,b,c=entrada.split()
d,e,f=pedidos.split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
e=int(e)
f=int(f)
falta=0
if a<d:
    falta=falta+(d-a)
if b<e:
    falta=falta+(e-b)
if c<f:
    falta=falta+(f-c)
print(falta)