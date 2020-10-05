teste=1
while True:
    acertou=0
    entrada_fazenda=""
    entrada_fazenda=input()
    x1,y1,x2,y2=entrada_fazenda.split()
    x1=int(x1)
    x2=int(x2)
    y1=int(y1)
    y2=int(y2)
    if y2>=0 and y1>y2 and y1<=10000 and x1>=0 and x2>x1 and x2<=10000:
        n_meteoro=int(input())
        if x1==0 and y1==0 and x2==0 and y2==0:
            exit()
        for con in range(n_meteoro):
            entrada_meteoro=input()
            x_meteoro,y_meteoro=entrada_meteoro.split()
            x_meteoro=int(x_meteoro)
            y_meteoro=int(y_meteoro)
            if not x_meteoro>=0 and not x_meteoro<=10000 and not y_meteoro>=0 and not y_meteoro<=10000:
                exit()
            elif x_meteoro>=x1 and x_meteoro<=x2 and y_meteoro<=y1 and y_meteoro>=y2:
                acertou=acertou+1
        print("Teste %d\n%d\n" %(teste,acertou))
        teste=teste+1