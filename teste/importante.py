dist=float(input("Insira a distância: "))
quantidade=int(input("Insira a quantidade de carros a serem comparados: "))
teste=1
nome=[]
velocidade=[]
velocidade_teste=0
while (teste<=quantidade):
    teste=teste+1
    carro_nome=input("Insira o nome do carro: ")
    nome.append(carro_nome)
    tempo=float(input("Insira o tempo do carro: "))
    velocidade_registro=dist/tempo
    velocidade.append(velocidade_registro)
    if (velocidade_teste<velocidade_registro):
        numero=teste-2
        velocidade_teste=velocidade_registro
        nome_teste=carro_nome
velocidade_maior=max(velocidade)
teste_nome=nome[numero]
#Encontrei 2 jeitos de fazer isso, um utiliza listas e o outro guarda a maior váriavel, os dois parecem estar funcionando, mas não tenho certeza
print(f"Teste 1: carro: {teste_nome} com velocidade {velocidade_maior}")
print(f"Teste 2: carro: {nome_teste} com velocidade {velocidade_teste}")
sair=(input("Gostaria de encerrar? "))
if (sair.upper()=="SIM"):
    exit()