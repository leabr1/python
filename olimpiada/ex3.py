n_casos=int(input())
con_in=0
con_out=0
for caso in range(n_casos):
    x=int(input())
    if x>=10 and x<=20:
        con_in=con_in+1
    else:
        con_out=con_out+1
print("%d in" %(con_in))
print("%d out" %(con_out))