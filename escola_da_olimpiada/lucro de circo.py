n_dias=int(input())
custo_por_dia=int(input())
dia=1
lucro=0
if custo_por_dia>=0 and custo_por_dia<=1000:
    while dia<=n_dias:
        lucro_por_dia=int(input())
        if not 0<= lucro_por_dia or not lucro_por_dia<1000:
            exit()
        if lucro_por_dia>custo_por_dia:
            lucro_por_dia=lucro_por_dia-custo_por_dia
            lucro=lucro_por_dia+lucro
        dia=dia+1
    print(lucro)
else:
    exit()
