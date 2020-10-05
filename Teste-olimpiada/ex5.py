n=int(input())
coelho=0
rato=0
sapo=0
for con in range(n):
    ent=input()
    quantia,tipo=ent.split()
    quantia=int(quantia)
    if tipo=="C":
        coelho=coelho+quantia
    elif tipo=="R":
        rato=rato+quantia
    else:
        sapo=sapo+quantia
total=rato+coelho+sapo
porcento_rato=(rato*100)/total
porcento_sapo=(sapo*100)/total
porcento_coelho=(coelho*100)/total
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelho}")
print(f"Total de ratos: {rato}")
print(f"Total de sapos: {sapo}")
print("Percentual de coelhos: {:.2F} %".format(porcento_coelho))
print("Percentual de ratos: {:.2F} %".format(porcento_rato))
print("Percentual de sapos: {:.2F} %".format(porcento_sapo))