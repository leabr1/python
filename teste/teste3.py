while True:
    #ta errado
    n_quadrados=int(input())
    if n_quadrados==0:
        break
    area_quadrados=n_quadrados**2
    total_quadrados=0
    for divisor in range(1,area_quadrados+1):
        divisor_pratico=divisor**2
        #teste=(area_quadrados//divisor_pratico)
        teste=(area_quadrados//divisor)
        if not teste%divisor==0:
            continue
        if teste<0:
            continue
        else:
            total_quadrados=teste+total_quadrados
    print(total_quadrados)