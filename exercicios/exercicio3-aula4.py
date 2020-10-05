a=float(input("Insira o valor da hipotenusa: "))
b=float(input("Insira o valor do primeiro cateto: "))
c=float(input("Insira o valor do segundo cateto: "))

if a**2==b**2+c**2:
    print("O triângulo é pitagórico")
else:
    print("o triângulo não é pitagórico")