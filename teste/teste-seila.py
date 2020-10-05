x=9
y=27
con=1
divisor_comun=1
while divisor_comun<=x and divisor_comun<=y:
    if  x%divisor_comun==0 and y%divisor_comun==0:
        print(divisor_comun)
        divisor_final=divisor_comun
    divisor_comun=divisor_comun+1