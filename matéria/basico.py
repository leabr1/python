print("Ta funciona")
print("Sou foda")
print("N sei")
#print() imprime o q estiver dentro dos parênteses
print("5+3")
print(5+3)
#tratou como número em vez de texto
print("Prestar atenção: + (adição), - (subtração), * (multiplicação), / (divisão com resultado fracionário), // (divisão com resultado inteiro, % (módulo ou resto), ** (exponenciação ou potenciação))")
print(5/2)
print(5//2)
#criar uma variavel, não é permitido caracteres especiais
meu_nome= "Leandro Poletti de Oliveira"
valor= 544
print(meu_nome)
#python assume que o tipo passa a ser de acordo com o valor nela atribuido
#python não precisa que informe o tipo de variável
#python trabalha com os tipos básicos de programação: int (para números inteiros), float (para números reais de ponto flutuante {quebrado}, bool (valores lógicos [true e false]), str (caracteres em formato unicode [escrita])
#Em termos de tipos de dados é possível converter tipos de dados, colocando o tipo de dados a ser convertido antes da váriavel

#Para converter faça:
ValorTexto="26"
numero= int(ValorTexto)
print(numero)
print(numero+4)

#Constante é um valor usado diretamente no momento que o código é escrito e jamais será alterado

#Resultado = Entrada * 1.23 (constante)

#Há varias formas de se exibir "João tem X anos", sendo X uma variável numérica, são essas formas:

x= 45
print("João tem",x,"anos") #pythom da espaço autamatico


print("João tem %d anos" %x)
# %d é uma formatação para valores decimais, para especificar a variável, após fechar os parenteses coloque %(nome da variável)

print("João tem {} anos".format(x))
# o abre e fecha chaves indica o local a ser colocado a variável referenciada, para especificar a variável coloque .format("variável")


#OUTRO EXEMPLO:

nome="João"
idade=25
valor=40.00

print(nome,"tem",idade,"anos e apenas R$",valor,"no bolso")
#Usa que nem o JavaScript

print("%s tem %d anos e apenas R$ %f no bolso" %(nome,idade,valor))
# %s (indica formatação de string), %d (formatação para decimal valor inteiro), %f (formatação para float, valor real)
# AS VARIÁVEIS DEVEM SER COLOCADAS NA MESMA ORDEM QUE OS % na frase

print("{} tem {} anos e apenas R$ {} no bolso".format(nome,idade,valor))
# colocar a mesma ordem das variáveis que deseja exibir

#%d números inteiros
#%s strings
#%f números decimais

#entre o % e o d e o % e o f é permitido colocar a quantidade de posições desejadas

# %3d, o conteúdo da variável será apresentado com 3 posições sen zeros à esquerda, caso o número n possua menos caracteres, os espaços em branco seram preenchidos com espaço
# %03d, o conteúdo da variável será apresentado com 3 posições com zeros à esquerda, caso o número possua menos caracteres os espaços em branco seram preenchidos com 0
# %5.2f, o primeiro caractere indica o tamanho total de posições a serem ocupadas e o segundo caractere, o número de casas decimais

#Isso também funciona com o abre e fecha chaves.
# {:12} a variavel sera mostrada com 12 caracteres
# {:3} a variavel será mostrada com 3 caracteres e sem 0 caso o número total não seja atingido
# {:03} a variável será mostrada com 3 caracteres e com 0 caso o número total não seja atingido
# {:<3} 
# {:5.2f} mesma coisa que o %5.2f

print("{:12} tem {:3} anos e apenas R$ {:5.2f} no bolso".format(nome,idade,valor))
print("{:12} tem {:03} anos e apenas R$ {:5.2f} no bolso".format(nome,idade,valor))
print("{:12} tem {:<3} anos e apenas R$ {:5.2f} no bolso".format(nome,idade,valor))


#ENTRADA DE DADOS
#objetivo de solicitar ao usuário insira algo

#formas de se fazer entrada de dados com input

#print("Informe seu nome:")
#nome=input()
#print("Olá, %s" %nome)

#ou

#nome= input("Informe seu nome:")
#print("Olá %s" %nome)

#NÃO ESTÁ FUNCIONANDO NO VS CODE, PARA TRESTAR ABRA O APLICATIVO PYTHON

#Outras formas de entrada de dados

nome= input("Informe seu nome:")
nasc= int(input("Informe ano de nascimento:"))
hoje= int(input("informe ano atual"))
idade= hoje-nasc
print("Olá, %s" %nome)
print("Você possui em torno de %d anos de idade" %idade)
enter= input("\nPressione <Enter> para encerrar...")

#input lê todos os dados como string