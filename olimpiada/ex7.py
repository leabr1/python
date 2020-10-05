while True:
    n_casos=int(input())
    if n_casos==0:
        break
    entrada=input()
    john=0
    maria=0
    for caso in entrada.split():
        resultado=int(caso)
        if resultado==1:
            john=john+1
        elif resultado==0:
            maria=maria+1
    print("Mary won %d times and John won %d times" %(maria,john))
