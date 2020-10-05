#O que traz o resto da divisão em python é % e não &
numero=int(input("Insira o número: "))
b = 0
con = 0
while (numero!=0):
    b+=(numero%2)*(10**con)
    numero//=2
    #Ele está adicionando o resultado (0 ou 1) vezes 10 elevado a con para aumentar o valor das casas de maneira proporcional a posição delas na conversão binaria
    #Desse modo, faz com que os números não se misturem
    con+=1
    #Adiciona um a ele mesmo
print(b)