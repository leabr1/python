casos_teste=int(input("Insira a quantidade de casos de teste: "))
for caso in range(casos_teste):
    entrada=input("Insira a quantidade de figurinhas de cada um: ")
    f1,f2=entrada.split()
    f1=int(f1)
    f2=int(f2)
    mdc=f1 #pode ser f2 também
    while (f1%mdc!=0) or (f2%mdc!=0): #Esta fazendo calculo de mdc, pois busca encontrar uma solução onde ambas condições são satisfeitas
        mdc=mdc-1
    print(mdc)
