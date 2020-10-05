A=int(input())
B=int(input())
if (A<1 or B>100000):
    exit()
else:
    resto=A%B
    #É % E NÃO &
    print(resto)
