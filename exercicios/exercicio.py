comp= float(input("Informe o comprimento do terreno: "))
larg=float(input("Informe a largura do terreno: "))
#assume que o q foi inserido é uma string, então tem que especificar que é float
area=comp*larg
peri=(larg+comp)*2
print("A área do terreno é %10.4f m² e o perimetro é de %10.4f metros."%(area,peri))
#Calcula o perímetro e a área de um terreno retangular.