#ESTRUTURA DE SELEÇÃO (IF)
#Checa se algo deve ou não ser executado
a=5
if a==5:
    print("O valor é igual a 5")
#É assim que escreve, é diferente de java script.
#O ínicio e fim do if é definido pelo espaço (tabulação/tab), ou seja mais a direita dentro do if, foi para esquerda fora do if e o encerra

#if... else
b=input("Bom dia, você está bem?")
if b=="sim":
    print("Que bom, eu também estou bem.")
    num=float(input("Me diga um número: "))
    #tem que indicar o tipo de número, pois se não colocar ele entende como string
    num=num*2
    #se fosse uma string, o que estava escrito seria dobrado (EX: "5"*2 = 55)
    print("O dobro do número inserido é: {}".format(num))
else:
    #tem que colocar os dois pontos
    print("Que ruim, espero que seu dia melhore")

num=int(input("Digite um número: "))
if num %2==0:
    # %2 é resto 2, provavelmente esta se referindo a segunda casa do resto da divisão
    print("O número",num,"é par!")
else:
    print("O número",num,"é impar")

#elif é igual else+if
print("1 - Mussarela")
print("2 - Calabresa")
print("3 - Lombinho")

tipo=int(input("Insira o código de sua pizza: "))
if tipo==1:
    print("Você pediu uma pizza de musssarela")

elif tipo==2:
    print("Você pediu uma pizza de calabresa")

elif tipo==3:
    print("Você pediu uma pizza de lombinho")

print("\nFim")

#OPERADORES RELACIONAIS PARA USAR NO IF
# == igual a
# > maior que
# < menor que
# >= maior ou igual que
# <= menor ou igual que
# != diferente de

#OPERADORES LÓGICOS
# and e
# or ou
# not não
print("Bom dia, estou testando o pycharm")