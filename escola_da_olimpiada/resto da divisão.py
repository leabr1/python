x=int(input())
y=int(input())
if x<y:
    aux=x
    x=y
    y=aux
for n in range(y+1,x):#tem que colocar o +1, pois pode acabar por cair e printer no primeiro valor, o que não pode
    if n%5==2 or n%5==3:
        print(n)