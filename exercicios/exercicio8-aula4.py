ano=int(input("Inisra o ano: "))
if ano>2020:
    print("Ano inválido.")
    exit()
if ano%4==0 or ano%400==0:
    print("É bisexto.")
else:
    print("Não é bisexto.")