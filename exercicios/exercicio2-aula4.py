p1=int(input("Insira o valor: "))
p2=int(input("Insira o valor: "))
p3=int(input("Insira o valor: "))
if p1!=1 or p1!=2 or p2!=1 or p2!=2 or p3!=1 or p3!=2:
    print("Um dos jogadores inseriu um número inválido")
    exit()
if p1==p2 and p1==p3 and p2==p3 and p3==p1:
    print("Empate")
if p1!=p2 and p1!=p3:
    #se for diferente de determinada variável, ativa a condição
    #pode colocar os parenteses
    print("Jogador 1 venceu.")
if (p2!=p1) and (p2!=p3):
    print("Jogador 2 venceu")
if p3!=p1 and p3!=p2:
    print("Jogador 3 venceu")