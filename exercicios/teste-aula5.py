resposta=input("Gostaria de começar? ")
if (resposta.upper()=="SIM"):
    for n in range(10,1000,2):
        print(n)
        #Não imprime o 1000, pois quando à variável chega nesse valor, ela foge da condição.
        #Para imprimir o 1000, poderia colocar o fim como 1002.