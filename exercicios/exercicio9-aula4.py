v1=float(input("Insira o valor: "))
v2=float(input("Insira o valor: "))
v3=float(input("Insira o valor: "))
#TERMINAR DE FAZER, TEM QUE ORGANIZAR OS NÚMEROS DE MANEIRA A COLOCAR O NÚMERO MAIOR NA FRENTE.
if v1>=v2 and v1>=v3 and v2>=v3:
    a=v1
    b=v2
    c=v3
if v1>=v2 and v1>=v3 and v2<v3:
    a=v1
    b=v3
    c=v2
if v2>=v1 and v2>=v3 and v1>=v3:
    a=v2
    b=v1
    c=v3
if v2>=v1 and v2>=v3 and v1<v3:
    a=v2
    b=v3
    c=v1
if v3>=v1 and v3>=v2 and v2>=v1:
    a=v3
    b=v2
    c=v1
if v3>=v2 and v3>=v1 and v2<v1:
    a=v3
    b=v1
    c=v2
print(f"Maior:{a}  Intermediário:{b}  Menor:{c}")
