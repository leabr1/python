con=1
numero_positivo=0
while con<=6:
    numero=float(input())
    if numero>0:
        numero_positivo=numero_positivo+1
    con=con+1
print("%d valores positivos" %(numero_positivo))