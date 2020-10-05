idade=int(input("Insira sua idade: "))
altura=float(input("Insira sua altura (coloque . em vez de ,): "))
if idade>=30:
    print(f"Você é velho demais. Você tem :{idade} máxima = 30")
    #aparentemente se fizer desse jeito da para colocar a váriavel assim
    exit()
if altura>1.85 and idade>16:
    print("Você pode entrar no clube.")
else:
    print("Você não pode entrar no clube.")