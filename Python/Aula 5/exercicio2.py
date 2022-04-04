import math

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))



if a ==0:
    print("Não é equação de segundo grau")
else:
    delta = b**2 -4*a*c
    if delta < 0:
        print("Não há raizes reais")
    else:
        x1 = (-b +math.sqrt(delta))/2*a
        x2 = (-b -math.sqrt(delta))/2*a
        print(f'x1 = {x1}\nx2 = {x2}')
