inicio=1
while inicio>0:
    n=int(input())
    pontos_a=0
    pontos_b=0
    for con in range(n):
        ent=input()
        a,b=ent.split()
        a=int(a)
        b=int(b)
        if a>b:
            pontos_a=pontos_a+1
        elif b>a:
            pontos_b=pontos_b+1
    print(f"{pontos_a} {pontos_b}")