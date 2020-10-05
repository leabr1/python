#Calcula uma média entre as notas e impeça de digitar notas maiores que 10 e menores que 0
n1= float(input("Insira a nota 1: "))
n2= float(input("Insira a nota 2: "))
media=(n1+n2)/2
if n1>10 or n1<0 or n2>10 or n2<0:
    print("Uma das notas é inválida.")
    exit()
    #sai do código
print("A média das notas é {:5.2f}".format(media))