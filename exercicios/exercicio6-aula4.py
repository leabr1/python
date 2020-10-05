altura=float(input("Digite sua altura: "))
sexo=input("Digite M ou F")
if sexo=="M":
    pesoHomem=(72.7 * altura)-58
    print(f"Peso ideal {pesoHomem}")
elif sexo=="F":
    pesoMulher=(62.1*altura)-44.7
    print(f"Peso ideal {pesoMulher}")
