print("Candidato 1 = 1")
print("Candidato 2 = 2")
print("Candidato 3 = 3")
votar="SIM"
candidato1=0
candidato2=0
candidato3=0
n_votos=0
while (votar.upper()=="SIM"):
    escolha=int(input("Escolha o código do candidato: "))
    if (escolha==1):
        candidato1=candidato1+1
        print("Você votou no candidato 1")
    elif (escolha==2):
        candidato2=candidato2+1
        print("Vcê votou no candidato 2")
    elif (escolha==3):
        candidato3=candidato3+1
        print("Você votou no candidato 3")
    else:
        print("Candidato invalido, tente novamente")
        n_votos=n_votos-1
    n_votos=n_votos+1
    votar=input("Digite sim caso deseje votar novamente, digite qualquer coisa para sair: ")
if (candidato1>candidato3 and candidato1>candidato2):
    print("O candidato 1 venceu a eleição com %d votos de um total de %d eleitores." %(candidato1,n_votos))
elif (candidato2>candidato1 and candidato2>candidato3):
    print("O candidato 2 venceu a eleição com %d votos de um total de %d eleitores." %(candidato2,n_votos))
elif (candidato3>candidato2 and candidato3>candidato1):
    print("O candidato 3 venceu a eleição com %d votos de um total de %d eleitores. "%(candidato3,n_votos))
else:
    print("Houve um empate entre dois ou mais candidatos, logo, as votações deverão ser refeitas.")
