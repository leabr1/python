largura=float(input("Insira a largura do terreno: "))
comp=float(input("Insira o comprimento do terreno: "))
area=largura*comp
peri=(largura+comp)*2
print("O seu terreno possui %5.2f de largura e %5.2f de comprimento, fazendo com que ele possua %5.2f m² e %5.2f metros" %(largura,comp,area,peri))
