while True:
    entrada=input()
    m,n=entrada.split()
    m=int(m)
    n=int(n)
    total=0
    if m<=0 or n<=0:
        break
    if n<m:
        m,n=n,m
    for con in range(m,n+1):
        print(con, end=" ")
        total=total+con
    print("Sum=%d" %(total))