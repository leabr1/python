x=int(input())
z=int(input())
con=0
resultado=0
while z<=x:
    z=int(input())
while resultado<z:
    resultado=x+resultado
    con=con+1
    if resultado>z:
        break
    x=x+1
print(con)