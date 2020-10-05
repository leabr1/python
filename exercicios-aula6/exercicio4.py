#NÃO ESTA FUNCIONANDO
d=int(input(""))
if d<6 or d>800008:
    exit()
d-=3
con=0
while d>=0:
    d-=1
    con=con+1
    if (con==1 and d-2==0):
        print("Saída 1")
    if (d-3)==0:
        print("Saída: 1")
        break
    d-=1
    if (d-3)==0:
        print("Saída: 2")
        break
    d-=1
    if (d-3)==0:
        print("Saída: 3")
        break
    d-=5