import math

graus = float(input("Digite o valor em graus para um ângulo: "))

radianos = math.radians(graus)

print("O valor do seno do ângulo é igual a: ", math.sin(radianos) )
print("O valor do cosseno do ângulo é igual a: ", math.cos(radianos))
print("O valor do tangente do ângulo é igual a: ", math.tan(radianos))
