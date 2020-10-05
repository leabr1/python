#TESTE 1
while True:
    n = int(input("Insia um número: "))
    if n==0:
        break
    contador=0
    while not n==0:
        n_teste=n%10
        n=n//10
        if not n_teste%2==0:
            contador=contador+1
        print(f"O número inserido possui {contador} números ímpares")