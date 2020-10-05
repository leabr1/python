inserido=input()
p1,p2=inserido.split()
p1=float(p1)
p2=float(p2)
total=0
if p1==1 or p2==1:
    total=total+4
if p1==2 or p2==2:
    total=total+4.50
if p1==3 or p2==3:
    total=total+5
if p1==4 or p2==4:
    total=total+2
if p1==5 or p2==5:
    total=total+1.50
print("Total: R$ %.2f" %(total))