entrada=input()
a,b,c=entrada.split()
a=int(a)
b=int(b)
c=int(c)
maior=a
if maior<b:
    maior=b
if maior<c:
    maior=c
print("%d eh o maior" %(maior))