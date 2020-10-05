#Estruturas de repetição
#duas formas: while e
#While testa a condição, repetindo-a até que seja satisfeita.
print("1 para while")
print("2 para for in")
print("3 para exemplo de break e continue")
perg=int(input("Escolha o que quer fazer: "))
if (perg==1):
    x=1
    while x<=10:
        #Printou até o 10, pois a condição não começa a ser atendida depois do 10
        print(x)
        x=x+1
    print("FIM")

    resp=input("Você gostaria de começar? ")
    while resp.upper()=="SIM": #pode colocar parenteses se quiser, não é obrigado
        #A função .upper, muda os caracteres da variável para maiusculo
        print("Você disse sim.")
        resp=input("Você gostaria de continuar? ")
    print("FIM")
if (perg==2):
    print("For in é como o para no portugol studio, porém é escrito de forma diferente mas semelheante.")
    print("Estrutura do for in range:")
    print("\n\nfor <variável> in range([<inicio>,] <fim> [, <incremento>]):")
    print("Inicio e incremento são opicionais.")
    print("\nCaso não seja especificado o inicio, ele será posto como 0 ")
    print("\nSe o incremento não especificado, ele será posto como 1")
    for z in range (0, 11, 1): #tem que ter os parentêses.
        #Coloquei 11 para exibir o 10 também, porém ele está EXIBINDO 11 NÚMEROS, POIS COMEÇA NO 0
        #também pode colocar incremento decrescente como (-2)
        #se colocar o incremento, se deve colocar o ínicio (eu acho)
        print("\n",z)
    # break cria uma interrupção, ou seja, interrompe o programa
    #o continue continua o programa
    teste=input("Quer testar: ")
    if teste.upper()=="SIM":
        for t in range(0,700,1):
            print(t)
            if t == 500:
                decisao = input("Continuar? ")
                if decisao.upper() == "SIM":
                    continue
                else:
                    break
if (perg==3):
    print("Break interrompe o ciclo do programa, já continue continua o ciclo do programa.")
    for k in range(0,11,1):
        if (k==4):
            break
        print(k)
    print("\n\nO programa foi interrompido quando determinada condição foi atendida, porém só a estrutura em que ele se encontrava foi interrompida\n\n")
    for l in range(0,11,1):
        if (l==4):
            continue
        print(l)
    print("\n\nO continue continuou o ciclo do programa, mas pulou o número em que a condição foi atendida")