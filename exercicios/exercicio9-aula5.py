n=int(input("Insira o número de lados do poligono: "))
while True:
    if n<4:
        print("Número inválido")
        n=int("Insira outro número de lados ou digite 0 para sair: ")
    else:
        soma=(n-2)*180
        ang=soma/n
        print("A soma dos angûlos internos resultou em %d, com cada lado possuindo %d graus" %(soma,ang))
        n = int("Insira outro número de lados ou digite 0 para sair: ")
    if n==0:
        break