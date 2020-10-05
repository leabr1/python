preco_compra=float(input("Insira o preço do item: "))
adicionar=input("Gostaria de adicionar mais alguma coisa? ")
preco_total=preco_compra
while adicionar=="sim":
    preco_compra=float(input("Insira o valor: "))
    preco_total=preco_total+preco_compra
    adicionar=input("Gostaria de adicionar mais alguma coisa? ")
preco_total=preco_total*0.80
print("O preço com desconto é %5.2f" %(preco_total))