#Live sobre estrutura de repetição
#As estruturas de repetição se repetem até que a condição não atenda mais o requisito
print("Exemplo de tabuada")
resp="S"
while (resp.upper()=="S"):
    n=int(input("Insira o valor da tabuada: "))
    i=1
    while (i<=10):
        r=n*i
        print("{:2} X {:2} = {:3}".format(n,i,r))
        i=i+1
    resp=input("Digite S para continuar / digite outro caractere para sair: ")
