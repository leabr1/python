#TESTE
comp=float(input("Insira o comprimento da piscina: "))
larg=float(input("Insira a largura da piscina: "))
while True:
    if larg>4 and comp>4:
        larg_teste=larg-4
        comp_teste=comp-4
        area=comp_teste*larg_teste
        print("A área da surperfície da piscina será de %5.2f m²." %(area))
        comp=float(input("Insira outro comprimento ou digite 0 para sair"))
        larg=float(input("Insira outra largura ou digite 0 para sair: "))
    else:
        print("O terreno é pequeno demais.")
        comp=float(input("Insira outro comprimento: "))
        larg=float(input("Insira outra largura: "))
    if larg==0 or comp==0:
        break