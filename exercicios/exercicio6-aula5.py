#Calcula o preço da compra de vários clientes
numero_clientes=int(input("Insira o número total de clientes: "))
cliente_atual=1
while cliente_atual<=numero_clientes:
    adicionar="SIM"
    total=0
    while adicionar.upper()=="SIM":
        print(f"Compra do cliente {cliente_atual}: ")
        preco=float(input("Insira o preço do produto: "))
        total=total+preco
        adicionar=input("Gostaria de adicionar mais alguma coisa? ")
    print(f"O cliente número {cliente_atual} gastou R${total}")
    cliente_atual=cliente_atual+1
print("FIM")