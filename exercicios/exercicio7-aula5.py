#TESTE 1
#PARECE ESTAR FUNCIONAND, PORÉM ACHO QUE OPDE REDUZIR O CÓDIGO
n1=int(input("Insira o primeiro número: "))
n2=int(input("Insira o segundo número: "))
n1_resultado=[]
n2_resultado=[]
n1_marcador=2
n2_marcador=2
while (n1_marcador<=n1):
    n1_teste=n1/n1_marcador
    if n1%n1_marcador==0:
        n1_resultado.append(n1_teste)
    n1_marcador=n1_marcador+1
while (n2_marcador<=n2):
    n2_teste=n2/n2_marcador
    if (n2%n2_marcador==0):
        n2_resultado.append(n2_teste)
    n2_marcador=n2_marcador+1
print(f"Os divisores de {n1} são: {n1_resultado} \nOs divisores de {n2} são: {n2_resultado}")
if (sum(n2_resultado)==n1 and sum(n1_resultado)==n2):
    print("Esses são números amigos.")
else:
    print("Eles não são números amigos.")