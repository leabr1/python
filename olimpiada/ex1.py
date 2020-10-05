
casos=int(input())
for caso in range(casos):
    entrada=input()
    ricardo,vicente=entrada.split()
    x=int(ricardo)
    y=int(vicente)
    divisor_comun = 1
    while divisor_comun <= x and divisor_comun <= y:
        if x % divisor_comun == 0 and y % divisor_comun == 0:
            divisor_final = divisor_comun
        divisor_comun = divisor_comun + 1
    print(divisor_final)