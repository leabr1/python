x1=int(input("Insira a posição do canto superior esquerdo da trave: "))
y1=int(input("Insira a altura do canto superior esquerdo da trave: "))
x2=int(input("Insira a posição do canto inferior direito da trave: "))
y2=int(input("Insira a altura do canto inferior direito da trave: "))
a=int(input("Insira a posição onde a bola bateu: "))
b=int(input("Insira a altura onde a bola bateu: "))
if a==x1 or a==x2 or b==y1 or b==y2:
    print("Trave")
elif a<x1 or a>x2 or b>y1 or b<y2:
    print("Fora")
elif a>x1 and a<x2 and b>y2 and b<y1:
    print("GOL")
#TEM OUTRO JEITO DE FAZER (ESTUDAR SPLIT, É SÉRIO, É IMPORTANTE DEMAIS)