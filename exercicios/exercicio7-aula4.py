v1=float(input("Insira um valor: "))
v2=float(input("Insira outro valor: "))
v3=float(input("Insira mais um valor: "))

if v1>v2 and v1>v3:
    print(v1)
elif v2>v3 and v2>v1:
    print(v2)
else:
    print(v3)