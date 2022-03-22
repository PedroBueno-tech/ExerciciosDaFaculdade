a = int(input("Digite A: "))
b = int(input("Digite B: "))
c = int(input("Digite C: "))

delta = b*b -4*a*c

result1 = (-b+(delta*0.5))/2*a

result2 = (-b-(delta*0.5))/2*a

print("O resultado com o delta positivo deu: ", result1)
print("O resultado com o delta negativo deu: ", result2)