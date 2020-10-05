comp=float(input("Insira o comprimento da rua: "))
while comp>0:
    while comp>4:
        comp=comp-4
        resu=comp//5

        print("A rua poderá acomodar %.0f carros."%(resu))
        comp=float(input("Insira outro comprimento de rua, ou digite 0 para sair: "))
    else:
        print("Rua muito pequena.")
        comp=float(input("Insira o comprimento da rua (Digite 0 para sair)"))