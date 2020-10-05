#Mostra a velocidade do carro mais rápido de determinado grupo em determinada distãncia
#while True , acho que roda enquanto for verdadeiro, ou seja, um programa que não para de rodar
distancia=float(input("Insira a distância percorrida em metros: "))
while distancia>0:
    quantidade=int(input("Insira a quantidade de carros a serem comparados: "))
    atual=0
    velocidade_final=0
    while (atual<=quantidade):
        carro_adicionado=input("Insira o nome do carro: ")
        tempo_adicionado=float(input("Insira o tempo do carro: "))
        if tempo_adicionado==0:
            break
        velocidade_adicionada=distancia/tempo_adicionado
        if (velocidade_adicionada>velocidade_final):
            nome=carro_adicionado
            velocidade_final=velocidade_adicionada
    print(f"O carro mais rápido foi o {nome} com {velocidade_final} m/s")
    distancia=float(input("Inisra o valor de outra distância para reiniciar o programa, ou digite 0 para encerra-lo: "))
else:
    exit()