#Exemplo de uso de if e else
print("Primeiro exericio: 1")
print("Segundo exercício: 2")
escolha=int(input("Escolha o exercicio a ser resolvido: "))
if escolha==1:
    print("Você entrou no exercício de calcular média: \n")
    nota1 = float(input("Insira sua nota: "))
    nota2 = float(input("Insira sua segunda nota: "))
    media = (nota2 + nota1) / 2
    if media >= 7:
        print("Você foi aprovado com média %4.2f, parabéns!" %(media))
    else:
        print("Você foi reprovado comm média %4.2f, que pena." %(media))
elif escolha==2:
    print()