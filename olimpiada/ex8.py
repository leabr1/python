while True:
    entrada=input()
    l,r=entrada.split()
    l=int(l)
    r=int(r)
    if l==0 and r==0:
        break
    soma=l+r
    print(soma)