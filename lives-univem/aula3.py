print("Escolha o que você quer fazer: ")
print("1 = Ifs \n2 = Elif \n3 = Operadores Lógicos")
escolha=int(input("Escolha o que quer fazer: "))
if escolha==1:
    print("O if estabelece uma condição para que determinada parte do código seja executada. \nO else entra em ação quando a condição do if não é atendida")
    decisao=int(input("Escolha entre 1 e 0"))
    if decisao==1:
        print("O número é 1")
    else:
        print("O número não é 1")
if escolha==2:
    print("Elif é a junção de else e if")
if escolha==3:
    print("Os operadores lógicos são: and | or | not")
    print("Exemplo: ")
    nota=float(input("Insira sua nota: "))
    if nota>7 and nota<=9:
        print("Você passou foi bem.")
    elif nota>9:
        print("Você passou com louvor.")
    elif not nota>7 and not nota<5:
        #prestar atenção
        print("Quase não passou")
    elif nota==5 or nota<5:
        print("Você não passou")
    elif nota==0:
        print("Você não passou e tirou 0.")



simnao=input("Você gostaria de ver um exemplo de if/else/elif? Responda com sim e não")
if simnao=="sim":
    print("Exemplo de if e else: ")
    print("1 = mussarela")
    print("2 = oregano")
    print("3 = maionese")
    pizza=int(input("Escolha o pedido: "))
    if pizza==1:
        print("Você escolheu pizza de mussarela")
    elif pizza==2:
        print("Você escolheu a pizza de oregano")
    elif pizza==3:
        print("Você escolheu pizza de maionese. \nQuem é você? \nHijikata Toshiro!?")
    else:
        print("Opção invalida.")