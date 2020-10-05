#Mesma coisa que o jogo frogger
inicio=int(input("Insira o ponto de início: "))
fim=int(input("Insira o ponto de parada: "))
for pulo in range(inicio,fim,2):
    print(pulo)
    if inicio==0 and fim==0:
        break