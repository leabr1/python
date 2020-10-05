#TEM OUTRO JEITO DE FAZER ISSO, É MAIS FÁCIL DO OUTRO JEITO
while True:
    compra=float(input("Insira o valor da compra: "))
    pago=float(input("Insira o calor dado pelo cliente: "))
    if (compra==0 or pago==0):
        break
    troco=pago-compra
    cinquenta=troco//50
    troco%=50
    vinte=troco//20
    troco%=20
    dez=troco//10
    troco%=10
    cinco=troco//5
    troco%=5
    dois=troco//2
    troco%=2

    print(f"A compra de {compra} terá troco de: {cinquenta} notas de R$50.00, \n{vinte} notas de R$20.00, \n{dez} notas de R$10.00, \n{cinco} notas de R$5.00, \n{dois} notas de R$2.00 e \n{troco} notas de R$1.00 ")
