n_casos=int(input())
for caso in range(n_casos):
    entrada=input()
    x,y=entrada.split()
    x=int(x)
    y=int(y)
    rafael=((3*x)**2)+(y**2)
    beto=2*(x**2)+((5*y)**2)
    carlos=(-100*x)+(y**3)
    if rafael>carlos and rafael>beto:
        print("Rafael ganhou")
    elif carlos>rafael and carlos>beto:
        print("Carlos ganhou")
    elif beto>rafael and beto>carlos:
        print("Beto ganhou")